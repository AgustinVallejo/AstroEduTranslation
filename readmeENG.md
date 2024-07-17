
# AstroEdu Automatic Translator

This Python script was developed by Agustín Vallejo in 2024 to automate the translation of documents used in AstroEdu.

## Main Features

- **Translation Automation**: Facilitates the translation of documents, especially `.po` formats for localization.
- **Partial Translation Management**: Allows resuming unfinished translations through cache file management.

## Initial Setup

1. **Clone the repository**:
   Make sure you have a copy of the source code on your local machine.
    ```shell
    git clone https://github.com/AgustinVallejo/AstroEduTranslation.git
    ```

2. **Prepare the environment**:
   - It is recommended to create a virtual environment to handle dependencies.
   - Install the necessary dependencies by running:
     ```shell
     pip install -r requirements.txt
     ```
   - Create a keys.py file with your OpenAI credentials:
     ```python
     OPENAI_API_KEY = "your-api-key"
     ```

3. **Directory structure**:
   - The script expects the files to be translated to be in the `files_pre` folder.
   - Ensure this folder contains the `.po` files you need to translate.

4. **Execution**:
   - Run the script with Python to start the translation process.
   - You will be prompted to decide on specific actions during the process, such as loading previous translations or stopping the translation in case of errors.

5. **Review and Completion**:
   - After the translation, review the results and confirm to save the changes.
   - The translated files will be saved in the `files_post` folder.
   - Pay special attention to:
      - The mention of "English" as the original language, as it will be translated literally.
      - Technical concepts that may have been mistranslated.
      - Links or HTML formats.
      - Words that the AI refused to translate due to its guidelines.
   - Especially review phrases that were originally split between two lines, as the translation may not be correct.

## Usage

Edit [this section of the `main.py` file](https://github.com/AgustinVallejo/AstroEduTranslation/blob/d6695c0ebc3566fd0a7589a05df8a3be29ee688f/main.py#L17), which contains the reference to the file you want to translate.

```shell
python main.py
```
