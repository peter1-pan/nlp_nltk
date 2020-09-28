import nltk
from nltk.stem import WordNetLemmatizer

# 词性还原，在WordNet中找不到输入的单词，则保持不变，pos:词性
lemmatizer_output=WordNetLemmatizer() 
print(lemmatizer_output.lemmatize('working'))
print(lemmatizer_output.lemmatize('working',pos='v'))
print(lemmatizer_output.lemmatize('works'))

# 词干提取和词性还原的区别
from nltk.stem import PorterStemmer
stemmer_output = PorterStemmer()
print('词干提取: ',stemmer_output.stem('happiness'))
print('词性还原: ',lemmatizer_output.lemmatize('happiness'))

