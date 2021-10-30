import urllib.request
import random
import string
import itertools 
import rlcompleter
import re
import operator

url = 'https://www.gutenberg.org/cache/epub/66627/pg66627.txt'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
nltk_text = data.decode('utf-8')

strippables = r"(?:s|'s|!+|,|\.|;|:|\(|\)|\"|\?+)?\s"
text = re.sub(strippables, ' ',text)
text = text.lower()

def count_words(book):
    word_count = {}
    for i in book.split():
        word_count[i] = word_count.get(i,0)+1
    return word_count


def ranked_words(dic):
    sorted_values = sorted(dic.values(),reverse=True) # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in dic.keys():
            if dic[k] == i:
                sorted_dict[k] = dic[k]

    return(sorted_dict)


def top_x_words(dic,x):
    sorted_values = sorted(dic.values(),reverse=True) # Sort the values
    sorted_dict = {}
    sorted_top = []
    for i in range(10):
        sorted_top.append(sorted_values[i])

    for i in sorted_top:
        for k in dic.keys():
            if dic[k] == i:
                sorted_dict[k] = dic[k]

    return(sorted_dict)

def compare_top_x(dict_1,dict_2,x):
    d1 = top_x_words(dict_1,x)
    d2 = top_x_words(dict_2,x)
    l = []
    for key in d1:
        if key not in d2.keys():
            l.append(key)
    for key in d2:
        if key not in d1.keys():
            l.append(key)
    no_dup_list = []
    for i in l:
        if i not in no_dup_list:
            no_dup_list.append(i)
    return no_dup_list


import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = nltk_text
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)
