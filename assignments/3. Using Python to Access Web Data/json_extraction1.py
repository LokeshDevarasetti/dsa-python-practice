
import json
import urllib
import urllib.parse
import urllib.request


host = input("enter the url: ")
if len(host) < 1:
    host = "http://py4e-data.dr-chuck.net/comments_2252571.json"
# param = dict()
# location = input("enter the search location:")
# location = location.strip()
# param['q'] = location
# finalurl = host + urllib.parse.urlencode(param)

# data = urllib.request.urlopen(finalurl).read().decode()
data = urllib.request.urlopen(host).read().decode()

try:
    js = json.loads(data)
    # print(js)
except:
    js = None

# if not js or 'features' not in js:
#     print("====Download error===")
#     print(data)
# if len(js['features'])==0:
#     print("===error===")
#     print(data)

sum = 0
for comment in js["comments"]:
    sum = sum + int(comment['count']) 

print(sum)
