import nltk
from nltk.stem import PorterStemmer

# porter词干提取算法
stemerporter = PorterStemmer()
print(stemerporter.stem('working'))
print(stemerporter.stem('happiness'))

# Lancaster词干提取算法，比porter涉及更多的情感词
from nltk.stem import LancasterStemmer
stemmerlan=LancasterStemmer()
print(stemmerlan.stem('working'))
print(stemmerlan.stem('happiness'))

# 设计自己的词干提取器
from nltk.stem import RegexpStemmer
stemmerregexp=RegexpStemmer('ing') # 去除ing
print(stemmerregexp.stem('working'))
print(stemmerregexp.stem('happiness'))
print(stemmerregexp.stem('inghappiness'))

# 除英文外的14种语言的词干提取
from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)
# arabic(阿拉伯语) danish(丹麦语) dutch(荷兰语) finnish(芬兰语) french(法语) german(德语)
# hungarian(匈牙利语) italian(意大利语) norwegian(挪威语) porter portuguese(葡萄牙语)
# romanian(罗马尼亚语) russian(俄语) spanish(西班牙语) swedish(瑞典语)
spanishstemmer=SnowballStemmer('spanish')
print(spanishstemmer.stem('comiendo'))
frenchstemmer=SnowballStemmer('french')
print(frenchstemmer.stem('manger'))

def oo():
    with open('test.txt') as f:
        tok = nltk.word_tokenize(f.read())
    return tok
print(oo())