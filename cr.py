# coding:utf-8



def getBookSaveToDb(book_org_name):

  import requests

  #book_org_name = "《图解数据结构-使用Java》"

  book_name = book_org_name.replace('中文版','').replace('完整版','').replace('高清版','').replace('扫描版','').replace('高清','').replace('扫描','').replace('完整','').replace('中文','').replace('书签版','')

  left_kh = book_name.find('(')
  right_kh = book_name.find(')')
  if left_kh != -1 and right_kh != -1:
    book_name = book_name.replace(book_name[left_kh:right_kh+1],'')

  left_kh1 = book_name.find('（')
  right_kh1 = book_name.find('）')
  if left_kh1 != -1 and right_kh1 != -1:
    book_name = book_name.replace(book_name[left_kh1:right_kh1+1],'')
    
  print(book_name)


  myheaders = {
      "Cookie":"CViewProductHistory=34408%3b%c8%cb%b9%a4%d6%c7%c4%dc%3a%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf(%d4%ad%ca%e9%b5%da2%b0%e6)%7c8074663%3b%bb%e1%bb%b0%ca%bdAI%a3%ba%d7%d4%c8%bb%d3%ef%d1%d4%b4%a6%c0%ed%d3%eb%c8%cb%bb%fa%bd%bb%bb%a5; __utma=268923182.1021025815.1665834022.1665834022.1666271502.2; __utmz=268923182.1666271502.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_c68f8a95996223c018465c5143d0bdea=1665834022,1666271502; ordercount=0; cartbooknum=0; hurl=; __utmb=268923182.15.10.1666271502; __utmc=268923182; Hm_lpvt_c68f8a95996223c018465c5143d0bdea=1666273561; ASP.NET_SessionId=1ngun3vnl13sg145y2fjv555; selecthistory=%c8%cb%b9%a4%d6%c7%c4%dc+%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf; logvistsid=umg00b45kqexi5jj30deok45",
      "User":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
      "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
      "Host":"search.china-pub.com",
      "Upgrade-Insecure-Requests":"1",
      "Referer":"http://search.china-pub.com/s/?key1=%c8%cb%b9%a4%d6%c7%c4%dc+%d6%c7%c4%dc%cf%b5%cd%b3%d6%b8%c4%cf&type=&pz=1"}

  url = "https://search.jd.com/Search?keyword=" + book_name + "&enc=utf-8&pvid=f1d8a3962dca40089230d229e7d909e7"
  r = requests.get(url)



  from bs4 import BeautifulSoup
  soup = BeautifulSoup(r.text,'html.parser')


  elem_name = soup.select_one('font[class="skcolor_ljg"]').find_parent()
  print(elem_name.text) #这里的书名更规范。可能，修复去掉了<< >> 【】 这样的不需要的符号.

  url2 = elem_name.find_parent().get('href')
  print(url2)

  myheaders2 = {
      "Cookie":("__jda=122270672.166590261493392472227.1665902614.1666262239.1666429607.6; unpl=JF8EAKhnNSttWE1XUUkKExERGwpXWwkKGUdXbTMFAF1dTQEDHVZPGhB7XlVdXhRLFh9sZBRUXFNLUg4bBisSEXtfVVdcDkgWA25XNVNdUQYVV1YyGBIgS1xkXloPTx8CbGAFUVVaSVwGHgQYERNNbVVuWghCJzNfYgVVXFxIUgMYCisTIElcVVtVCkMUCm5XTjpcFUtTAh8KGhEXS1hcXF8ASBIFbGQGUm1Ze1c; __jdv=76161171|direct|-|none|-|1666002612231; __jdu=166590261493392472227; areaId=2; ipLoc-djd=2-2817-51973-0; shshshfp=2fcf430ed73055eb524e1bd4e0a6fbe7; shshshfpa=4edbb9d4-2df2-d2ab-e5bd-503fbb37774e…c=122270672; shshshsID=d666195c66bb298a5cc1238843523b97_4_1666430059495; joyya=1666429631.1666429743.18.00gweaf; joyytokem=babel_3sAaxodHF7kfo3s95cjxo2UZUxu2MDFKWVdlaDk5MQ==.e29hU1x4YGFWWnhgbhsFfCoVEQ0ybWcKFnt1YUlZZmgpVxZ7JzYiBQ4OEzASBHRkLSoaODgNURlrAxMPNCc=.93d5021f; jsavif=1; token=b2839ed286bca6192a8d95604a1aff18,2,925794; __tk=de4f8837b795cce27878274f4161b1b0,2,925794; jsavif=1; ip_cityCode=2817; 3AB9D23F7A4B3C9B=ATX43LNB4ILHZ4QXOIIV25WREBXDMFFRLQ4JTMCPQKRHW675JNVX4TYOWM4AEWEAMSAVQATHM35Q6T27A4TOVN5TMA").encode("utf-8").decode("latin1"),
      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
      "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
      "Host":"item.jd.com",
      "Upgrade-Insecure-Requests":"1",
      "Referer":"https://search.jd.com/"}

  from selenium import webdriver
  driver = webdriver.Firefox()

  driver.get("https:"+url2)



  #r2 = requests.get("https:"+url2, headers=myheaders2)

  #soup2 = BeautifulSoup(r2.text,'html.parser')

  soup2 = BeautifulSoup(driver.page_source,'html.parser')

  driver.close()
  driver.quit()


  print("封面图:")
  img_cover = soup2.select_one('img[id="spec-img"]').get('data-origin')
  if img_cover is None:
    print("img_cover None")
  else:
    print(img_cover)

  print("描述图:")
  desc = soup2.select_one('div[id="J-detail-content"]')
  img2 = None

  if desc is None or desc.select_one('img') is None:
    print("img_desc None")
  else:
    img2 = desc.select_one('img').get('src')
    print(img2)
    if img2.find("blank.gif") != -1:
      img2 = None
      print("img2 None")



  [s.extract() for s in desc.find_all("img")]
  [s.extract() for s in desc.find_all('div',class_="more")]

  for d in desc.find_all('div',style="height: 314px; overflow: hidden;"):
    del(d['style'])

  print("描述:")
  print(desc)



  #开始插入数据到数据库

  import pymysql
  try:
    db = pymysql.connect(host='localhost',user='root',passwd='123456',port=3306,db='spec')
    print('连接成功')
  except:
    print('连接失败')

  cursor = db.cursor()

  sql = "insert into book(orginal_book_name,`name`,cover_img,desc_img,`desc`) values('%s','%s','%s','%s','%s')" %(book_org_name,elem_name.text, img_cover, img2, desc )
  print(sql)
  try:
    cursor.execute(sql)
    db.commit()
    print('插入成功')
  except Exception as e:
    db.rollback()
    print(e)

  db.close()




import os, sys
folder = "D:\downloads"
count = 0
for d in os.listdir(folder):
  #print(d)
  """
  org = d
  if d.find("_") != -1:
    d = d[d.find("_")+1:]

  if d.find("相关") != -1:
    d = d[:d.find("相关")]

  os.rename(folder+"\\"+org, folder+"\\"+d)
  print(d)

  for f in os.listdir(folder + "\\" + d):
    if f.find(".pdf") == -1:
      #print(f[:f.find(".pdf")])
      print(folder + "\\" + d + "\\" + f)

  """
  for f in os.listdir(folder + "\\" + d):
    count = count + 1
    print(f[:f.find(".pdf")])
print(count)


book_org_name = "《图解数据结构-使用Java》"
#getBookSaveToDb(book_org_name)







