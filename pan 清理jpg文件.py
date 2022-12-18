import requests
import json
import time

url = "http://pan.baidu.com/rest/2.0/xpan/multimedia?method=listall&path=/000各种文档资料/万门大学-零基础学德语/&access_token=126.b136a1726ea175304c174c873ead18f6.YDA-tQDMq9lj-iCfJe7YlxhH_qx0oDzjeAkRl8e.DpTDYg&web=1&recursion=1&start=0&limit=1000"

payload = {}
files = {}
headers = {
  'User-Agent': 'pan.baidu.com'
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

list = response.json().get("list")
for i in list:

    if i.get("server_filename").count('jpg') != 0:

                file_jpg = i.get("path")
                print(file_jpg)
                url2 = "http://pan.baidu.com/rest/2.0/xpan/file?method=filemanager&access_token=126.b136a1726ea175304c174c873ead18f6.YDA-tQDMq9lj-iCfJe7YlxhH_qx0oDzjeAkRl8e.DpTDYg&opera=delete"
                payload2 = {'async': '0',
                    'filelist': '[{"path":"' + file_jpg + '"}]'}
                response2 = requests.request("POST", url2, data = payload2)
                print(response2.json())
