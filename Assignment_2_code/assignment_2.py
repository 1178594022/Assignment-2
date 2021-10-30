from os import write
from mediawiki import MediaWiki
import urllib.request
import random
import string
import itertools
import re

import mediawiki 
wikipedia = MediaWiki()
MJ = wikipedia.page("Michael Jackson")
strippables = string.punctuation + string.whitespace
subed_MJ = re.sub(strippables,' ',MJ.content)
print(subed_MJ)

# data = babson.content
# with open('babson.txt', 'w') as f:
#     for line in data:
#         if line.startswith('='):
#             continue
#         else:
#             f.write(line)

# data1 = open(babson.txt)

# strippables = string.punctuation + string.whitespace

# for line in data1:
#     print(line)
# l = []

# for line in data:
#     if line.startswith('==='):
#         continue
#     else:
#         l.append(line)

# print (l)
