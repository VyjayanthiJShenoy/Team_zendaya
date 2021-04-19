import random
import urllib.request
#import request
import threading

def thingspeak():
    threading.Timer(15,thingspeak).start()
    URL=" https://api.thingspeak.com/update?api_key=R8ZZPBUGW9HXIIA8"
    HEADER=" &field1={}&field2={}&field3={}".format(str(12),str(56),str(78))
    new_URL=URL+HEADER
    urllib.request.urlopen(new_URL)
    print(new_URL)
    data=urllib.request.urlopen(new_URL)
    print(data)

thingspeak()