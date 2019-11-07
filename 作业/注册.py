from hashlib import  sha1

import pymysql
from settings import dbParams1

conn = pymysql.Connect(**dbParams1)
cursor = conn.cursor()

while True:
    username = input("请输入用户名:")
    password = input("请输入密码：")

    if len(username) >= 2 or username.isspace() == 0:
        password = sha1(password.encode('utf8')).hexdigest()
        username = pymysql.escape_string(username)
        sql1 = "select  username from user where username = '{}' ".format(username)
        result = cursor.execute(sql1)
        if result > 0:
            print("表中已存在该用户名,请重新输入")

        else:
            sql= "insert into user(username,password) values('{}','{}')".format(username, password)

            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            break

    else:
        print("用户名长度必须大于2,不能为纯空格,请重新输入")



