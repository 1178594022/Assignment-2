import urllib.request
import random
import string
import itertools 

url = 'https://www.gutenberg.org/cache/epub/66627/pg66627.txt'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

def process_file(text, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    text

    if skip_header:
        skip_gutenberg_header(text)

    strippables = string.punctuation + string.whitespace

    for line in text:
        if line.startswith('THE END'):
            break

        line = line.replace('-', ' ')

        for word in line:
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK THE CAT\'S PAW ***'):
            break

print(process_file(text, skip_header = True ))