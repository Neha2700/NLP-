import nltk 
nltk.download('all')
from nltk.tokenize import sent_tokenize ,word_tokenize
text="Hello everyone. Welcome to NLP lab. You are doing NLP practical"
print(sent_tokenize(text))
print(word_tokenize(text))

