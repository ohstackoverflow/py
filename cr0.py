# coding:utf-8

import requests

myheaders = {
    "Cookie":"CViewProductHistory=34408%3b%c8%cb%b9%a4%d6%c7%c4%dc%3a%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf(%d4%ad%ca%e9%b5%da2%b0%e6)%7c8074663%3b%bb%e1%bb%b0%ca%bdAI%a3%ba%d7%d4%c8%bb%d3%ef%d1%d4%b4%a6%c0%ed%d3%eb%c8%cb%bb%fa%bd%bb%bb%a5; __utma=268923182.1021025815.1665834022.1665834022.1666271502.2; __utmz=268923182.1666271502.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_c68f8a95996223c018465c5143d0bdea=1665834022,1666271502; ordercount=0; cartbooknum=0; hurl=; __utmb=268923182.15.10.1666271502; __utmc=268923182; Hm_lpvt_c68f8a95996223c018465c5143d0bdea=1666273561; ASP.NET_SessionId=1ngun3vnl13sg145y2fjv555; selecthistory=%c8%cb%b9%a4%d6%c7%c4%dc+%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf; logvistsid=umg00b45kqexi5jj30deok45",
    "User":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Host":"search.china-pub.com",
    "Upgrade-Insecure-Requests":"1",
    "Referer":"http://search.china-pub.com/s/?key1=%c8%cb%b9%a4%d6%c7%c4%dc+%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf&type=&pz=1"}


r = requests.get("http://search.china-pub.com/s/?key1=%c8%cb%b9%a4%d6%c7%c4%dc+%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf&type=&pz=1", headers=myheaders)
html = r.text




from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')

url2 = soup.select_one('span[class="orange"]').find_parent().get('href')
myheaders2 = {
    "Cookie":"CViewProductHistory=34408%3b%c8%cb%b9%a4%d6%c7%c4%dc%3a%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf(%d4%ad%ca%e9%b5%da2%b0%e6)%7c8074663%3b%bb%e1%bb%b0%ca%bdAI%a3%ba%d7%d4%c8%bb%d3%ef%d1%d4%b4%a6%c0%ed%d3%eb%c8%cb%bb%fa%bd%bb%bb%a5; __utma=268923182.1021025815.1665834022.1665834022.1666271502.2; __utmz=268923182.1666271502.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_c68f8a95996223c018465c5143d0bdea=1665834022,1666271502; ordercount=0; cartbooknum=0; hurl=; __utmb=268923182.15.10.1666271502; __utmc=268923182; Hm_lpvt_c68f8a95996223c018465c5143d0bdea=1666273561; ASP.NET_SessionId=1ngun3vnl13sg145y2fjv555; selecthistory=%c8%cb%b9%a4%d6%c7%c4%dc+%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf; logvistsid=umg00b45kqexi5jj30deok45",
    "User":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Host":"product.china-pub.com",
    "Upgrade-Insecure-Requests":"1",
    "Referer":"http://search.china-pub.com/"}
r2 = requests.get(url2, headers=myheaders2)
r2.encoding = 'gb2312'
soup2 = BeautifulSoup(r2.text,'html.parser')

print(r2.text)

tar = soup2.select_one('h3[id="ml"]').find_next_sibling()
print(tar)

