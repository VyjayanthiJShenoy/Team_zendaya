import urllib.request
#import 
#from bs4 import BeautifulSoup

data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=R8ZZPBUGW9HXIIA8&field1={}&field2={}&field3={}".format("10","20","30"))
print(data)