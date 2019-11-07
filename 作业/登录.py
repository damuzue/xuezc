import pymysql
from settings import dbParams1
from hashlib import  sha1

conn = pymysql.Connect(**dbParams1)
cursor = conn.cursor()

while True:
    username =input("请输入用户名：")
    password = input("请输入密码：")
    password = sha1(password.encode('utf8')).hexdigest()
    username = pymysql.escape_string(username)

    sql = "select uid from user where username='{}' and password='{}'".format(username,password)


    result = cursor.execute(sql)
    print(result)



    if result > 0:
        print("登录成功")
        exit()

    else:
        print("密码错误，请重新登录")

