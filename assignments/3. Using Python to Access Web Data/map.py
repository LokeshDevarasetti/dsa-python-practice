from ast import Param
import urllib.request, urllib.parse
import json, ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter the address: ")
    if len(address) < 3: break
    address = address.strip()

    params = dict()
    params['q'] = address
    url = serviceurl + urllib.parse.urlencode(params)
    data = urllib.request.urlopen(url).read().decode()

    try:
        js = json.loads(data)
        # print(json.dumps(js, indent=4))
    except:
        js = None
    
    if not js or 'features' not in js:
        print('===Download error===')
        print(data)
        break
    if len(js['features']) == 0:
        print("===ERROR===")
        print(data)
        break
    plus_code = js['features'][0]['properties']['plus_code']
    print("plus_code:", plus_code)
