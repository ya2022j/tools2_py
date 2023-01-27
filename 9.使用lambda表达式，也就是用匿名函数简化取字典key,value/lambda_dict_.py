old_dt = [{"python":[{"d":["dd","t.py"]}]}]



# 使用lambda表达式，也就是用匿名函数简化取字典key,value的步骤
getkey = lambda x: [x for x in old_dt[0].keys()][0]
getvalue = lambda x: [x for x in old_dt[0].values()][0]

# getkey(old_dt)--->"python"
# getvalue(old_dt)---> [{"d":["dd","t.py"]}]
