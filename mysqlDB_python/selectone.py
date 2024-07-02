# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",database="shop",port=8088)

# open cursor
cursor = mysql_conn.cursor()

try:
    id = input("Enter product id:-")
    # select query 1st way
    # select = "SELECT * FROM product WHERE p_id ="+id

    # select query 2nd way
    select = "SELECT * FROM product WHERE p_id =%s"

    # execute select query 1st way
    # cursor.execute(select)

    # execute select query 2nd way
    cursor.execute(select,id)

    # fetch single record
    record = cursor.fetchone()
    print(record) 

except Exception as e:
    print("Error in fetching record")
    print(e)

finally:
    mysql_conn.close()