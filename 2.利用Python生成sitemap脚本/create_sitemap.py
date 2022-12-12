# -*- coding:utf-8 -*-

import datetime
import os.path
import re

# 利用Python生成sitemap脚本
# https://www.jianshu.com/p/30f127c48b46



# def get_url():
#     with open('D:\\Excel\\sitemap\\可用.txt', 'r', encoding='UTF-8') as f:
#         list1 = []
#         for i in f:
#             line = i.strip()
#             list1.append(line)

#         return list1


def creat_xml(filename, url_list):  # 生成sitemap所需要的xml方法
    header = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    file = open(filename, 'a', encoding='utf-8')
    file.writelines(header)
    file.close()

    for url in url_list:
        times = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        urls = re.sub(r"&", "&amp;", url)  # 注意这里,在URL中如果含有&将会出错,所以需要进行转义

        # 这个是生成的主体,可根据需求进行修改
        ment = "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n" % (urls, times)

        file = open(filename, 'a', encoding='utf-8')
        file.writelines(ment)
        file.close()

    last = "</urlset>"
    file = open(filename, 'a', encoding='utf-8')
    file.writelines(last)
    file.close()


if __name__ == '__main__':
    # url_list = get_url()
    url_list = ['https://search.google.com', 'https://www.google.com', 'https://translate.google.cn']
    creat_xml(os.path.join(os.getcwd(),"ss.xml"), url_list*6)




######################


from flask import Flask,request,send_from_directory


app = Flask(__name__)

# 这样就可以加载多个xml文件了
# 都放在static文件夹下，彼此之间又有链接关系
@app.route("/robots.txt")
@app.route("/s1.xml")
@app.route("/s2.xml")
@app.route("/ss.xml")
def static_from_root():
    return send_from_directory(app.static_folder,request.path[1:])


if __name__ =="__main__":
    app.run(debug=True)
