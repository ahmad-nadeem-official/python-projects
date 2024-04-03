from googletrans import Translator
from googletrans.constants import LANGUAGES

text = input("Enter your text: ")

try:
    translator = Translator()
    dt = translator.detect(text)
    tr = translator.translate(text)
    print(f"Detected language: {LANGUAGES[dt.lang]}")
    print(f"Translated text: {tr.text}")
except Exception as e:
    print("An error occurred:", e)

