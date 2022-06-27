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
# 点击‘展开全部’使网页加载全部数据
browser.find_element(By.CSS_SELECTOR
                     ,'#nationTable > div > span')\
    .click()
# 创建一个文件夹，用于存储爬取的数据
path = os.getcwd()
file_path = os.path.join(path,'..','疫情数据')
try:
    os.mkdir(file_path)
except Exception:
    pass
# *****************************************************************************
# 国内数据爬取
# 用于统计国内数据
Ch_newly_added = 0
Ch_cumulative = 0
Ch_cure = 0
Ch_death = 0
# 爬取包含各省数据的tbody
tbody_list = browser.find_elements(By.CSS_SELECTOR,'#nationTable > table > tbody > tr')
# print(tbody_list)
# 遍历获取各省的数据并写入表格文件中
# 创建‘中国疫情数据’到文件夹中，并写好列名
f = open(f'../疫情数据/中国疫情数据.csv', 'w', encoding='UTF-8', newline='')
# 创建写操作
mywrite = csv.writer(f)
# 写入列名
# writerow():单行写入
mywrite.writerow(['区域', '新增', '现有', '累计', '治愈', '死亡'])
f.close()
# 遍历获取到的各省源码，提取其中的数据
for i in tqdm(tbody_list,desc='国内数据写入中'):
    region = i.find_element(By.CSS_SELECTOR,' tr > td.VirusTable_1-1-317_MdE8uT > div > span:nth-child(2)').text
    # print(region)
    if i.find_element(By.CSS_SELECTOR,'tr > td.VirusTable_1-1-317_3x1sDV.VirusTable_1-1-317_2bK5NN').text == '待公布':
        newly_added = 0
    else:
        newly_added = i.find_element(By.CSS_SELECTOR,'tr > td.VirusTable_1-1-317_3x1sDV.VirusTable_1-1-317_2bK5NN').text
    existing = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(3)').text
    cumulative = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(4)').text
    cure = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(5)').text
    death = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(6)').text
    # 求和,暂未公布的数据不计入
    try:
        Ch_newly_added += int(newly_added)
        Ch_cumulative += int(cumulative)
        Ch_cure += int(cure)
        Ch_death += int(death)
    except:
        pass
    # print(newly_added,existing,cumulative,cure,death)
    # 将数据写入csv文件
    f = open(f'../疫情数据/中国疫情数据.csv', 'a', encoding='UTF-8', newline='')
    # 创建写操作
    mywrite = csv.writer(f)
    # 写入数据
    # writerow():单行写入
    mywrite.writerow([f'{region}',f'{newly_added}',f'{existing}',f'{cumulative}',f'{cure}',f'{death}'])
    f.close()

# ***********************************************************************************
# 外国数据爬取
# 点击'国外疫情'跳转到国外疫情数据页面
browser.find_element(By.CSS_SELECTOR
                     ,'#tab > div > a:nth-child(2)')\
    .click()
# 点击‘展开全部’使网页加载全部数据
browser.find_element(By.CSS_SELECTOR
                     ,'#foreignTable > div > span')\
    .click()
# 爬取包含各国数据的tbody
tbody_list = browser.find_elements(By.CSS_SELECTOR,'#foreignTable > table > tbody > tr > td > table > tbody > tr')
# print(tbody_list)
# 遍历获取各国的数据并写入表格文件中
# 创建‘外国疫情数据’到文件夹中，并写好列名
f = open(f'../疫情数据/外国疫情数据.csv', 'w', encoding='UTF-8', newline='')
# 创建写操作
mywrite = csv.writer(f)
# 写入列名
# writerow():单行写入
mywrite.writerow(['区域', '新增', '累计', '治愈', '死亡'])
f.close()
# 遍历获取到的各国源码，提取其中的数据
for i in tqdm(tbody_list,desc='国外数据写入中'):
    region = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(1)').text
    # print(region)
    if i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(2)').text == '待公布':
        newly_added = 0
    else:
        newly_added = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(2)').text
    # existing = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(3)').text
    cumulative = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(3)').text
    cure = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(4)').text
    death = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(5)').text
    # print(region,newly_added,cumulative,cure,death)
    # 将数据写入csv文件
    f = open(f'../疫情数据/外国疫情数据.csv', 'a', encoding='UTF-8', newline='')
    # 创建写操作
    mywrite = csv.writer(f)
    # 写入数据
    # writerow():单行写入
    mywrite.writerow([f'{region}',f'{newly_added}',f'{cumulative}',f'{cure}',f'{death}'])
    f.close()

# ***********************************************************************************************
# 全球疫情数据(在外国数据的基础上把国内统计数据写入表中）
f = open(f'../疫情数据/全球疫情数据.csv', 'w', encoding='UTF-8', newline='')
# 创建写操作
mywrite = csv.writer(f)
# 写入列名
# writerow():单行写入
mywrite.writerow(['区域', '新增', '累计', '治愈', '死亡'])
f.close()
# 遍历获取到的各国源码，提取其中的数据
for i in tqdm(tbody_list,desc='全球数据写入中'):
    region = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(1)').text
    # print(region)
    if i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(2)').text == '待公布':
        newly_added = 0
    else:
        newly_added = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(2)').text
    # existing = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(3)').text
    cumulative = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(3)').text
    cure = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(4)').text
    death = i.find_element(By.CSS_SELECTOR,'tr > td:nth-child(5)').text
    # print(region,newly_added,cumulative,cure,death)
    # 将数据写入csv文件
    f = open(f'../疫情数据/全球疫情数据.csv', 'a', encoding='UTF-8', newline='')
    # 创建写操作
    mywrite = csv.writer(f)
    # 写入数据
    # writerow():单行写入
    mywrite.writerow([f'{region}',f'{newly_added}',f'{cumulative}',f'{cure}',f'{death}'])
    f.close()
# 在外国数据的基础上把国内统计数据写入表中
f = open(f'../疫情数据/全球疫情数据.csv', 'a', encoding='UTF-8', newline='')
# 创建写操作
mywrite = csv.writer(f)
# 写入数据
# writerow():单行写入
mywrite.writerow(['中国',f'{Ch_newly_added}',f'{Ch_cumulative}',f'{Ch_cure}',f'{Ch_death}'])
f.close()
# print('爬取结束')
browser.quit()
print('FINISHED')
