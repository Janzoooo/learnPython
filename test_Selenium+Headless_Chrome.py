import csv
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("headless")
option.add_argument('UTF-8')
driver = webdriver.Chrome("C:\Python27\Scripts\chromedriver.exe", chrome_options=option)
driver_in = webdriver.Chrome("C:\Python27\Scripts\chromedriver.exe", chrome_options=option)
print('打开新浪新闻首页')
driver.get("https://news.sina.com.cn/china/")
news_list = driver.find_elements_by_css_selector('div#feedCardContent>div>div.feed-card-item')
print('创建csv文件准备导入')
csvfile = open('hotnews.csv', 'w', newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['时间','标题','网址','评论数'])
print('查询写入中...')
num = 1
for news in news_list:
    news_title = news.find_elements_by_css_selector('h2>a')[0].text
    news_url = news.find_elements_by_css_selector('h2>a')[0].get_attribute('href')
    news_date = news.find_element_by_class_name('feed-card-time').text
    driver_in.get(news_url)
    #print(news_url)
    #print(driver.find_elements_by_css_selector('div.page-tools>span.tool-cmt>a>span.num')[0].text == '')
    news_comments_num = '0' if driver_in.\
                                   find_elements_by_css_selector('div.page-tools>span.tool-cmt>a>span.num')\
                                   [0].text == '' else\
            driver_in.find_elements_by_css_selector('div.page-tools>span.tool-cmt>a>span.num')[0].text

    csvwriter.writerow([news_date, news_title, news_url, news_comments_num])

    print(num)
    num = num + 1

print('关闭csv文件')
csvfile.close()
print('关闭浏览器')
driver.quit()
driver_in.quit()