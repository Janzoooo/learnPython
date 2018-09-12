# coding:utf-8
'''
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

'''


'''
#example
from bs4 import BeautifulSoup
html_sample= ' \
<html> \
    <body> \
    <h1 id="title">Hello Word</h1> \
    <a href="#" class="link">This is link1</a> \
    <a href="# link2" class="link">This is link2</a> \
    </body> \
    </html>'
soup = BeautifulSoup(html_sample, 'html.parser')
print(type(soup))
print(soup.text)

print('---------')

header = soup.select('h1')
print(header[0])
print(header[0].text)

print('----------')

alink = soup.select('#title')
print(alink[0])

print('----------')

for link in soup.select('.link'):
    print(type(link))
    print(link['href'])

print('----------')

'''
import csv
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
news = soup.select('.right-content')[0]

#创建csv文件准备导入
csvfile = open('news.csv', 'w',newline='')
try:
    writer = csv.writer(csvfile)
    writer.writerow(['时间','标题','网址'])


    for a_link in news.select('a'):
        new_title = a_link.text
        new_url = a_link['href']
        res_click = requests.get(new_url)
        res_click.encoding = 'utf-8'
        soup_click = BeautifulSoup(res_click.text, 'html.parser')
        date = soup_click.select('.date')[0].text
        #print(date, new_title, new_url)
        writer.writerow([date, new_title, new_url])

finally:
    csvfile.close()