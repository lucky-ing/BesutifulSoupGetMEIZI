# -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request,response
import requests
import gzip,zlib
from io import StringIO
import urllib
import re

header1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
           'accept-encoding':'','accept-language':'zh-CN,zh;q=0.8','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'cookie':'thw=cn; UM_distinctid=15ad75e8f3564-0e6b742498981b-5d4e211f-1fa400-15ad75e8f362bf; t=02cfb3cd4b73b9ad6b127e8a75db87de; l=AllZctE-43-0B4Mb-EGcFots6U87Zk2X; mt=ci%3D-1_0; cna=Jd9HEZ1izWkCAdoE3a42MKsA; JSESSIONID=43806F6A1954DFEF8CBAA2D24A4ECE96; isg=As_PEjLJyu-gx89wR8eKzbIfXmPTcHIyXw809eHcZz5SsO-y6cSzZs0ixtf0'}#'Host':'www.mmjpg.com','Referer':'http://www.mmjpg.com/images/style.css'
html='https://s.taobao.com/search?q=%E6%8B%96%E9%9E%8B&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170527&bcoffset=1&ntoffset=1&p4ppushleft=1%2C48&s=0'
payload = {'q': 'python','s': '1','ie':'utf8'}
def get_pic(htmld,c):
    requ=request.Request(url=htmld,headers=header1)
    req = request.urlopen(requ)
    #req = requests.get(url=htmld, params=payload)
    #print(req.encoding)
    print(req.headers.get('Content-Encoding'))
    #print(req.content.decode('gb2312'))
    #qq=gzip.GzipFile(fileobj=StringIO(req.read().decode()), mode='r')
    print(req.read().decode())
    htm=zlib.decompress(req.read(),16+zlib.MAX_WBITS)
    print(htm.decode())
    bs=BeautifulSoup(qq,'lxml')
    error=len(bs.find_all(text='下一页'))
    for i in bs.find_all('div',class_='pic'):
        for j in i.find_all('img'):
            c=c+1
            print(j['src'])
            request.urlretrieve(j['src'],r'taobao/'+str(c)+'.jpg')
    return (c,error)
if __name__=="__main__":
    c=0
    error=1
    num=1
    get_pic(html,0)
    '''
    while error!=0:
        num=num+1
        html_temp=html+str(num)
        (c,error)=get_pic(html_temp,c)
    '''
#bs = BeautifulSoup(html,'html.parser')
#for i in bs.find_all('class'):
 #   print(i)

