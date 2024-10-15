import re
from bs4 import BeautifulSoup

html_text = "<p>This is <b>HTML</b> <a href='https://example.com'>text</a>.</p>"

def clean_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    cleaned_text = soup.get_text()
    return cleaned_text

cleaned_html_text = clean_html_tags(html_text)
print("Cleaned HTML Text:", cleaned_html_text)


import emoji
text_with_emojis = "I love 😊 Python! 🐍"

def normalize_emojis(text):
    cleaned_text = emoji.demojize(text)
    return cleaned_text

normalized_text = normalize_emojis(text_with_emojis)
print("Normalized Text:", normalized_text)


from textblob import TextBlob

text_with_errors = "vinayy is veryyy talennted."

def correct_spelling(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

corrected_text = correct_spelling(text_with_errors)
print("Corrected Text:", corrected_text)
from autocorrect import Speller

text_with_typing_errors = "I amm typingg fastt."

def correct_fast_typing(text):
    spell = Speller(lang="en")
    corrected_text = spell(text)
    return corrected_text

corrected_typing_text = correct_fast_typing(text_with_typing_errors)
print("Corrected Typing Text:", corrected_typing_text)
