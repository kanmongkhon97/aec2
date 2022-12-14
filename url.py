import requests
URL = "http://m.jxyuging.com/shares/2022/1208/232019.html"
for x in range(10):
    response = requests.get(URL)
    open("232019.html", "wb").write(response.content)
    print("requests : %2d successfuly!" % (x))
