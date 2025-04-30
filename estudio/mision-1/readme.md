# Fundamentos de aprendizaje de máquina y preparación de datos

## Objetivo -

Aprender conceptos y habilidades esenciales para desarrollar y gestionar proyectos de aprendizaje de máquina, enfocandos en la identificación de problemas, la recolección, preparación y analisis de los datos.

## Tipos de aprendizaje en la IA

- Supervisados: Son entrenados con un conjunto de datos etiquetados

  Ejemplo: clasificación y regresión.

- No supervisado: Los modelos encuentran patrones en datos no etiquetados

  Ejemplo: clustering y reducción de dimensionalidad

- Reforzado: Los modelos aprenden a tomar decisiones secuenciales para maximizar una recompenza

  Ejemplos: juegos y contról robótico

## Materíal de apoyo:

[ML-Modulo3-sesion-3](./ML%20-%20Módulo%203%20-%20sesión%203_Nuevo.pptx.pdf)

[ML-Modulo3-sesion-3 drive](https://drive.google.com/file/d/1wBU0VwdR61f7IG6sDKwkcnQ6RUuAbt3s/view)

## Ejecución del proyecto

El proyecto práctico tiene como objetivo ilustrar las primeras fases del ciclo de vida de un proyecto de machine learning (ML), centrándose en la detección del problema, la identificación de datos potenciales y la identificación de los interesados, así como en el posible impacto de la solución. Los estudiantes trabajarán con un conjunto de datos públicos en el marco de las siguientes líneas:

Para la realización del proyecto se deben utilizar herramientas de análisis de datos como Jupyter Notebooks, Python, pandas y numpy.

## Tema 1: Introducción

En el campo de la inteligencia artificial (IA) y el machine learning, hay diferentes enfoques para entrenar los modelos basado en los tipos de datos y la supervisión disponible. Los tres tipos son aprendizaje supervizado, no supervizado y por refuerzo. Cada uno tiene sus propias caracteristicas, aplicaciones y ventajas.

### Aprendizaje Supervisado

Es como aprender con un maestro. El modelo se entrena usando un conjunto de datos de entrada (características) y salida correctas (estiquetas). El objetivo es que el modelo aprenda a mapear las entradas a las salidas correctas para poder hacer predicciones precisas sobre datos nuevos

Se entrena usando conjuntos de dato de entrada y salidas correctas

Aprender a mapear entradas a salidas correctas para hacer predicciones precisas

Ejemplo:

- Clasificación:

Imagina que quieres entrenar un modelo que pueda distinguir entre perros y gatos

Tienes un conjunto de fotos etiquedados como "perros" y "gatos".

Usando este conjunto de datos etiquetados el modelo aprende a reconocer patrones en las imagenes que corresponden a cada categoría

- Regresión:

Deseas predecir el precio de una casa basandose en las caracteristicas como el tamaño, número de habitaciones, ubicación, etc.

Tienes un conjunto de datos donde cada casa tiene estas características y su precio correspondiente

El modelo aprende a predecir el precio de una casa nueva basándose en estos datos

### Aprendizaje No Supervisado

Es como explorar un nuevo terreno sin un mapa.

Se entrena con un conjunto de datos sin etiquetas

El objetivo es descubrir patrones o estructuras ocultas en los datos

Eje:

- Clustering:

Tienen una gran cantidad de datos de clientes y quieres segmentarlos en diferentes grupos basados en comportamiento de compra similares.

El algoritmo de clustering puede agrupar los clientes en segmentos como "compradores frecuentes", "compradores ocasionales", etc. Sin saber de antemano cuántos o que tipo de grupos encontrar

- Reducción de dimensionalidad:

Tienes un conjunto de datos con muchas características y quieres simprificarlo para visualizarlos o para mejorar la eficiencia del modelo

Algoritmos como PCA (Analisis de Componentes Principales/Principal Component Analisys) puede reducir el número de dimensiones mientras retienen la mayor parte de la variabilidad de los datos

### Aprendizaje por Refuerzo

Es como aprender mediante ensayo y error

Aprende a tomar decisiones secuenciales interactuando con el entorno

El agente recibe recompensas o penalizaciones basadas en las acciones que toma

El objetivo es maximizar las recompensas a lo largo del tiempo

Eje:

- Juegos:

Puede aprender jugando un videojuego como (ajedrez o juego de arcade) desde cero

Prueba diferentes estrategias, recibe recompensas por ganar puntos y penalizaciones por perder vidas. Con el tiempo el agente mejora sus estrategias para maximizar su puntuación

- Robótica:

Imagina un robot que debe aprender a caminar

Al principio el robot puede caerse mucho, pero cada vez que da un paso exitoso, recibe una recompensa. A travéz de muchos intentos y errores, el robot aprende a caminar de manera estable.

Estos tres enfoques forman la base de muchas aplicaciones y avances en el campo de la IA, y cada uno tiene su propio conjunto de técnicas y algoritmos especializados.

### Material de apoyo:

[Las 3 etapas de la IA, en cuál estamos y por qué muchos piensan que la tercera puede ser fatal](https://www.youtube.com/watch?v=MgWtYXcUg9Y)

Notas: 

[¿Qué es y cómo funciona la INTELIGENCIA ARTIFICIAL?](https://www.youtube.com/watch?v=_tA5cinv0U8&t=208s)

Notas: 

[¿Qué es el Aprendizaje Supervisado y No Supervisado? | DotCSV](https://www.youtube.com/watch?v=oT3arRRB2Cw&t=1s)

Notas: 

### Ejercicio Práctico

Práctica: Identificación de Problemas por Tipo de Aprendizaje en Inteligencia Artificial.

Objetivo:
El estudiante identificará y describirá un ejemplo de problema adecuado para cada tipo de aprendizaje en inteligencia artificial: supervisado y no supervisado.

El objetivo es que comprendan las características y aplicaciones de cada enfoque de aprendizaje en el contexto de problemas reales.

- Aprendizaje supervisado

Objetivo: Comprender cómo se utiliza el aprendizaje supervisado para predecir resultados basados en datos etiquetados.

Tareas:

Identificación del Problema: Seleccionar un problema donde los datos ya están etiquetados con la salida deseada.

Ejemplo: En el contexto de la transición energética justa, se podría utilizar un modelo de aprendizaje supervisado para predecir el ahorro en la factura de electricidad de hogares que instalan paneles solares, utilizando datos históricos de consumo energético, costos de instalación y ahorro registrado.

Descripción del Enfoque: Explicar cómo se utilizaría el aprendizaje supervisado para resolver este problema.

Ejemplo: El modelo podría ser entrenado con datos históricos donde se conoce el ahorro real de cada hogar, utilizando variables como la ubicación, el tamaño del hogar, el costo de instalación y la cantidad de energía generada por los paneles solares. Luego, el modelo podría predecir el ahorro para nuevos hogares que consideren la instalación de paneles solares.

- Aprendizaje no supervisado

Objetivo: Explorar cómo el aprendizaje no supervisado puede descubrir patrones ocultos en datos sin etiquetar.

Tareas:

Identificación del Problema: Seleccionar un problema donde los datos no están etiquetados y se requiere identificar patrones o agrupaciones.

Ejemplo: Un problema de aprendizaje no supervisado podría ser agrupar comunidades en función de su perfil energético para identificar cuáles están mejor preparadas para la transición hacia energías limpias. Los datos podrían incluir el consumo de energía, la disponibilidad de recursos renovables, y las infraestructuras existentes.

Descripción del Enfoque: Explicar cómo se utilizaría el aprendizaje no supervisado para resolver este problema.

Ejemplo: Un algoritmo de clustering podría agrupar las comunidades en diferentes clusters basados en sus perfiles energéticos. Esto permitiría identificar grupos de comunidades que podrían beneficiarse de estrategias similares en la adopción de tecnologías limpias, como la instalación de parques eólicos o solares compartidos.

