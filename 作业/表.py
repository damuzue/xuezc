import pymysql

conn = pymysql.Connect(host='127.0.0.1',user='root',password='xzc',db='bbs',port=3306,charset='utf8')

cursor =conn.cursor()

sql = "create table if not exists user (uid int primary key auto_increment,username varchar(10) unique,usertype  \
      enum('普通用户','管理员') default '普通用户',password varchar(300) not null,regtime datetime,email varchar(100))"

cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()