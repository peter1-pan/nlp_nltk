import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer('\w+')
res = tokenizer.tokenize("Don't hesitate to ask questions!")
print(res)

tokenizer2=RegexpTokenizer('\s+',gaps=True)
res2 = tokenizer.tokenize("Don't hesitate, to ask questions !")
print(res2)

print(nltk.word_tokenize("Don't hesitate, to ask questions!"))