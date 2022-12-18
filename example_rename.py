import requests

url = "http://pan.baidu.com/rest/2.0/xpan/file?method=filemanager&access_token=126.b136a1726ea175304c174c873ead18f6.YDA-tQDMq9lj-iCfJe7YlxhH_qx0oDzjeAkRl8e.DpTDYg&opera=rename"


path_org = "/000各种文档资料/万门大学-零基础学德语/四/询问，留学德语零基础特训_万门-大学_10【不要添加任何微信，公众号：97学社-免费分享】关注即可获取更多免费学习资源(1).ts"
name_org = "询问，留学德语零基础特训_万门-大学_10【不要添加任何微信，公众号：97学社-免费分享】关注即可获取更多免费学习资源(1).ts"
name_renamed = name_org.replace("【不要添加任何微信，公众号：97学社-免费分享】关注即可获取更多免费学习资源","").replace("(1)","")

payload = {'async': '0',
'filelist': '[{"path":"' + path_org + '","newname":"' + name_renamed + '","ondup":"overwrite"}]'}

response = requests.request("POST", url, data = payload)

print(response.text.encode('utf8'))
