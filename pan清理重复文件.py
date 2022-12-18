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

    if i.get("isdir") ==  0:
        url1 = "http://pan.baidu.com/rest/2.0/xpan/file?method=filemanager&access_token=126.b136a1726ea175304c174c873ead18f6.YDA-tQDMq9lj-iCfJe7YlxhH_qx0oDzjeAkRl8e.DpTDYg&opera=rename"


        path_org = i.get("path")
        name_org = i.get("server_filename")
        name_renamed = name_org.replace("【不要添加任何微信，公众号：97学社-免费分享】关注即可获取更多免费学习资源","")

        if name_org != name_renamed:            

            payload1 = {'async': '0',
            'filelist': '[{"path":"' + path_org + '","newname":"' + name_renamed + '","ondup":"overwrite"}]'}

            response1 = requests.request("POST", url1, data = payload1)


            if response1.json().get("info")[0].get("errno") == -8:
                file_dup = response1.json().get("info")[0].get("path")
                print(file_dup)
                url2 = "http://pan.baidu.com/rest/2.0/xpan/file?method=filemanager&access_token=126.b136a1726ea175304c174c873ead18f6.YDA-tQDMq9lj-iCfJe7YlxhH_qx0oDzjeAkRl8e.DpTDYg&opera=delete"
                payload2 = {'async': '0',
                    'filelist': '[{"path":"' + file_dup + '"}]'}
                response2 = requests.request("POST", url2, data = payload2)
                print(response2.json())
