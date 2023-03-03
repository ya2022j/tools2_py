import os

import json



#递归遍历/root目录下所有文件


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


def input_text_KeyEnter(url,inputContent):
    ch_options = webdriver.ChromeOptions()
    # 为Chrome配置无头模式

    # 在启动浏览器时加入配置
    dr = webdriver.Chrome(options=ch_options)
    dr.get(url)
    time.sleep(3)

    dr.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/section/div/div/div[1]/div[2]/div[1]/div[5]').send_keys(inputContent)
    # dr.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div[2]/input').send_keys(Keys.ENTER)





def tree_path_json(path):
    dir_structure = {}
    base_name = os.path.basename(os.path.realpath(path))
    if os.path.isdir(path):
        dir_structure[base_name] = [tree_path_json(os.path.join(path, file_name)) for file_name in os.listdir(path)]
    else:
        return os.path.basename(path)
    return dir_structure

# 1. 先生成文件目录的列表
# 2. 把文件目录的列表塞进json里面

def writeinto_jsonfile(filename,list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=2, ensure_ascii=False)


def output_json(jsonfile,path):
    big_dict = dict(tree_path_json(path))
    input_text_KeyEnter(url,big_dict)
    writeinto_jsonfile(jsonfile,[big_dict])
    print(big_dict)

if  __name__ == "__main__":
    url = "https://jsoncrack.com/editor"
    path_info = "/home/vue22"
    json_file = path_info.split("/")[-1] + ".json"

    output_json(json_file,path_info)
