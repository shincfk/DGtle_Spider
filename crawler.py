#!/usr/bin/python
import re
import urllib

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getImg(html):
    reg=r'file="(.*?\.png)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' %x)
        x+=1
        
html=getHtml("http://bbs.dgtle.com/thread-256234-1-1.html")
print getImg(html)        
