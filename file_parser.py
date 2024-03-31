from typing import List, TypedDict

class TranslateUnit(TypedDict):
    id: int
    msgctxt: str
    msgid: List[str]
    msgstr: List[str]

def load_file(filepath: str) -> List[TranslateUnit]:
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    entries = content.split('\n\n')  # Split the file into blocks separated by empty lines
    parsed_entries = []

    for id, entry in enumerate(entries):
        lines = entry.split('\n')
        entry_dict: TranslateUnit = {'id': id, 'msgctxt': '', 'msgid': [], 'msgstr': []}
        current_key = ''

        for line in lines:
            if line.startswith('msgctxt'):
                current_key = 'msgctxt'
                _, value = line.split(' ', 1)
                entry_dict[current_key] = value.strip('"')
            elif line.startswith('msgid'):
                current_key = 'msgid'
                _, value = line.split(' ', 1)
                entry_dict[current_key].append(value.strip('"'))
            elif line.startswith('msgstr'):
                current_key = 'msgstr'
                _, value = line.split(' ', 1)
                entry_dict[current_key].append(value.strip('"'))
            elif line.startswith('"') and current_key in ['msgid', 'msgstr']:
                # Append subsequent lines of text to the current key
                value = line.strip('"')
                entry_dict[current_key].append(value)

        parsed_entries.append(entry_dict)

    return parsed_entries


def save_file(filepath: str, entries: List[TranslateUnit]):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('#\n')
        for entry in entries:
            if entry['id'] == 0:
                file.write('msgid ""\n')
                file.write('msgstr ')
                for msgstr in entry['msgstr']:
                    file.write(f'"{msgstr}"\n')
                file.write('\n')
            else:
                file.write(f'msgctxt "{entry["msgctxt"]}"\n')
                file.write('msgid ')
                for msgid in entry['msgid']:
                    file.write(f'"{msgid}"\n')
                file.write('msgstr ')
                for msgstr in entry['msgstr']:
                    file.write(f'"{msgstr}"\n')
                file.write('\n')
