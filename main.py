"""
Script de traducción automática de documentos de AstroEdu.

TODO:
- Implementar un sistema de autovalidación (similaridad? longitud?) para flaggear traducciones incorrectas

- Agustín Vallejo 2024
"""

from file_parser import load_file, save_file, TranslateUnit
from gpt import translate
from typing import List
from tqdm import tqdm
import os

def main():
    filepath = 'the-sky-at-your-fingertips-es.po'
    input_dir = 'files_pre/'
    output_dir = 'files_post/'

    # filepath = 'test2.po'
    # input_dir = 'files_test/'
    # output_dir = 'files_post/'

    # Check if there is a cache file for unfinished translations
    if os.path.exists('cache/'+filepath):
        response = input("Se ha encontrado una traducción previa. ¿Desea cargarla? (s/n): ")
        if response.lower() == 's':
            parsed_entries = load_file('cache/'+filepath)
        else:
            parsed_entries = load_file(input_dir + filepath)
    else:
        parsed_entries = load_file(input_dir + filepath)

    translated_entries: List[TranslateUnit] = []
    failed_entries: List[TranslateUnit] = []

    print("INICIANDO TRADUCCIÓN...")
    for entry in tqdm(parsed_entries):
        if entry['msgstr'] != ['']:
            translated_entries.append(entry)
            continue
        try:
            values_to_translate = entry['msgid']
            translated_values = []
            for value in values_to_translate:
                if value == "": 
                    translated_values.append("")
                else:
                    translated_value = translate(value)
                    translated_values.append(translated_value)
            entry['msgstr'] = translated_values
            translated_entries.append(entry)
        except Exception as e:
            print(f'\nFailed to translate entry. Error: {e}')
            print(f'\nEntry: {entry}')
            failed_entries.append(entry)
            response = input("¿Desea detener la traducción? (s/n): ")
            if response.lower() == 's':
                response = input("¿Desea guardar el progreso? (s/n): ")
                if response.lower() == 's':
                    save_file( 'cache/'+filepath, translated_entries )
                    save_file( 'cache/FAILED-'+filepath, failed_entries )
                break

    print("\nTRADUCCIÓN FINALIZADA. REVISE LOS RESULTADOS..")

    for entry in translated_entries:
        if entry['id'] == 0: continue
        for i, value in enumerate(entry['msgid']):
            if value == "": 
                continue
            print(f"TEXTO ORIGINAL:\n{value}")
            print(f"TEXTO TRADUCIDO:\n{entry['msgstr'][i]}\n")

    if failed_entries:
        print("\n\n### Errores:")
        for entry in failed_entries:
            print(entry)
        save_file( 'cache/FAILED-'+filepath, failed_entries )

    response = input("Por favor revise con atención los textos traducidos. ¿Desea guardar los cambios? (s/n): ")

    if response.lower() == 's':
        save_file( output_dir + filepath, translated_entries )
        print("Cambios guardados.")

if __name__ == '__main__':
    main()
