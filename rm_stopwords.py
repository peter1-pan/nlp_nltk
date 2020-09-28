import nltk
from nltk.corpus import stopwords
stops = set(stopwords.words('english'))
words = ["Don't", 'to', 'ask']
res = [word for word in words if word not in stops]
print(res)