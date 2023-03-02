
#! -*- coding:utf-8 -*-

"""
Notice
# AttributeError: 'WebDriver' object has no attribute 'find_element_by_xpath'

# pip3 uninstall selenium

#  pip3  install selenium==3.141.0  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

"""

import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def readDatafile(filename):
    line_list = []
    with open(filename,"r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line_list.append(line)
    return line_list

def input_text_KeyEnter(url,inputContent):
    ch_options = webdriver.ChromeOptions()
    # 为Chrome配置无头模式
    ch_options.add_argument("--headless")
    ch_options.add_argument('--no-sandbox')
    ch_options.add_argument('--disable-gpu')
    ch_options.add_argument('--disable-dev-shm-usage')
    # 在启动浏览器时加入配置
    dr = webdriver.Chrome(options=ch_options)
    dr.get(url)
    time.sleep(3)

    dr.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div[2]/input').send_keys(inputContent)
    dr.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div[2]/input').send_keys(Keys.ENTER)



if __name__ == "__main__":
    url = "http://127.0.0.1:8080/"
    ret = readDatafile("dt")
    for item in ret:
        print(item)
        input_text_KeyEnter(url,item)
        print("----->OK")


