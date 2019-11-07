import pymysql
from settings import dbParams1
from hashlib import  sha1

conn = pymysql.Connect(**dbParams1)
cursor = conn.cursor()
while True:
    username =input("请输入用户名：")
    password = input("请输入密码：")
    # password = sha1(password.encode('utf8')).hexdigest()
    username = pymysql.escape_string(username)
    sql = "select username,password from user where username='{}'".format(username)
    result = cursor.execute(sql)
    data = cursor.fetchone()
    while data:
        print(data)
        data = cursor.fetchone()
    if result == 0:
        print("用户名错误,请重新登录")
    else:
        if data[1] == password:
            print("登录成功")
            cursor.close()
            conn.close()
            break
        else:
            print("密码错误，请重新登录")
