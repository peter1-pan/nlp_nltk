import nltk
import sys
try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print('Error has occured')

def calculate_languages_ratios(text):
    languages_ratios = {}
    tok = wordpunct_tokenize(text)
    words = [word.lower() for word in tok]
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        languages_ratios[language] = len(common_elements)
        return languages_ratios

def detect_language(text):
    ratios = calculate_languages_ratios(text)
    most_rated_language = max(ratios,key=ratios.get)
    return most_rated_language

if __name__ == "__main__":
    text = "i love you." 
    language = detect_language(text)
    print(language) # 有bug，结果都是arabic