import requests
URL = "http://m.jxyuging.com/shares/2022/1208/232019.html"
response = requests.get(URL)
i = 0
for x in range(6):
    i + 1
    print("requests : %2d" % (i))
    open("232019.html", "wb").write(response.content)
