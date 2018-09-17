from selenium import webdriver
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait


#因给input框赋值失败，本段代码存在BUG
#发现给输入框用send_keys方法赋值虽成功但无法产生作用


print("------当天车票余票查询------")

option = webdriver.ChromeOptions()
option.add_argument("headless")
option.add_argument("utf-8")

driver = webdriver.Chrome("C:\Python27\Scripts\chromedriver.exe",chrome_options=option)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
#time.sleep(20)
WebDriverWait(driver,20,1).until(lambda driver:driver.find_elements_by_css_selector("form#queryLeftForm"))
fromStationText = input("请输入出发地：")
toStationText = input("请输入目的地：")
form = driver.find_elements_by_tag_name("form")
queryform = driver.find_elements_by_css_selector("form#queryLeftForm")

driver.find_element_by_id("fromStationText").clear()
driver.find_element_by_id("fromStationText").send_keys(fromStationText)
#driver.find_element_by_id("fromStation").send_keys("CDW")
#driver.find_element_by_id("fromStationText").send_keys("成都")
#driver.execute_script("$(\"#fromStationText\").val(\"成都\")")
driver.find_element_by_id("toStationText").clear()
driver.find_element_by_id("toStationText").send_keys(toStationText)
#driver.find_element_by_id("toStation").send_keys("NJH")
#driver.find_element_by_id("toStationText").send_keys("南京")
#driver.execute_script("$(\"#toStationText\").val(\"南京\")")

print(driver.find_element_by_id("query_ticket").text)
driver.find_element_by_id("query_ticket").click()
#driver.refresh()
#time.sleep(5)
#print(driver.page_source)
WebDriverWait(driver,20,1).until(lambda driver:driver.find_elements_by_css_selector("div#t-list>table>thead>tr>th"))
print("th")
th = driver.find_elements_by_css_selector("div#t-list>table>thead>tr>th")
titles = []
for title in th:
    titles.append(title.text)

WebDriverWait(driver,20,1).until(lambda driver:driver.find_elements_by_css_selector("div#t-list>table>tbody#queryLeftTable>tr"))
print("tr")
queryTbody = driver.find_elements_by_css_selector("div#t-list>table>tbody#queryLeftTable>tr")
queryResult = []

for tr in queryTbody:
    if tr.get_attribute("style") != "display:none;":
        queryResult.append(tr)

csvfile = open("download_csv\\ticket.csv","w",newline="",encoding="utf-8")

writer = csv.writer(csvfile)
writer.writerow(titles)

num = 1

for tr in queryResult:
    resultRow = []
    queryRow = []
    train_number = tr.find_element_by_css_selector("a.number").text
    station = tr.find_element_by_css_selector("div.cdz").text
    time = tr.find_element_by_css_selector("div.cds").text
    costTime = tr.find_element_by_css_selector("div.ls").text
    msgs = tr.find_elements_by_css_selector("td")

    queryRow.append(train_number)
    queryRow.append(station)
    queryRow.append(time)
    queryRow.append(costTime)

    afterMsgs = []

    for msg in msgs:
        if msg.get_attribute("style") == "cursor: pointer;":
            afterMsgs.append(msg.text)

    resultRow = queryRow + afterMsgs

    writer.writerow(resultRow)
    print(num)
    num = num + 1

csvfile.close()
driver.quit()



'''
import requests
from bs4 import BeautifulSoup

res = requests.get("https://kyfw.12306.cn/otn/leftTicket/init")
res.encoding="utf-8"
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
'''