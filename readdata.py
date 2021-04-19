import urllib.request
import re

datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/526585/fields/1.json?results=1")
print(datafromwebsite.read())