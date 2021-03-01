import requests
import json
import time
d={}
d2={}
def jjs():
    url="https://blockchain.info/ru/ticker"
    return requests.get(url).text

d=jjs()
print(d)
a=input("Введите обозначение волюты: ")
d = json.loads(jjs())
d2=d[a]
print("Стоимость покупки биткоина в волюте",a,"равна:",d2["buy"])
