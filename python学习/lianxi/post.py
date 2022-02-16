import requests
import json
import jsonpath

url = "http://localhost:8000/login"

data = {
    "username": "admin",
    "password": "admin"
}

r = requests.post(url=url,json=data)
print(json.dumps(r.json(),indent=4,ensure_ascii=False))

print(jsonpath.jsonpath(r.json(), "$..token")[0])


print("*************************************************************")

urllogin = "http://localhost:8000/auth/hello"

token = "Bearer "+jsonpath.jsonpath(r.json(),"$..token")[0]

headers ={
    "Authorization":token
}

r1 = requests.get(url=urllogin,headers=headers)
print(json.dumps(r1.json(),indent=4,ensure_ascii=False))

print('************************************************************')

url ="http://httpbin.org/post"


file =open("C:\\Users\\EDZ\\Desktop\\1111.txt","rb")

files = {
    "file": file
}
res2 = requests.post(url=url, files=files)
#print(res.json())
print(json.dumps(res2.json(), indent=4, ensure_ascii=False))