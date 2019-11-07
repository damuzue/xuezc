import pymysql
from settings import dbParams1

conn = pymysql.Connect(**dbParams1)
cursor = conn.cursor()

sql = "select * from user"

result = cursor.execute(sql)
data = cursor.fetchone()
while data:
    print(data)
    data = cursor.fetchone()
print(data,type(data))

cursor.close()
conn.close()