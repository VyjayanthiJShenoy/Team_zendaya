import requests

token="1769774111:AAGtg8c6_p3XIZ_oZSC4rnsTaXZmj26Wwnc"
chat_id="629545180"

url_req ="https://api.telegram.org/bot"+ token+"/sendMessage"+"?chat_id="+chat_id +"&text=hello"

result=requests.get(url_req)
print(result.json())
