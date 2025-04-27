import pandas as pd
from googletrans import Translator, LANGUAGES
import time # Importar time para posibles pausas

def traducir_csv_completo(ruta_archivo_entrada, ruta_archivo_salida, lang_destino='es', lang_origen='en', separador=';', codificacion='utf-8'):
    """
    Lee un archivo CSV, traduce los encabezados (manejando '_') y el contenido
    de las celdas de texto del idioma de origen al de destino utilizando googletrans.

    Args:
        ruta_archivo_entrada (str): Ruta del archivo CSV de entrada.
        ruta_archivo_salida (str): Ruta donde se guardará el archivo CSV traducido.
        lang_destino (str): Código del idioma de destino (por defecto 'es' para español).
        lang_origen (str): Código del idioma de origen (por defecto 'en' para inglés).
        separador (str): Separador de columnas en el CSV (por defecto ';').
        codificacion (str): Codificación del archivo de salida (por defecto 'utf-8').
    """
    print(f"Iniciando traducción de '{ruta_archivo_entrada}'...")
    print(f"Idioma origen: {lang_origen}, Idioma destino: {lang_destino}")

    try:
        df = pd.read_csv(ruta_archivo_entrada, sep=separador)
        print("Archivo CSV leído correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo_entrada}")
        return
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return

    # Reemplazar valores NaN (vacíos) por cadenas vacías para evitar errores en applymap
    # y asegurarse de que no se intenten traducir.
    df = df.fillna('')

    translator = Translator()

    # --- 1. Traducir Encabezados ---
    nuevos_encabezados = {}
    print("Traduciendo encabezados...")
    for columna in df.columns:
        # Reemplazar '_' con espacios para dar más contexto al traductor
        columna_para_traducir = columna.replace('_', ' ')
        try:
            # Pausa breve para evitar posibles bloqueos por exceso de solicitudes
            time.sleep(0.1)
            traduccion = translator.translate(columna_para_traducir, src=lang_origen, dest=lang_destino)
            if traduccion and traduccion.text:
                 # Opcional: Volver a poner guiones bajos si se desea (puede ser menos legible)
                # nuevos_encabezados[columna] = traduccion.text.replace(' ', '_')
                nuevos_encabezados[columna] = traduccion.text
                print(f"  '{columna}' -> '{traduccion.text}'")
            else:
                print(f"  Advertencia: No se pudo traducir el encabezado '{columna}'. Se mantiene original.")
                nuevos_encabezados[columna] = columna
        except Exception as e:
            print(f"  Error al traducir el encabezado '{columna}': {e}. Se mantiene original.")
            nuevos_encabezados[columna] = columna # Mantener original en caso de error

    # Renombrar las columnas antes de traducir los datos
    df.rename(columns=nuevos_encabezados, inplace=True)
    print("Encabezados traducidos y renombrados.")

    # --- 2. Traducir Contenido de Celdas ---
    print("Traduciendo contenido de las celdas (esto puede tardar)...")

    # Crear un nuevo DataFrame para los datos traducidos
    df_traducido = df.copy()

    total_celdas = df.shape[0] * df.shape[1]
    celdas_procesadas = 0

    # Iterar sobre cada columna y luego cada celda de esa columna
    for col in df.columns:
        print(f"  Procesando columna: '{col}'")
        traducciones_columna = []
        for index, valor in df[col].items():
            celdas_procesadas += 1
            if isinstance(valor, str) and valor.strip(): # Solo traducir strings no vacíos
                try:
                    # Pausa breve para evitar posibles bloqueos
                    time.sleep(0.05)
                    traduccion_celda = translator.translate(valor, src=lang_origen, dest=lang_destino)
                    if traduccion_celda and traduccion_celda.text:
                        traducciones_columna.append(traduccion_celda.text)
                    else:
                         traducciones_columna.append(valor) # Mantener original si la traducción falla
                except Exception as e:
                    # Imprimir error solo una vez por valor único para no llenar la consola
                    # print(f"    Error traduciendo valor '{valor}': {e}. Se mantiene original.")
                    traducciones_columna.append(valor) # Mantener original en caso de error
            else:
                traducciones_columna.append(valor) # Mantener valores no-string o vacíos

            # Imprimir progreso cada cierto número de celdas
            if celdas_procesadas % 100 == 0:
                print(f"    Progreso: {celdas_procesadas}/{total_celdas} celdas procesadas...")

        # Actualizar la columna en el DataFrame copiado
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
    ruta_entrada = 'Bullying_2018_copy.csv' # Tu archivo de entrada
    # Construir nombre de archivo de salida automáticamente
    nombre_base = ruta_entrada.rsplit('.', 1)[0]
    extension = ruta_entrada.rsplit('.', 1)[1] if '.' in ruta_entrada else 'csv'
    ruta_salida = f"{nombre_base}_traducido_completo.{extension}"

    # Verificar si la librería googletrans soporta los idiomas (opcional pero bueno)
    if 'en' in LANGUAGES and 'es' in LANGUAGES:
         traducir_csv_completo(ruta_entrada, ruta_salida, lang_destino='es', lang_origen='en', separador=';')
    else:
        print("Error: La librería googletrans no parece soportar inglés ('en') o español ('es'). Verifica la instalación.")