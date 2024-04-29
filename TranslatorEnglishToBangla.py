from googletrans import Translator
def translate_to_bangla(input_file, output_file):

    translator = Translator()
    with open(input_file, 'r', encoding='utf-8') as f:
        english_text = f.read()
    translated = translator.translate(english_text, src='en', dest='bn')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated.text)
    print("Translation complete. Output written to", output_file)
input_file = "input.txt"
output_file = "output.txt"
translate_to_bangla(input_file, output_file)