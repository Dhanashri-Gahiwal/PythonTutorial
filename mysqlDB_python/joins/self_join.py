# import mysql database modulr
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",port=8088,database="ecommerce")

# open cursor
cursor = mysql_conn.cursor()

try:
    # self join query
    # self_join = "SELECT * FROM orders as o1, orders as o2 WHERE o1.product_id = o2.order_id"
    self_join = "SELECT o1.order_id,o1.order_date,o1.product_id FROM orders as o1, orders as o2 WHERE o1.product_id = o2.order_id"
    # self_join = "SELECT * FROM orders"

    # execute self join query
    cursor.execute(self_join)

    # fetch all records
    data = cursor.fetchall()

    # iterate data
    for i in data:
        print(i)

except Exception as e:
    print("Error in fetching data")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()