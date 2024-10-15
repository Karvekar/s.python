import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "POS tagging is an essential task in natural language processing."

tokens = word_tokenize(text)

pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)
              
import nltk
from nltk import RegexpParser
nltk.download('punkt')

text = "The quick brown fox jumps over the lazy dog."

tokens = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

grammar = r"""
    NP: {<DT>?<JJ>*<NN>}
    VP: {<VB.*><DT>?<JJ>*<NN>}
"""

parser = RegexpParser(grammar)

tree = parser.parse(pos_tags)

print(tree)
