#!/usr/bin/env python
#-*-coding:utf8-*-
"""
分析Nginx等Web应用访问IP信息 并将其访问数量从大到小排序
"""
ip_list=[] #定义空列表 所有的访问IP放置在该列表中
ip_count={}#定义一个空字典 将IP和访问的次数放置到该字典中



import copy
import re
import json
import time

import requests
from lxml import etree
import datetime
import csv
import copy
import re
import json
import time
from lxml import etree
from selenium import webdriver
import csv
import os
import os
ch_options = webdriver.ChromeOptions()
# 为Chrome配置无头模式
ch_options.add_argument("--headless")
ch_options.add_argument('--no-sandbox')
ch_options.add_argument('--disable-gpu')
ch_options.add_argument('--disable-dev-shm-usage')
# 在启动浏览器时加入配置
driver = webdriver.Chrome(options=ch_options)





def writeintoCSV_file(filename,data):
    with open(filename,'a', newline='\n', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)
def to_fetch_ip_info(filename):
    """
    分析Nginx等Web应用访问IP信息 并将其访问数量从大到小排序
    """
    ip_list = []  # 定义空列表 所有的访问IP放置在该列表中
    ip_count = {}  # 定义一个空字典 将IP和访问的次数放置到该字典中
    with  open(filename, "r") as ngfile:  # 打开日志文件
        for line in ngfile:
            # print(line.split())  调试信息
            ip_list.append(line.split()[0])  # 用split分割字符串获取到列表line.split()[0] 每行的IP地址
    for count in set(ip_list):  # 将ip_list去重
        ip_number = ip_list.count(count)  # 统计每个IP出现的次数
        ip_count.setdefault(count, ip_number)  # 将IP以及数量更新到字典
    ip_count_new = sorted(ip_count.items(), key=lambda d: d[1], reverse=True)  # 使用lambda函数 对其重新排序构建新字典
    for eachip in ip_count_new:
        ip_item_info = eachip[0]
        ip_item_times = eachip[1]
        print(ip_item_times, ip_item_info)


def fromNginxlogfile_to_IPcsvfile_(csvfile,args):
    writeintoCSV_file(csvfile,[args])
    for _, _, files in os.walk(os.getcwd()):
        for item_log in files:
            if ".log" in item_log:
                with open(item_log, "r") as ngfile:  # 打开日志文件
                    for line in ngfile:
                        writeintoCSV_file(csvfile,[line.split()[0]])
if __name__ == "__main__":
    fromNginxlogfile_to_IPcsvfile_("nginx.csv","IP")




