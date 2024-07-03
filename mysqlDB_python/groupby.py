# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",port=8088,database="ecommerce")

# open cursor
cursor = mysql_conn.cursor()

try:
    # select all products query
    # prod = "SELECT * FROM product"

    # group by query 
    # prod = "SELECT * FROM product GROUP BY category_id"
    prod = "SELECT COUNT(category_id) FROM product GROUP BY category_id"

    # execute query
    cursor.execute(prod)

    # fetch all records
    records = cursor.fetchall()

    # iterate all records
    for i in records:
        print(i)

except Exception as e:
    print("Error in fetching records")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()