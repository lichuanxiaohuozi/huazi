import requests
import json
url = "http://127.0.0.1:8080//EasyBuy/Login"
data = "loginName=admin&password=123456&action=login"
#
# req =requests.request("POST",url=url,params=data)
req = requests.post(url=url,params=data)

# print(json.dumps(req.json(),indent=4, ensure_ascii=False))
print(req.text)