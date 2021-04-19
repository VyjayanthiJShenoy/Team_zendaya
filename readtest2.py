import urllib.request
import request
import threading
import json

import random

URL='https://api.thingspeak.com/channels/526585/fields/1.json?results=2'
KEY='R2K30QMFC3S53SWE'
HEADER='&results=2'
NEW_URL=URL+KEY+HEADER
print(NEW_URL)

get_data=request.get(NEW_URL).json()
    #print(get_data)
channel_id=get_data['channel']['id']

feild_1=get_data['feeds']
    #print(feild_1)

t=[]
for x in feild_1:
        #print(x['field1'])
    t.append(x['field1'])