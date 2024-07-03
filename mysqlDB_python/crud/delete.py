# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",database="shop",port=8088)

# open cursor
cursor = mysql_conn.cursor()

id = input("Enter product id:-")

try:
    # delete query
    delete = "DELETE FROM product WHERE p_id=%s"

    # execute delete query
    cursor.execute(delete,id)

    # commit(save) changes
    mysql_conn.commit()

    print("Record deleted successfully")

except Exception as e:
    print("Error in deleting record")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()