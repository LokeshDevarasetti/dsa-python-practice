import urllib
import urllib.request

from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Eirinn.html'
name = ''
times = 7
pos = 18

for x in range(times):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    url = tags[pos-1].get('href',None)
    name = tags[pos-1].contents[0]
print(name)
