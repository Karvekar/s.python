from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')


text = "Tokenization is the first step in natural language processing."

tokens = word_tokenize(text)
print("Tokens:", tokens)
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

tokens = ["Tokenization", "is", "the", "first", "step", "in", "natural", "language", "processing"]

stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)
from nltk.stem import PorterStemmer

tokens = ["Tokenization", "is", "the", "first", "step", "in", "natural", "language", "processing"]

stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]
print("Stemmed Tokens:", stemmed_tokens)

from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

tokens = ["Tokenization", "is", "the", "first", "step", "in", "natural", "language", "processing"]

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
print("Lemmatized Tokens:", lemmatized_tokens)

import string

text = "This is a sample sentence with punctuation marks!"

clean_text = text.translate(str.maketrans("", "", string.punctuation))
print("Clean Text:", clean_text)

text = "This is a Sample Text."

lowercased_text = text.lower()
print("Lowercased Text:", lowercased_text)

from langdetect import detect

text = "Bonjour tout le monde"

language = detect(text)
print("Detected Language:", language)
