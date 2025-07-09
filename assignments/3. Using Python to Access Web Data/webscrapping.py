import urllib
import urllib.request

from bs4 import BeautifulSoup

html = (urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2252568.html')).read()

soup1 = BeautifulSoup(html,'html.parser')

spans = soup1('span')
sum = 0
count = 0
for tag in spans:
    # print('TAG:',tag)
    # print('URL:',tag.get('href', None))
    # print('Contents:',tag.contents[0])
    # print('Attrs:',tag.attrs)
    sum = sum + int(tag.contents[0])
    count = count + 1
print(sum, count)