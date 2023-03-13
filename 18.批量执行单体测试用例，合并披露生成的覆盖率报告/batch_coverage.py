#! -*- utf-8 -*-

import os




if __name__ =="__main__":
    file_list = []
    path_info =""



    for (dirname, subdir, subfile) in os.walk(path_info):
        ret_file = [os.path.join(dirname, x) for x in subfile]
        for item in ret_file:
            file_list.append(item)
    os.system("coverage erase")
    for item in file_list:
        exec_file = item.split("\\")[-1]
        if "test_" in exec_file and ".py" in exec_file and ".pyc" not in exec_file:
            print(item)
            os.system("coverage run  -p {0}".format(item)) # 生成多个文件的报告

    os.system("coverage combine")

    os.system("coverage html -d report")






