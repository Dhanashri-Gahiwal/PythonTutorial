# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",port=8088,user="root",password="")

# open cursor
cursor = mysql_conn.cursor()

try:
    # database create
    empdb = "CREATE DATABASE employeeDB"

    # execute database
    cursor.execute(empdb)

    print("Database created successfully")

except Exception as e:
    print("Database already exist")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()