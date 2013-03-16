import urllib
import urllib.request
import xml.etree.ElementTree as ET


app_id='APLTT9-9WG78GYE65'
print('App ID: ',app_id)
query=input('Enter Query: ')
url_query=query.replace(' ','+')
url=('http://api.wolframalpha.com/v2/query?input={}&appid={}'.format(url_query,app_id))

xml_data=urllib.request.urlopen(url).read()
root = ET.fromstring(xml_data)

for pt in root.findall('.//plaintext'):
    if pt.text:
        print(pt.text)
