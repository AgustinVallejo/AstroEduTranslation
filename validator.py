from file_parser import load_file, save_file, TranslateUnit

def validate_entry(entry: TranslateUnit):
    # Checks and corrects the following rules:
    # 0. Don't enforce but print a warning if msgid and msgstr have different number of lines.
    # 1. msgstr and msgid must have the same casing on start character.
    # 2. msgstr and msgid must have the same punctuation at the end.
    # 3. Don't enforce but print a warning if msgid and msgstr have different lengths up to 20%.
    
    end_characters = ['.', ',', '!', '?', ' ']

    # Check rule 0
    if len(entry['msgid']) != len(entry['msgstr']):
        print(f'Warning: msgid and msgstr have different number of lines at entry {entry["id"]}')

    for i in range(len(entry['msgid'])):
        msgid = entry['msgid'][i]
        msgstr = entry['msgstr'][i]
        
        # Skip empty strings
        if len(msgid) < 2 or len(msgstr) < 2:
            continue

        # Check rule 1
        if msgid[0].isupper():
            msgstr = msgstr[0].upper() + msgstr[1:]
        elif msgid[0].islower():
            msgstr = msgstr[0].lower() + msgstr[1:]

        # Check rule 2
        if msgid[-1] in end_characters and msgstr[-1] not in end_characters:
            msgstr += msgid[-1]
        elif msgid[-1] not in end_characters and msgstr[-1] in end_characters:
            msgstr = msgstr[:-1]

        # Check rule 3
        chardiff = abs(len(msgid) - len(msgstr))
        if chardiff / len(msgid) > 0.2:
          print(f'Warning: msgid and msgstr have significantly different lengths at entry {entry["id"]}, delta={chardiff}')

        entry['msgid'][i] = msgid
        entry['msgstr'][i] = msgstr


if __name__ == '__main__':
    # Load a file and validate its entries
    entries = load_file('files_test/translated-test.po')
    for entry in entries:
        validate_entry(entry)

    input("Press Enter to continue...")

    for entry in entries:
      if entry['id'] == 0: continue
      print(f"ENTRY ID: {entry['id']}")
      for i, value in enumerate(entry['msgid']):
          if value == "": 
              continue
          print(f"TEXTO ORIGINAL:\n{value}")
          print(f"TEXTO TRADUCIDO:\n{entry['msgstr'][i]}\n")
