# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",port=8088,database="shop")

# open cursor
cursor = mysql_conn.cursor()

try:
    # product query
    # agg = "SELECT * FROM product"

    # min qyery
    # agg = "SELECT MIN(p_quantity) FROM product"

    # max qyery
    # agg = "SELECT MAX(p_quantity) FROM product"

    # avg qyery
    # agg = "SELECT AVG(p_quantity) FROM product"

    # sum qyery
    # agg = "SELECT SUM(p_quantity) FROM product"

    # count qyery
    agg = "SELECT COUNT(*) FROM product"

    # execute query
    cursor.execute(agg)

    # fetch min record
    aggr = cursor.fetchall()
    for i in aggr:
        # print(i)
        # print("minimum product quantity:",i)
        # print("maximum product quantity:",i)
        # print("average product quantity:",i)
        # print("total product quantity:",i)
        print("total products:",i)

except Exception as e:
    print("Error in fetching records")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()