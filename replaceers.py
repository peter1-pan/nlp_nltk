import re
from nltk import word_tokenize
from nltk.corpus import wordnet

replacement_patterns = [
    (r'won\'t', 'will not'),
    (r'can\'t', 'can not'),
    (r'i\'m', 'i am'),
    (r'am\'t', 'is not'),
    (r'(\w+)\'ll', '\g<1> will'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> is'),
    (r'(\w+)\'re', '\g<1> are'),
    (r'(\w+)\'d', '\g<1> would')
]

# 替换缩略词
class RegexReplacer:
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex),repl) for (regex,repl) in patterns]
    def replace(self,text):
        s = text
        for (pattern,repl) in self.patterns:
            (s, count) = re.subn(pattern,repl,s)
        return s

# replacer = RegexReplacer()
# res = replacer.replace("Don't hesitate to ask questions")
# print(res)
# print(word_tokenize(res))

# 替换重复字符
class RepeatReplacer:
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'
    def replace(self,word):
        if wordnet.synsets(word):
            return word
        repl_word = self.repeat_regexp.sub(self.repl,word)
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word

# replacer = RepeatReplacer()
# print(replacer.replace('happiness'))

# 用单词的同义词替换
class WordReplacer:
    def __init__(self,word_map):
        self.word_map = word_map
    def replace(self,word):
        return self.word_map.get(word,word)

# 在定义的word_map词典中寻找单词对应的同义词，若存在就替换，没有就返回单词本身
replacer = WordReplacer({'congrats':'congratulations'})
res = replacer.replace('congrats')
print(res)
res2 = replacer.replace('love')
print(res2)