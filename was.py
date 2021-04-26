import requests
import urllib.request
import re
import json


token="1769774111:AAGtg8c6_p3XIZ_oZSC4rnsTaXZmj26Wwnc"
chat_id="562934559"

datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/526585/fields/1.json?results=1")
json_data =json.loads(datafromwebsite.read())

url_req ="https://api.telegram.org/bot"+ token+"/sendMessage"+"?chat_id="+chat_id +"&text=" + json_data["feeds"][0]["field1"]
result=requests.get(url_req)
print(result.json())
