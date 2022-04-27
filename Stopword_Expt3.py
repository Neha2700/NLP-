from nltk.tokenize import sent_tokenize ,word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
text="Hello everyone. Welcome to NLP lab. You are doing NLP practical"

example=word_tokenize(text)
stop_words=set(stopwords.words('english'))
ans=[]
for i in example:
  if i.lower() not in stop_words:
    ans.append(i)
print(ans)