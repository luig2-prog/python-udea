import pandas as pd
from googletrans import Translator, LANGUAGES
import time

# Diccionario para traducciones manuales rápidas y fiables de términos comunes
TRADUCCIONES_MANUALES = {
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

def traducir_con_reintento(translator, texto, lang_origen, lang_destino, max_reintentos=3, pausa_inicial=0.5):
    """Intenta traducir texto con reintentos en caso de error."""
    for intento in range(max_reintentos):
        try:
            # Pausa antes de intentar la traducción
            time.sleep(pausa_inicial * (intento + 1)) # Pausa creciente
            traduccion = translator.translate(texto, src=lang_origen, dest=lang_destino)
            if traduccion and traduccion.text:
                return traduccion.text
            else:
                # Si la traducción no devuelve texto, podría ser un error sutil
                raise ValueError("Traducción no devolvió texto")
        except Exception as e:
            print(f"    Intento {intento + 1}/{max_reintentos} fallido para '{texto}': {e}")
            if intento == max_reintentos - 1: # Si es el último intento
                print(f"    Error final al traducir '{texto}' después de {max_reintentos} intentos. Se mantiene original.")
                return texto # Devuelve el texto original si todos los reintentos fallan
    return texto # Por si acaso, devuelve original si el bucle termina inesperadamente

def traducir_csv_completo_mejorado(ruta_archivo_entrada, ruta_archivo_salida, lang_destino='es', lang_origen='en', separador=';', codificacion='utf-8'):
    """
    Versión mejorada: Lee CSV, traduce encabezados y contenido con reintentos
    y traducciones manuales para términos comunes.

    Args:
        ruta_archivo_entrada (str): Ruta del archivo CSV de entrada.
        ruta_archivo_salida (str): Ruta donde se guardará el archivo CSV traducido.
        lang_destino (str): Código del idioma de destino (por defecto 'es' para español).
        lang_origen (str): Código del idioma de origen (por defecto 'en' para inglés).
        separador (str): Separador de columnas en el CSV (por defecto ';').
        codificacion (str): Codificación del archivo de salida (por defecto 'utf-8').
    """
    print(f"Iniciando traducción MEJORADA de '{ruta_archivo_entrada}'...")
    print(f"Idioma origen: {lang_origen}, Idioma destino: {lang_destino}")
    print(f"Usando reintentos y traducciones manuales para: {list(TRADUCCIONES_MANUALES.keys())}")

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

    # --- 1. Traducir Encabezados (con reintentos) ---
    nuevos_encabezados = {}
    print("Traduciendo encabezados (con reintentos)...")
    for columna in df.columns:
        columna_para_traducir = columna.replace('_', ' ')
        texto_traducido = traducir_con_reintento(translator, columna_para_traducir, lang_origen, lang_destino)
        # Normalizar a Capitalize (Primera letra mayúscula, resto minúscula)
        nuevos_encabezados[columna] = texto_traducido.capitalize()
        print(f"  '{columna}' -> '{nuevos_encabezados[columna]}'")

    df.rename(columns=nuevos_encabezados, inplace=True)
    print("Encabezados traducidos y renombrados.")

    # --- 2. Traducir Contenido de Celdas (con lookup manual y reintentos) ---
    print("Traduciendo contenido de las celdas (esto puede tardar)...")
    df_traducido = df.copy()
    total_celdas = df.shape[0] * df.shape[1]
    celdas_procesadas = 0

    for col in df.columns:
        print(f"  Procesando columna: '{col}'")
        traducciones_columna = []
        for index, valor in df[col].items():
            celdas_procesadas += 1
            if isinstance(valor, str) and valor.strip():
                # Primero, intentar con el diccionario manual
                if valor in TRADUCCIONES_MANUALES:
                    texto_traducido_celda = TRADUCCIONES_MANUALES[valor]
                else:
                    # Si no está en el manual, usar API con reintentos
                    texto_traducido_celda = traducir_con_reintento(translator, valor, lang_origen, lang_destino)

                traducciones_columna.append(texto_traducido_celda)
            else:
                traducciones_columna.append(valor)

            if celdas_procesadas % 100 == 0:
                print(f"    Progreso: {celdas_procesadas}/{total_celdas} celdas procesadas...")

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
    # Usar un nombre diferente para este resultado mejorado
    ruta_salida = f"{nombre_base}_traducido_mejorado.{extension}"

    if 'en' in LANGUAGES and 'es' in LANGUAGES:
         traducir_csv_completo_mejorado(ruta_entrada, ruta_salida, lang_destino='es', lang_origen='en', separador=';')
    else:
        print("Error: La librería googletrans no parece soportar inglés ('en') o español ('es'). Verifica la instalación.")