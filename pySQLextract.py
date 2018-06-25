import pymysql

conn = pymysql.connect(host="192.168.1.12", port=3306, user="root", password="admin123", db="userdb")

mysql = conn.cursor()

sql_lookup = "select * from userdb.materialdb_userdb;"

#make first value increment of the second value for the addition command

sql_add = "insert into userdb.materialdb_userdb values ('6','5', 'Jake Wayne', 'Canada', 'Toronto', '$45,704');"
sql_commit = "SET autocommit = 1;"
mysql.execute(sql_add)
mysql.execute(sql_commit)
mysql.execute(sql_lookup)

countrows = mysql.execute(sql_lookup)
print("Number of rows: ", countrows)
data = mysql.fetchall()
print(data)
