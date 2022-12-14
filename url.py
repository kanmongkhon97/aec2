import requests
URL = "http://m.jxyuging.com/shares/2022/1208/232019.html"
response = requests.get(URL)
for x in range(6):
    open("232019.html", "wb").write(response.content)