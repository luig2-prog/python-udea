# Tema 1: Procesamiento del lenguaje natural

## Limpieza y Preprocesamiento de Datos

Es una etapa esencial en el machine learning, especialmente en el procesamiento del lenguaje natural. 

Esta etapa se encarga de preparar los datos textuales para que los modelos puedan analizarlos y aprender de ellos de manera efectiva

A travez de la tokenización, normalización, eliminación de stopwords, lematización y stemming, se transforma y simplifica el texto

Esto mejora la precisión y eficacia en tareas como la clasificación de texto, analisis de sentimientos, y la implementación de chatbots que interactuen de manera natural con los usuarios

### Tokenización: 

Proceso de dividir un texto en unidades más pequeñas llamadas tokens, pueden ser palabras o frases

Ej: 

Si el usuario usuario escribe: "Quiero hacer un reclamo sobre mi última compla", la tokenización separa la oración en tokens como: ["Quiero", "hacer", "un", "reclamo", "sobre", "mi", "última", "compra"]

Esto facilita al chatbot identificar que el mensaje es sobre un "reclamo"

### Normalización:

Transforma las palabras a una forma estándar como convertir todo el texto en minusculas, eliminar signos de puntuación o normalizar carácteres

Ej:

En el mensaje "QUIERO HACER UN RECLAMO!!!", la normalización convertirá el texto a minusculas y eliminará signos de puntuación, dando como resultado:

"quiero hacer un reclamo"

Esto para que el chatbot procese el mensaje de manera uniforme

### Eliminación de `stopwords`

Remueve las palabras comunes que no añaden valor significativo al análisis, como "el", "y", "de".

Ej:

En la frase "quiero hacer un reclamo sobre el servicio", las stopwords como "quiero", "un", "sobre", "el" podrían eliminarse, dejando como resultado:

"hacer reclamo servicio" 

Esto ayuda al chatbot a centrarse en las palabras claves como "reclamo" y "servicio"

### Lematización

Reduce las palabras en su forma base o lema, teniendo en cuenta el contexto y la gramatica

Ej: 

En la frase "Estoy enviando una petición", la lemanización podría convertir "enviando" en "enviar" y "petición" en "petición", ayudando a identificar la acción principal como "enviar" y la categoría como "petición

### Stemming

Reduce las palabras a su raíz eliminando prefijos y sufijos, sin considerar el contexto gramatical

Ej: 

En la frase "estoy solicitando información" el stemming podría convertir la palabra "solicitando" en "solicit" ayudando al chatbot a reconocer la intención del usuario, que es "solicitar"

