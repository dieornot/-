# 导入相关包
import csv
import os
from tqdm import tqdm
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象


browser = webdriver.Chrome('../chromedriver.exe')
# 浏览器窗口最大化
# browser.maximize_window()

# 爬取的网页
URL = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner&qq-pf-to=pcqq.group#tab0'
# 请求网页
browser.get(url=URL)
# 点击'国外疫情'跳转到国外疫情数据页面
browser.find_element(By.CSS_SELECTOR
                     ,'#tab > div > a:nth-child(2)')\
    .click()
# 点击美国了解详情
browser.find_element(By.CSS_SELECTOR
                     ,'#foreignTable > table > tbody > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > div.VirusTable_1-1-317_AcDK7v')\
    .click()
# 爬取美国全国的疫情数据的tbody
tbody_list = browser.find_elements(By.CSS_SELECTOR,'#nationTable > table > tbody > tr:nth-child(2) > td > table > tbody > tr')
# 创建‘美国疫情数据’到文件夹中，并写好列名
f = open(f'../疫情数据/美国疫情数据.csv', 'w', encoding='UTF-8', newline='')
# 创建写操作
mywrite = csv.writer(f)
# 写入列名
# writerow():单行写入
mywrite.writerow(['区域','累计确诊', '治愈', '死亡'])
f.close()
# 遍历获取到的各州源码，提取其中的数据
for i in tqdm(tbody_list,desc='美国数据写入中'):
    region = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(1)').text
    # print(region)
    # newly_added = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(2)').text
    # existing = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(3)').text
    cumulative = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(2)').text
    cure = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(3)').text
    death = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(4)').text
    # print(region,newly_added,cumulative,cure,death)
    # 将数据写入csv文件
    f = open(f'../疫情数据/美国疫情数据.csv', 'a', encoding='UTF-8', newline='')
    # 创建写操作
    mywrite = csv.writer(f)
    # 写入数据
    # writerow():单行写入
    mywrite.writerow([f'{region}',f'{cumulative}',f'{cure}',f'{death}'])
    f.close()
browser.quit()
print('FINISHED')