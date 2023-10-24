from translate import Translator

def translate_text(input_text):
    translator = Translator(to_lang="ru")
    translation = translator.translate(input_text)
    return translation

if __name__ == "__main__":
    input_text = input("Введите текст на английском: ")
    translated_text = translate_text(input_text)
    print(f"Перевод на русский: {translated_text}")
