
import os


def readDatafile(filename):
    line_list = []
    with open(filename,"r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line_list.append(line)
    return line_list





if __name__ =="__main__":
    removefile_info = readDatafile("ted")

    file_list = []
    path_info =""
    for (dirname, subdir, subfile) in os.walk(path_info):
        ret_file = [os.path.join(dirname,x) for x in subfile]
        for item in ret_file:
            file_list.append(item)

    for item in file_list:
        exec_file = item.split("\\")[-1]
        if exec_file in removefile_info:
            os.remove(item)




