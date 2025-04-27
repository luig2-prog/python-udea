import pandas as pd
from googletrans import Translator, LANGUAGES
import time

# Diccionario para traducciones manuales rápidas y fiables de TÉRMINOS COMUNES EN DATOS
TRADUCCIONES_MANUALES_DATOS = {
    'Yes': 'Sí',
    'No': 'No',
    'Male': 'Masculino',
    'Female': 'Femenino',
    'Always': 'Siempre',
    'Never': 'Nunca',
    'Sometimes': 'A veces',
    'Rarely': 'Casi nunca',
    'Most of the time': 'La mayor parte del tiempo'
    # Añadir más si es necesario
}

# Diccionario para traducciones manuales de ENCABEZADOS PROBLEMÁTICOS
# (Usa el nombre original de la columna como clave)
TRADUCCIONES_MANUALES_ENCABEZADOS = {
    'record': 'Registro', # Asegurémonos que este también esté bien
    'Felt_lonely': 'Sentirse solo', # O 'Sensación de soledad'
    'Close_friends': 'Amigos cercanos',
    'Miss_school_no_permission': 'Faltar a la escuela sin permiso', # Corregir la mala traducción
    'Other_students_kind_and_helpful': 'Otros estudiantes amables y serviciales',
    'Parents_understand_problems': 'Padres entienden problemas',
    'Most_of_the_time_or_always_felt_lonely': 'Se sintió solo la mayor parte del tiempo o siempre',
    'Were_obese': 'Tenían obesidad' # O 'Eran obesos'
    # Añadir cualquier otro encabezado que falle consistentemente
}


def traducir_con_reintento(translator, texto, lang_origen, lang_destino, max_reintentos=3, pausa_inicial=0.5):
    """Intenta traducir texto con reintentos en caso de error."""
    # No traducir si es un número o cadena vacía (ya debería estar filtrado antes, pero por seguridad)
    if not isinstance(texto, str) or not texto.strip():
         return texto

    for intento in range(max_reintentos):
        try:
            # Pausa antes de intentar la traducción
            time.sleep(pausa_inicial * (intento + 1)) # Pausa creciente
            traduccion = translator.translate(texto, src=lang_origen, dest=lang_destino)
            if traduccion and traduccion.text and traduccion.text.strip():
                 # Comprobación adicional: Si la traducción es igual al original (a veces pasa), considerarlo fallo
                 if traduccion.text.strip().lower() == texto.strip().lower() and lang_origen != lang_destino:
                      print(f"    Advertencia: Traducción de '{texto}' resultó igual al original. Intento {intento + 1}/{max_reintentos}")
                      # Continuar al siguiente intento si no es el último
                      if intento < max_reintentos - 1:
                           continue
                      else: # Si es el último intento y sigue igual, mantener original
                           raise ValueError("Traducción resultó igual al original")
                 return traduccion.text.strip() # Devolver texto limpio
            else:
                raise ValueError("Traducción no devolvió texto válido")
        except Exception as e:
            print(f"    Intento {intento + 1}/{max_reintentos} fallido para '{texto}': {e}")
            if intento == max_reintentos - 1:
                print(f"    Error final al traducir '{texto}'. Se mantiene original.")
                return texto
    return texto

def traducir_csv_final(ruta_archivo_entrada, ruta_archivo_salida, lang_destino='es', lang_origen='en', separador=';', codificacion='utf-8'):
    """
    Versión Final: Usa diccionarios manuales para datos y encabezados comunes/problemáticos,
    y API con reintentos para el resto.

    Args:
        ruta_archivo_entrada (str): Ruta del archivo CSV de entrada.
        ruta_archivo_salida (str): Ruta donde se guardará el archivo CSV traducido.
        # ... (otros args igual)
    """
    print(f"Iniciando traducción FINAL de '{ruta_archivo_entrada}'...")
    print(f"Idioma origen: {lang_origen}, Idioma destino: {lang_destino}")
    print(f"Usando traducciones manuales para encabezados: {list(TRADUCCIONES_MANUALES_ENCABEZADOS.keys())}")
    print(f"Usando traducciones manuales para datos: {list(TRADUCCIONES_MANUALES_DATOS.keys())}")

    try:
        df = pd.read_csv(ruta_archivo_entrada, sep=separador)
        print("Archivo CSV leído correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo_entrada}")
        return
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return

    df = df.fillna('')
    translator = Translator()

    # --- 1. Traducir Encabezados (Manual primero, luego API con reintentos) ---
    nuevos_encabezados = {}
    print("Traduciendo encabezados...")
    for columna in df.columns:
        texto_traducido = ""
        # Intentar primero con el diccionario manual de encabezados
        if columna in TRADUCCIONES_MANUALES_ENCABEZADOS:
            texto_traducido = TRADUCCIONES_MANUALES_ENCABEZADOS[columna]
            print(f"  '{columna}' -> '{texto_traducido}' (Manual)")
        else:
            # Si no está en manual, usar API (reemplazando '_')
            columna_para_traducir = columna.replace('_', ' ')
            print(f"  Traduciendo '{columna}' con API...")
            texto_traducido = traducir_con_reintento(translator, columna_para_traducir, lang_origen, lang_destino)
            print(f"  '{columna}' -> '{texto_traducido}' (API)")

        # Normalizar a Capitalize
        nuevos_encabezados[columna] = texto_traducido.capitalize()

    df.rename(columns=nuevos_encabezados, inplace=True)
    print("Encabezados traducidos y renombrados.")

    # --- 2. Traducir Contenido de Celdas (Manual datos primero, luego API con reintentos) ---
    print("Traduciendo contenido de las celdas (esto puede tardar)...")
    df_traducido = df.copy()
    total_celdas = df.shape[0] * df.shape[1]
    celdas_procesadas = 0

    for col in df.columns: # Iterar sobre las columnas ya renombradas
        print(f"  Procesando columna: '{col}'")
        traducciones_columna = []
        for index, valor in df[col].items(): # df tiene las columnas renombradas, pero los datos originales
            celdas_procesadas += 1
            if isinstance(valor, str) and valor.strip():
                texto_traducido_celda = ""
                # Intentar primero con el diccionario manual de datos
                if valor in TRADUCCIONES_MANUALES_DATOS:
                    texto_traducido_celda = TRADUCCIONES_MANUALES_DATOS[valor]
                else:
                    # Si no está en manual, usar API con reintentos
                    texto_traducido_celda = traducir_con_reintento(translator, valor, lang_origen, lang_destino)

                traducciones_columna.append(texto_traducido_celda)
            else:
                traducciones_columna.append(valor) # Mantener no-strings y vacíos

            if celdas_procesadas % 100 == 0:
                print(f"    Progreso: {celdas_procesadas}/{total_celdas} celdas procesadas...")

        # df_traducido tiene las columnas renombradas, así que usamos 'col' directamente
        df_traducido[col] = traducciones_columna
        print(f"  Columna '{col}' procesada.")


    print("Traducción de celdas completada.")

    # --- 3. Guardar Resultados ---
    try:
        df_traducido.to_csv(ruta_archivo_salida, index=False, sep=separador, encoding=codificacion)
        print(f"Archivo traducido guardado como: {ruta_archivo_salida}")
    except Exception as e:
        print(f"Error al guardar el archivo traducido: {e}")

# --- Ejecución ---
if __name__ == "__main__":
    ruta_entrada = 'Bullying_2018_copy.csv'
    nombre_base = ruta_entrada.rsplit('.', 1)[0]
    extension = ruta_entrada.rsplit('.', 1)[1] if '.' in ruta_entrada else 'csv'
    ruta_salida = f"{nombre_base}_traducido_final.{extension}" # Nuevo nombre de archivo

    if 'en' in LANGUAGES and 'es' in LANGUAGES:
         traducir_csv_final(ruta_entrada, ruta_salida, lang_destino='es', lang_origen='en', separador=';')
    else:
        print("Error: La librería googletrans no parece soportar inglés ('en') o español ('es'). Verifica la instalación.")