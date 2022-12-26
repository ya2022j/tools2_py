def insertDB_dict(dbname=None,tlname=None,**kwargs):

    keys_ = ",".join([x for x in kwargs.keys()])
    values_ = [tuple([x for x in kwargs.values()])]


    slice_ = "%s,"*len(keys_.split(","))
    sql_info ='insert into {0} ({1}) values ({2})'.format(tlname,keys_,slice_[:-1])
    # print(keys_)
    # print(values_)
    # print(slice_[:-1])
    # print(sql_info)

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db=dbname,
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany(sql_info, values_)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass




if __name__ == '__main__':
    gh_info = {}
    gh_info["ab_k"] = "ab_v"
    gh_info["ac_k"] = "ac_v"
    gh_info["ad_k"] = "ad_v"
    gh_info["ae_k"] = "ae_v"
    insertDB_dict(dbname="adsf",tlname="ssss",**gh_info)
