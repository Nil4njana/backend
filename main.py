from googletrans import Translator
translator = Translator()
tr_lang=input("Enter the language code: ")

translation1 = translator.translate(" こんにちは", dest=tr_lang)
print(translation1.text)
sentence=input("Enter your sentence: ")
preferred_lang=input("Enter your preferred language code: ")
detected_language = translator.detect(sentence).lang
language_name={
    "en":"english",
    "es":"spanish",
    "ru":"russian",
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'ar': 'Arabic',
    'zh': 'Chinese',

    'fr': 'French',
    'de': 'German',
    'ja': 'Japanese',
    'ko': 'Korean',


}

translation2 = translator.translate(sentence, dest=preferred_lang)
detected_language_name = language_name[preferred_lang]
print(f"The sentence in {detected_language_name} is : {translation2.text}")

sentence2=input("enter your sentence: ")

lang = translator.detect(sentence2).lang
print(f"This sentence is in {lang}")