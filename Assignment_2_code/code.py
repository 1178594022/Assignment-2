import urllib.request

url = 'https://www.gutenberg.org/cache/epub/66627/pg66627.txt'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
print(text)