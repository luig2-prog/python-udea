import pandas as pd
from googletrans import Translator

def traducir_csv(ruta_archivo):
    """
    Lee un archivo CSV, traduce las columnas en inglés a español utilizando la librería googletrans,
    y guarda un nuevo archivo CSV con las traducciones.

    Args:
        ruta_archivo (str): La ruta del archivo CSV a traducir.
    """
    try:
        df = pd.read_csv(ruta_archivo, sep=';')
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo}")
        return

    translator = Translator()
    columnas_traducidas = {}

    for columna in df.columns:
        try:
            traduccion = translator.translate(columna, dest='es')
            columnas_traducidas[columna] = traduccion.text
        except Exception as e:
            print(f"Error al traducir la columna '{columna}': {e}")
            columnas_traducidas[columna] = columna  # Mantener el nombre original en caso de error

    df_traducido = df.rename(columns=columnas_traducidas)

    ruta_archivo_traducido = ruta_archivo.replace('.csv', '_traducido.csv')
    df_traducido.to_csv(ruta_archivo_traducido, index=False, sep=';', encoding='utf-8')
    print(f"Archivo traducido guardado como: {ruta_archivo_traducido}")

if __name__ == "__main__":
    # ruta_del_csv = input("Por favor, introduce la ruta del archivo CSV que deseas traducir: ")
    traducir_csv('Bullying_2018_copy.csv')