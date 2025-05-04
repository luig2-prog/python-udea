# Procesamiento de lenguaje natural (PLN)

Lenguaje natural aplicado a chatbots básicos. 


[image.png](image.png)

Pre-requisitos

Principios básicos de ciencia de datos: Comprender los principios básicos de ciencia de datos, incluyendo la carga y manipulación de datos en Python usando bibliotecas como Pandas y NumPy.

Cargar, limpiar y transformar datos: Habilidad para cargar, limpiar, y transformar datos utilizando herramientas y bibliotecas de Python.

Análisis exploratorio de datos: Habilidad para realizar un análisis exploratorio de datos, identificando patrones, tendencias y anomalías mediante técnicas de visualización y estadísticas descriptivas.

Modelos de machine learning: Implementación y evaluación de modelos de machine learning

Competencias

Capacidad de analisis de problemas y encontrar soluciones efectivas

## Contenidos

Principios de procesamiento de lenguaje natural para Chatbots básicos y despliegue de modelo.

- Procesamiento de lenguaje Natural: O limpieza y preparación de datos

Tokenización

Normalización

Eliminación de Stopwords

Lematización

Stemming

- Representación de texto: 

Bolsa de palabras

TF-IDF

- Análisis de sentimientos utilizando modelos de aprendizaje de maquina

Regresión logística

Naive Bayes

- Despliegue de Modelos

Desarrollo de APIs RESTful para el acceso a modelos

## Ejecución del proyecto

Clasificador Naive Bayes básico para procesar frases y clasificarlas en categorías como saludo, queja, reclamo, petición o despedida.

Se definirá un conjunto de datos con frases etiquetadas, creando un diccionario de palabras y calcularán frecuencias, y luego implementarán el clasificador Naive Bayes aplicando el conteo de palabras y la suavización de Laplace. 

Se probará el clasificador con nuevas clases para probar su precisión y efectividad en la categorización.

## Preparación

### Procesamiento del lenguaje natural (PLN)

Limpieza y preparación de datos:

- Tokenización:

Proceso de dividir un texto en unidades mas pequeñas, como palabras o frases. 

Facilita el analisis y manipulación de texto en tareas posteriores

Ej: "El perro corre más rápido" se convierte en ["El", "perro", "corre", rápido" ]

- Normalización:

Transformar el texto a una forma consistente y estandarizada

Conversión a minusculas, eliminación de puntuación y corrección ortograficas

Ej: "EL PERRO corre RÁPIDO" se convierte en "el perro corre rápido"

- Eliminación de Stopwords

Son palabras comunes y de poca relevancia que se eliminan del texto para reducir el ruido y centrarse en las palabras más significativas

Ej: Palabras como: "el", "de", "y" se eliminan de "El perro corre rápido" para obtener ["perro", "corre", "rápido"]

- Lemantización:

Convierte las palabras a su forma base o lema, considerando el contexto y la parte del discurso

Ayuda a agrupar palabras en el mismo significado

Ej: "corriendo" y "corre" se lemantizan a "correr"

- Stemming:

Proceso similar a lemantización, pero más rudimentario

Recorta las palabras a su raíz básica sin considerar el contexto gramatical

Ej: "corriendo" y "corre" se reduce a "corr"

