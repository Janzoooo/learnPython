# coding:utf-8
import urllib.request
import re

def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')  # python3
    return html

reg = r'src="(.+?\.jpg)" width'#正则表达式
reg_img = re.compile(reg)#编译一下，运行更快
imglist = reg_img.findall(get_html('http://tieba.baidu.com/p/1753935195'))#进行匹配
x =0
for img in imglist:
    urllib.request.urlretrieve(img,'%s.jpg' %x)
    x += 1
