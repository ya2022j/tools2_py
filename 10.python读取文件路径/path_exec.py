


# python读取文件路径,上一级文件路径，上上一级文件路径的

# https://www.jianshu.com/p/170720d769f3

#
# 1，获取当前文件路径(工作路径)
#
# #获取当前文件路径
#
# #方法一import os
#
# Path=os.getcwd()print(Path)
#
# 结果：E:\newdocument\文件
#
# #----------------------
#
# #方法二
#
# import os
#
# Path=os.path.abspath(os.path.dirname(__file__))print(Path)
#
# 结果：E:\newdocument\文件
#
# 2，获取上一级文件路径
#
# #获取上一级文件路径
#
# #方法一
#
# import os
#
# Path=os.path.dirname(os.getcwd())print(Path)
#
# 结果：E:\newdocument
#
# #----------------------
#
# #方法二
#
# Path=os.path.abspath(os.path.join(os.getcwd(),".."))
#
# print(Path)
#
# 结果：E:\newdocument
#
#
#
# 3，获得上上一级文件路径
#
# #获取上上一级文件路径
#
# import os
#
# Path=os.path.abspath(os.path.join(os.getcwd(),"../.."))
#
# print(Path)
#
# 结果：E:\


