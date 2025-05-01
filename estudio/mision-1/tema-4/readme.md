# Tema 4: Recolección de Datos

## Recolección de Datos en el Ciclo de Vida de una Aplicación de Aprendizaje de Máquina

La recolección de datos es una fase fundamental en el ciclo de vida de una aplicación de aprendizaje de máquina, ya que la calidad y cantidad de los datos disponibles pueden determinar el éxito del modelo. A continuación, se describen los aspectos clave de esta etapa junto con ejemplos relevantes.

[KAGGLE - TODO LO QUE TIENES QUE SABER](https://www.youtube.com/watch?v=Qt-pN9CqJeo)

Plataforma con recursos para Machine Learning

## Fuentes de datos

Origenes de donse se optiene la info necesaria para entrenar y evaluar los modelos de aprendizaje de máquina

Dependen del problema especifico

Ejemplos de Fuentes de Datos:

•
Datos Públicos: Bases de datos gubernamentales, organizaciones internacionales, y repositorios abiertos.

•
Datos Privados: Datos internos de la empresa, registros históricos, datos transaccionales.

•
Datos de Sensores: Información recopilada por sensores en plantas de energía, dispositivos IoT, satélites.

•
Datos de Redes Sociales: Información extraída de plataformas como Twitter, Facebook, Instagram.
Ejemplo:

Para un proyecto de democratización de la generación y consumo energético, las fuentes de datos pueden incluir registros de consumo de energía de hogares y empresas, datos de producción de plantas solares y eólicas, y datos meteorológicos.

## Ejemplos de conjuntos de datos disponibles

Hay numerosos conjuntos de datos disponibles que pueden ser utilizados para proyectos de aprendizaje de máquina. Aquí algunos ejemplos relevantes:

1. Energía Renovable: Conjunto de datos de producción de energía solar y eólica (por ejemplo, el Open PV Project o el Global Wind Atlas).

2. Agricultura y Clima: Conjuntos de datos del Departamento de Agricultura de EE.UU. (USDA) y la Administración Nacional Oceánica y Atmosférica (NOAA).

3. Datos de Ciencia e Innovación: Conjuntos de datos de publicaciones científicas, patentes, y bases de datos de innovación (como la base de datos de la Oficina Europea de Patentes).

## Tipos de BD

Las bases de datos utilizadas para almacenar y gestionar los datos pueden variar según la estructura y el tipo de información.

Tipos de Bases de Datos:

•
Bases de Datos Relacionales (SQL): MySQL, PostgreSQL, Oracle.

•
Bases de Datos NoSQL: MongoDB, Cassandra, Redis.

•
Data Warehouses: Amazon Redshift, Google BigQuery.

•
Lakes de Datos: Apache Hadoop, Microsoft Azure Data Lake.

Ejemplo:

Una base de datos relacional puede ser utilizada para almacenar datos estructurados de consumo energético, mientras que un lake de datos podría ser adecuado para almacenar grandes volúmenes de datos no estructurados de sensores y redes sociales.

## Carga de datos:

La carga de datos implica importar y procesar los datos desde sus fuentes hasta el sistema donde se realizarán los análisis y entrenamientos de modelos.

Procesos de Carga de Datos:

•
ETL (Extracción, Transformación, Carga): Procesos que extraen datos de diversas fuentes, los transforman según las necesidades del análisis, y los cargan en un sistema de almacenamiento.

•
Stream Processing: Procesamiento en tiempo real de flujos de datos utilizando herramientas como Apache Kafka y Apache Flink.

Ejemplo:

Para un proyecto de energía solar, los datos de producción pueden ser extraídos diariamente de sensores en los paneles solares, transformados para normalizar las unidades de medida, y cargados en una base de datos central para análisis.

## Generación de datos sintéticos

Cuando los datos reales son insuficientes o difíciles de obtener, la generación de datos sintéticos puede ser una alternativa útil.

Métodos de Generación de Datos Sintéticos:

•
Modelos Estadísticos: Generar datos basados en distribuciones conocidas.

•
Simulaciones: Uso de simulaciones computacionales para crear datos realistas.

•
Algoritmos Generativos: Redes Generativas Adversarias (GANs) para generar datos que imiten características de datos reales.

Ejemplo:

En un proyecto de predicción de consumo energético, se pueden generar datos sintéticos que simulen el comportamiento de consumo de nuevos tipos de dispositivos eléctricos o patrones de uso en diferentes condiciones climáticas.

## Calidad y Cantidad de datos

La calidad y cantidad de los datos son factores cruciales que afectan el rendimiento del modelo.

Calidad de datos:

Precisión y Exactitud: Los datos deben ser correctos y representar con precisión la realidad.

Consistencia: Los datos deben ser coherentes en todos los registros y fuentes.

Completitud: No deben faltar datos esenciales.

Cantidad de datos:

Suficiencia: Debe haber suficientes datos para entrenar el modelo de manera efectiva.

Representatividad: Los datos deben representar adecuadamente todas las variaciones posibles del problema.

Ejemplo:

Para asegurar la calidad de los datos en un proyecto de energías limpias, los registros de producción de energía solar deben ser precisos, consistentes y completos. La cantidad de datos debe ser suficiente para capturar variaciones diarias y estacionales en la producción de energía.

Material complementario: 

[Tipos de datos en los entornos de Big Data](https://www.youtube.com/watch?v=dHM-kuxz4w4)

[¿Dónde Encontrar DATOS para Proyectos Data Science? ¿Qué es Kaggle?](https://www.youtube.com/watch?v=NhHTWGIglRI&t=40s)

[CURSO de PYTHON con PANDAS Para Ciencia de Datos](https://www.youtube.com/watch?v=2KCQQHpi2Qk)

[Python for Data Science - Course for Beginners (Learn Python, Pandas, NumPy, Matplotlib)](https://www.youtube.com/watch?v=LHBE6Q9XlzI)


