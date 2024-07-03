# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",port=8088,database="shop")

# open cursor
cursor = mysql_conn.cursor()

try:
    # product query(by default asc order)
    # filter = "SELECT * FROM product"

    # desc order qyery
    # filter = "SELECT * FROM product ORDER BY p_name DESC"

    # limit qyery
    # filter = "SELECT * FROM product LIMIT 1"
    # filter = "SELECT * FROM product LIMIT 1,2"

    # distinct qyery
    # filter = "SELECT DISTINCT(p_price) FROM product"

    # in qyery
    # filter = "SELECT * FROM product WHERE p_id IN (1,3)"

    # not in qyery
    # filter = "SELECT * FROM product WHERE p_id NOT IN (1,3)"

    # between qyery
    # filter = "SELECT * FROM product WHERE p_id BETWEEN 3 AND 5"

    # equal qyery
    # filter = "SELECT * FROM product WHERE p_name = 'ear rings'"

    # many condition qyery
    # filter = "SELECT * FROM product WHERE p_name = 'ear rings' AND p_quantity = 100"
    # filter = "SELECT * FROM product WHERE p_name = 'ear rings' OR p_quantity = 50"

    # like qyery
    # filter = "SELECT * FROM product WHERE p_name LIKE '%r%'"
    # filter = "SELECT * FROM product WHERE p_name LIKE 'p%'"
    filter = "SELECT * FROM product WHERE p_name LIKE '%er'"

    # execute query
    cursor.execute(filter)

    # fetch min record
    filterR = cursor.fetchall()
    for i in filterR:
        print(i)

except Exception as e:
    print("Error in fetching records")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()