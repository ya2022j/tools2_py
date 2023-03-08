#coding=utf-8
import re
import time

import pymysql

import requests


class Uniapp_plugin_info():
    def __init__(self):
        self.url = url


    def exec(self,url):
        try:

            html = self.request_html(url)
            ret_parse =  self.parse_html(html)
            if "购买" in ret_parse[1]:
                fee_flg = "1"
            else:
                fee_flg = "0"

            self.insertDB([(ret_parse[0], ret_parse[1], url, fee_flg)])

        except Exception as e:
            pass





    def request_html(self,url):

        res = requests.get(url)
        return res.text

    def parse_html(self,html):
        pattern = re.compile('<div class="col-lg-9 col-md-9 col-sm-9 col-xs-12 plugin-info">(.*?)<div class="col-lg-3 col-md-3 col-sm-3 col-sm-12 banner-side">',re.S)
        items = re.findall(pattern,html)
        try:


            bs = BeautifulSoup(items[0], "html.parser")
            h3_title = "".join(bs.find("h3").text.split())

            ret = " ".join(bs.text.split())
            return h3_title, ret
        except Exception as e:
            pass


    def insertDB(self,content):

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='uniapp',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()
        try:
            print(content)

            cursor.executemany('insert into uniapp_plugin (title,info,url,fee_flg) values (%s,%s,%s,%s)',
                               content)
            connection.commit()
            connection.close()
            print('向MySQL中添加数据成功！')
        except Exception as e:
            raise e





from bs4 import BeautifulSoup
if __name__ == "__main__":

    for item in range(1,22222):

        url = "https://ext.dcloud.net.cn/plugin?id={0}".format(item)
        print(url)
        ins = Uniapp_plugin_info()
        ins.exec(url)
        time.sleep(3)








# create table uniapp_plugin (id int not null primary key auto_increment,
# title  varchar(255),
# info  text,
# url  varchar(255),
# fee_flg varchar(1) NOT NULL DEFAULT '0'
# ) engine=InnoDB  charset=utf8;
