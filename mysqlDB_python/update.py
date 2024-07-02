# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",database="shop",port=8088)

# open cursor
cursor = mysql_conn.cursor()

id = input("Enter product id:-")
name = input("Enter product name:-")
price = input("Enter product price:-")
quantity = input("Enter product quantity:-")

try:
    # update query
    update = "UPDATE product SET p_name=%s, p_price=%s, p_quantity=%s WHERE p_id=%s"

    data = (name,price,quantity,id)

    # execute update query
    cursor.execute(update,data)

    # commit(save) changes
    mysql_conn.commit()

    print("Record updated successfully")

except Exception as e:
    print("Error in updating record")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()