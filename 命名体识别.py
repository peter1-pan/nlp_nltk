import nltk
from nltk import pos_tag,word_tokenize

print(pos_tag(word_tokenize("John and Smith are going to NY and Germany")))  # NNP标记的是命名实体

