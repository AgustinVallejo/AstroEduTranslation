# Traductor Automático de AstroEdu

Este script de Python fue desarrollado por Agustín Vallejo en 2024 para automatizar la traducción de documentos utilizados en AstroEdu.

## Características principales

- **Automatización de traducciones**: Facilita la traducción de documentos, especialmente formatos `.po` para localización.
- **Gestión de traducciones parciales**: Permite retomar traducciones no finalizadas gracias a la gestión de un archivo de caché.
- **Revisión y manejo de errores**: Ayuda a identificar y revisar traducciones fallidas para garantizar la calidad de la traducción.

## Configuración inicial

1. **Clonar el repositorio**:
   Asegúrate de tener una copia del código fuente en tu máquina local.
    ```shell
    git clone
    ```

2. **Preparar el entorno**:
   - Es recomendable crear un entorno virtual para manejar las dependencias.
   - Instala las dependencias necesarias ejecutando:
     ```shell
     pip install -r requirements.txt
     ```
    - Crea un archivo keys.py con tus credenciales de OpenAI:
    ```python
    OPENAI_API_KEY = "your-api-key"
    ```

3. **Estructura de directorios**:
   - El script espera que los archivos a traducir estén en la carpeta `files_pre`.
   - Asegúrate de que esta carpeta contenga los archivos `.po` que necesitas traducir.

4. **Ejecución**:
   - Ejecuta el script con Python para comenzar el proceso de traducción.
   - Se te pedirá que decidas sobre acciones específicas durante el proceso, como cargar traducciones previas o detener la traducción ante errores.

5. **Revisión y finalización**:
   - Tras la traducción, revisa los resultados y confirma para guardar los cambios.
   - Los archivos traducidos se guardarán en la carpeta `files_post`.
   - Revisa especialmente:la mención de "traducción", la palabra "inglés", y conceptos técnicos que puedan haber sido mal traducidos.
   - Especialmente revisa frases que originalmente están cortadas entre dos líneas, pues la traducción puede no ser correcta.
   - En el futuro habrá una función para revisar las traducciones de manera automática.

## Uso

```shell
python main.py
