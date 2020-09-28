import nltk
text1 = nltk.word_tokenize('It is a pleasant day today')
print(nltk.pos_tag(text1))

# 使用词典创建元祖（单词: 词性标记）
tag = {}
tag['beautiful'] = 'ADJ'
print(tag)
tag['boy'] = 'N'
tag['read'] = 'v'
tag['generously'] = 'ADV'
print(tag)