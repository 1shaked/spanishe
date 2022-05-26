from googletrans import Translator
tries = 0
max_try = 5
src = 'es'
dest = 'en'
dest_file_name = 'en.txt'
original_text_file_name = 'es_origin.txt'

translator = Translator()

source_file_name = 'es_source.txt'
with open(source_file_name, mode='r') as f:
    text = f.read()

lines_origin: list[str] = text.split('\n')
lines_dest: list[str] = text.split('\n')
index = 0
lines_number: int = len(lines_origin)
while index < lines_number and tries <= max_try:
    print(index)
    try:
        translation = translator.translate(lines_origin[index],src=src, dest=dest)
        lines_origin[index] = f'[{index}]: {lines_origin[index]}'
        lines_dest[index] = f'[{index}]: {translation.text}'
        tries = 0
        index += 1
    except Exception as e:
        tries += 1
        print(f'Exception {e}')
        print(f"will try rerun this max for {max_try} times. we tried {tries}")

dest_text: str = '\n'.join(lines_dest)
with open(dest_file_name, mode='w') as f:
    f.write(dest_text)

original_text: str = '\n'.join(lines_origin)
with open(original_text_file_name, mode='w') as f:
    f.write(original_text)