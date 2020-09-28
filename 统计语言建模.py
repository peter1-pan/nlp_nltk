from nltk.util import ngrams
from nltk.corpus import alpino

print(alpino.words())
unigrams=ngrams(alpino.words(),4) #四元语法
print(unigrams)
# for i in unigrams:
#     print(i)

from nltk.collocations import BigramCollocationFinder
from nltk.corpus import webtext
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
stops_filter = lambda w: len(w) < 3 or w in stop_words # 单词长度小于3或是停用词
tokens=[t.lower() for t in webtext.words('grail.txt')]
words=BigramCollocationFinder.from_words(tokens) # 创建实例
print(words)
words.apply_word_filter(stops_filter)
res = words.nbest(BigramAssocMeasures.likelihood_ratio,5) # 二元语法，前5个
print(res)

# 使用词汇搭配查找器生成bigrams
import nltk
text1="Hardwork is the key to success. Never give up!"
word = nltk.wordpunct_tokenize(text1)
finder = BigramCollocationFinder.from_words(word)
bigram_measures = BigramAssocMeasures()
value = finder.score_ngrams(bigram_measures.raw_freq)
print(sorted(bigram for bigram,score in value))