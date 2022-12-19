


import os

if __name__ =="__main__":
    base_dir = ""
    # 1. A/B----> 2l_nested_dir
    # 2. A/B---->  dir_string
    dir_list = []
    dir_string_list = []
    file_list = []
    path_info =""
    for (dirname, subdir, subfile) in os.walk(base_dir):
        ret_file = [os.path.join(dirname,x) for x in subfile]
        for item in ret_file:
            file_list.append(item)

    for item in file_list:
        exec_file = item.split("\\")
        dir_sting = exec_file[2] + "/" + exec_file[3]
        dir_string_list.append(dir_sting)
        dir_path = os.path.join(os.path.join(base_dir,exec_file[2]),exec_file[3])
        dir_list.append(dir_path)
    for one_dir,one_dir_string in zip(dir_list,dir_string_list):
        print(one_dir,one_dir_string)

