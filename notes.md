# Documentación de Traductor Automático para AstroEdu
- Agustín Vallejo 2024

A continuación se desciben los pasos para traducir documentos de AstroEdu con el presente script.

En la carpeta `po-files-pre` se encuentran los archivos `.po` que contienen la información a traducir.
En su interior hay varios párrafos con códigos:
- msgctxt: Identificador del texto a traducir.
- msgid: Texto original.
- msgstr: Texto traducido. Originalmente vacío.

El script `traducir.py` se encarga de traducir los textos de los archivos `.po` y guardarlos en la carpeta `po-files-post`. Para ello, agrupará los diferentes mensajes, los pasará por un pipeline de traducción automática con IA, y los guardará en un archivo `.po` con el mismo nombre que el original.