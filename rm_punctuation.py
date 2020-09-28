from nltk import word_tokenize
import re
import string

with open('test.txt','rt',encoding='utf-8') as f:
    text = [line.strip() for line in f]
print(text)
# 切分文本
tokenized_docs = [word_tokenize(doc) for doc in text]
# print(tokenized_docs)
# x=re.compile('[%s]' % re.escape(string.punctuation))

print(string.punctuation)
res = []
for i in tokenized_docs:
    line = []
    for j in i:
        if j not in string.punctuation:
            line.append(j)
    res.append(line)
print(res)