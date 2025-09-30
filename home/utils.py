# home/utils.py
from googletrans import Translator  # pip install googletrans==4.0.0-rc1

translator = Translator()

def translate_to_english(text):
    # O'zbekchadan inglizchaga tarjima qiladi
    translated = translator.translate(text, src='uz', dest='en')
    return translated.text
