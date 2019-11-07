import pymysql
from settings import dbParams1

conn = pymysql.Connect(**dbParams1)
cursor = conn.cursor()
# username = 'xzc'
sql = "select * from user"
# sql = "select username,password from user where username='{}'".format(username)
result = cursor.execute(sql)
data = cursor.fetchone()
while data:
    print(data)
    data = cursor.fetchone()
print(data,type(data))

cursor.close()
conn.close()