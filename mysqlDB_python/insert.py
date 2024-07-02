# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",database="shop",port=8088)

# open cursor
cursor = mysql_conn.cursor()

try:
    # insert records
    insert = "INSERT INTO product(p_name,p_price,p_quantity) VALUES(%s,%s,%s)"

    data = [
        ("dove shampoo","250","50"),
        ("ponds powder","100","150")
    ]


    # execute insert query
    cursor.executemany(insert, data)

    # commit(save) changes
    mysql_conn.commit()

    print("records inserted successfully")

except Exception as e:
    print("Error in inserting records")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()