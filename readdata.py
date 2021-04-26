import urllib.request
import re
import json

datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/526585/feeds.json?results=1")
json_data =json.loads(datafromwebsite.read())
print(json_data)

#print(json_data["feeds"][0]["field1"])