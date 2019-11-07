import pymysql
from settings import dbParams
conn = pymysql.Connect(**dbParams)

cursor =conn.cursor()

sql = "create  database bbs default charset=utf8"

cursor.execute(sql)

cursor.close()
conn.close()
# sql = "create table if not exists user (uid int primary key auto_increment,username varchar(10) unique,usertype " \
#       "enmu('普通用户','管理员') default 0,)"