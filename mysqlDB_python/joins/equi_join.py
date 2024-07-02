# import mysql database modulr
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",port=8088,database="ecommerce")

# open cursor
cursor = mysql_conn.cursor()

try:
    # equi join query
    # equi_join = "SELECT * FROM product as p, orders as o WHERE p.product_id = o.product_id"
    equi_join = "SELECT p.product_id,product_name,order_id FROM product as p, orders as o WHERE p.product_id = o.product_id"
    # equi_join = "SELECT * FROM product"
    # equi_join = "SELECT * FROM orders"

    # execute equi join query
    cursor.execute(equi_join)

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