import pymysql

conn = pymysql.connect(host="192.168.1.12", port=3306, user="root", password="admin123", db="userdb")

mysql = conn.cursor()

sql_lookup = "select * from userdb.users;"
#sql_add = "insert into userdb.users values ('4', 'Jake Wayne', 'Canada', 'Toronto', '38580');"
#sql_commit = "SET autocommit = 1;"
#mysql.execute(sql_add)
#mysql.execute(sql_commit)
mysql.execute(sql_lookup)

countrows = mysql.execute(sql_lookup)
print("Number of rows: ", countrows)
data = mysql.fetchall()
print(data)
