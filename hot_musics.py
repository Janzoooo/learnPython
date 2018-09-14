from selenium import webdriver
import csv
import time


#设置handless浏览器
option = webdriver.ChromeOptions()
option.add_argument("headless")
option.add_argument("utf-8")
driver = webdriver.Chrome("C:\Python27\Scripts\chromedriver.exe",chrome_options=option)

#打开网易云首页
print('打开网易云排行榜')
driver.get("https://music.163.com/discover/toplist")
driver.switch_to.frame("g_iframe")
#time.sleep(10)

#开搞
table_tbody_tr = driver.find_elements_by_css_selector('table.m-table.m-table-rank>tbody>tr')

#写csv
print('创建csv')

csvfile = open("hot_music.csv","w",newline="",encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow(['标题','歌曲链接','时长','歌手','歌手链接'])

num = 1
print('导入中')
for music in table_tbody_tr:

    music_title = music.find_element_by_css_selector("span.txt>a>b").get_attribute("title")
    music_url = "https://music.163.com" + music.find_element_by_css_selector("span.txt>a").get_attribute("href")
    music_time = music.find_element_by_css_selector("span.u-dur").text
    music_artist = music.find_element_by_css_selector("div.text").get_attribute("title")
    artist_url = "https://music.163.com" + music.find_element_by_css_selector("div.text>span>a").get_attribute("href")

    writer.writerow([music_title,music_url,music_time,music_artist,artist_url])

    print('正在导入第：',num,'条')
    num = num + 1


#结束
csvfile.close()

driver.quit()



'''
import requests
from bs4 import BeautifulSoup

res = requests.get("https://music.163.com/discover/toplist")
res.encoding="utf-8"
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
'''