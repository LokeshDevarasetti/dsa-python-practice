import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 5 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2252570.xml'

print('Retrieving', url)
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    nums.append(int(result.text))
    # Debug print the data :)
    print(result.text)

print('Count:', len(nums))
print('Sum:', sum(nums))