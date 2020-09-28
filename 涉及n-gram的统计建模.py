import nltk 
from nltk.tag import UnigramTagger
from nltk.corpus import treebank

training = treebank.tagged_sents()[:7000] # 使用treebank语料库前7000个句子训练
print('第一个句子: ',treebank.sents()[0])
unitagger = UnigramTagger(training)
print('第一个句子的词性标记: ',unitagger.tag(treebank.sents()[0]))

# 评估UnigramTagger的准确性
testing = treebank.tagged_sents()[2000:]
print('准确率: ',unitagger.evaluate(testing))