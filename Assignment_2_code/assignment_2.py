from mediawiki import MediaWiki
import urllib.request
import random
import string
import itertools 
wikipedia = MediaWiki()
babson = wikipedia.page("Babson College")
print(babson.title)
# print(babson.content)

data = wikipedia.page("Babson College")

for line in data:
    if line.startwith('==='):
        continue
    else:
        data.line = line
