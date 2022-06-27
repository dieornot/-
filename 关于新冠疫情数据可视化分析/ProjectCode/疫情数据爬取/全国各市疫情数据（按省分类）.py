# 导入相关包
import csv
import os
from time import sleep
from tqdm import tqdm
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# # 当前目录下创建一个文件夹
# def crdir(dirname):
#     # 创建一个文件夹，用于存储爬取的数据
#     path = os.getcwd()
#     file_path = path + '\\' + dirname
#     try:
#         os.mkdir(file_path)
#     except Exception:
#         pass
# 数据存储
def save(path,type,data):
    # 将数据写入csv文件
    f = open(path, type, encoding='UTF-8', newline='')
    # 创建写操作
    mywrite = csv.writer(f)
    # 写入数据
    # writerow():单行写入
    mywrite.writerow(data)
    f.close()

# 创建一个文件夹，用于存储爬取的数据
path = os.getcwd()
file_path = os.path.join(path,'..','各省市数据')
try:
    os.mkdir(file_path)
except Exception:
    pass
# 创建浏览器对象
browser = webdriver.Chrome('../chromedriver.exe')
# 浏览器窗口最大化
# browser.maximize_window()

# 爬取的网页
URL = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner&qq-pf-to=pcqq.group#tab0'
# 请求网页
browser.get(url=URL)

# 点击切换地区按钮
browser.find_element(By.CSS_SELECTOR
                     ,'#main > div > div > header > div.Virus_1-1-317_19YIBv > span > span')\
    .click()
# 等待页面加载完成
sleep(1)
# 获取各个省索引存入列表
browser.find_element(By.CSS_SELECTOR
                     ,'#main > div > div > div:nth-child(6) > div > div.CityFilter_1-1-317_2VEW5Y > div.CityFilter_1-1-317_3dnwE2 > div:nth-child(1)')\
    .click()
province_list =browser.find_elements(By.CSS_SELECTOR,'#main > div > div > div:nth-child(6) > div > div:nth-child(2) > div:nth-child(1) > div')
province_len = len(province_list) - 3
# print(province_len)
# crdir('各省市数据')
# 在循环内点击各省按钮获取各省下的各市数据
for i in range(3,province_len-1):
    browser.find_element(By.CSS_SELECTOR
                         , f'#main > div > div > div:nth-child(6) > div >'
                           f' div.CityFilter_1-1-317_2VEW5Y > div.CityFilter_1-1-317_3dnwE2 > div:nth-child({i})') \
        .click()
    # 点击省下的第一个选项，获取该省各个市的数据
    browser.find_element(By.CSS_SELECTOR
                         ,'#main > div > div > div:nth-child(6) > div >'
                          ' div.CityFilter_1-1-317_2VEW5Y > div.CityFilter_1-1-317_t_7pVm > div:nth-child(1)') \
        .click()
    # 获取当前区域数据
    try:
        province = browser.find_element(By.CSS_SELECTOR,'#nationTable > table > tbody > tr.VirusTable_1-1-317_3m6Ybq > td.VirusTable_1-1-317_MdE8uT > div > span:nth-child(2)').text
        save(f'../各省市数据/{province}.csv','w',['市区','新增','现有','累计','治愈','死亡'])
        tbody_list = browser.find_elements(By.CSS_SELECTOR, '#nationTable > table > tbody > tr:nth-child(2) > td > table > tbody > tr')
        for j in tqdm(tbody_list,desc=f'{province}数据写入中'):
            region = j.find_element(By.CSS_SELECTOR,'tr > td:nth-child(1)').text
            if j.find_element(By.CSS_SELECTOR, 'tr > td:nth-child(2)').text == '待公布':
                newly_added = 0
            else:
                newly_added = j.find_element(By.CSS_SELECTOR, 'tr > td:nth-child(2)').text
            existing = j.find_element(By.CSS_SELECTOR, 'tr > td:nth-child(3)').text
            cumulative = j.find_element(By.CSS_SELECTOR, 'tr > td:nth-child(4)').text
            cure = j.find_element(By.CSS_SELECTOR, 'tr > td:nth-child(5)').text
            death = j.find_element(By.CSS_SELECTOR, 'tr > td:nth-child(6)').text
            data = [f'{region}',f'{newly_added}',f'{existing}',f'{cumulative}',f'{cure}',f'{death}']
            # print(data)
            save(f'../各省市数据/{province}.csv','a',data)
    except:
        sleep(1)
        pass
    # 点击切换地区
    browser.find_element(By.CSS_SELECTOR
                         ,
                         '#main > div > div > header > div.Virus_1-1-317_19YIBv > span > span') \
        .click()
# 等待页面加载完成
    sleep(2)
browser.quit()
print('FINISHED')