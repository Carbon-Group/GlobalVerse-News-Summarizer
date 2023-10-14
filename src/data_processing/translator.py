import deepl

class DeepLTranslator:
    def __init__(self, auth_key):
        self.translator = deepl.Translator(auth_key)

    def translate_text(self, text, target_language):
        result = self.translator.translate_text(text, target_lang=target_language)
        return result.text

if __name__ == "__main__":
    auth_key = "YOUR_AUTH_KEY"
    target_language = "RU"
    text_to_translate = "Hello, world!"

    translator = DeepLTranslator(auth_key)
    translated_text = translator.translate_text(text_to_translate, target_language)
    print(translated_text)
