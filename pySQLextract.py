import pymysql

conn = pymysql.connect(host="192.168.1.12", port=3306, user="root", password="admin123", db="userdb")

mysql = conn.cursor()

sql_lookup = "select * from userdb.materialdb_userdb;"

#make first value increment of the second value for the addition command

name = "Diane Hallow"
country = "United States"
city = "New York"
salary = "$75,000"
sql_add = ("insert into userdb.materialdb_userdb (name,country,city,salary ) values ('%s', '%s', '%s', '%s');" % (name, country, city, salary))
sql_commit = "SET autocommit = 1;"
mysql.execute(sql_add)
mysql.execute(sql_commit)
mysql.execute(sql_lookup)

countrows = mysql.execute(sql_lookup)
print("Number of rows: ", countrows)
data = mysql.fetchall()
print(data)
