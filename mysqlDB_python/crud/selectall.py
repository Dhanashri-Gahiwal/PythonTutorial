# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",database="shop",port=8088)

# open cursor
cursor = mysql_conn.cursor()
print("{:<20} | {:<20} | {:<20} | {:<20}".format("Product ID","Product Name","Product Price","Product Quantity"))
print("_____________________________________________________________________________________")

try:
    # select query
    select = "SELECT * FROM product"

    # execute select query
    cursor.execute(select)

    # fetch all records
    records = cursor.fetchall()
    for n in records:  
        print("{:<20} | {:<20} | {:<20} | {:<20}".format(n[0],n[1],n[2],n[3]))      
        # print(n)

except Exception as e:
    print("Error in fetching records")
    print(e)

finally:
    mysql_conn.close()