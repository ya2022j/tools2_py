



# https://github.com/letterbeezps/chatgo
# https://github.com/letterbeezps/chatgo.git
import os

if __name__ == "__main__":
    base_dir = ""
    gh_url_list = ["https://github.com/letterbeezps/chatgo"]
    # 批量给list中每个元素做一个操作，使用列表表达式或者map+lambda表达式
    gh_url_list_url = map(lambda x: x+".git", gh_url_list)
    for item in gh_url_list_url:
        download_cmd = "git clone {0}".format(item)
        pro_dir = item.replace(".git","")
        pro_dir = pro_dir.replace("https://github.com/","")
        if "/" in pro_dir:
            pro_dir = pro_dir.replace("/","\\")
        download_dir = os.path.join(base_dir,pro_dir)

        os.makedirs(download_dir)
        os.chdir(download_dir)
        os.system(download_cmd)

