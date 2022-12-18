import requests
import json
import time

url = "http://pan.baidu.com/rest/2.0/xpan/multimedia?method=listall&path=/000各种文档资料/高考/&access_token=126.b136a1726ea175304c174c873ead18f6.YDA-tQDMq9lj-iCfJe7YlxhH_qx0oDzjeAkRl8e.DpTDYg&web=1&recursion=1&start=0&limit=1000"

payload = {}
files = {}
headers = {
  'User-Agent': 'pan.baidu.com'
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

list = response.json().get("list")
for i in list:
    print(i.get("fs_id"))


    url2 = "http://pan.baidu.com/rest/2.0/xpan/multimedia?method=filemetas&access_token=126.b136a1726ea175304c174c873ead18f6.YDA-tQDMq9lj-iCfJe7YlxhH_qx0oDzjeAkRl8e.DpTDYg&fsids=[39520534558307]&thumb=1&dlink=1&extra=1"
    response2 = requests.request("GET", url2, headers=headers, data = payload, files = files)
    print(response2.json().get("list"))
