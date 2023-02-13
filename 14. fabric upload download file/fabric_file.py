from fabric import Connection
import os

def scaner_file (window_path):
    path_list = []
    file = os.listdir(window_path)
    for f in file:
        read_path = os.path.join(window_path,f)
        path_list.append(read_path)
    return path_list


# 1. 遍历目录下的所有文件
# 2. 再遍历上传

def from_Windows_upload_to_linux(window_path,username,Linux_ip,password,Linux_path):

    c = Connection(host=f'{username}@{Linux_ip}',connect_kwargs={'password': password})
    path_list = scaner_file(window_path)
    for one_file in path_list:
        c.put(one_file, remote=Linux_path)

def from_linux_download_to_windows(window_path,username,Linux_ip,password,Linux_path):

    c = Connection(host=f'{username}@{Linux_ip}',connect_kwargs={'password': password})
    with c.cd(Linux_path):
    # # 这里执行的就是远程服务器的 shell ：
    # c.run("echo '[Current path] ' `pwd`;")
    # # 命令 put 为从本地上传文件到远端
        c.put(window_path, Linux_path)
    # # 压缩文件
    # c.run("tar -xzvf  archive.tar.gz -C /data/www/")
    # # 命令 get 为从远程下载文件到本地
        c.get('/home/t/flarum.sql')




if __name__ == "__main__":
    username = "root"
    password = "123456"
    Linux_ip = "192.168.56.136"
    window_path = r''
    Linux_path = r'/mnt'
    Linux_path2 = r'/home/t'
    # from_Windows_upload_to_linux(window_path, username, Linux_ip, password, Linux_path)
    from_linux_download_to_windows(window_path, username, Linux_ip, password, Linux_path2)
