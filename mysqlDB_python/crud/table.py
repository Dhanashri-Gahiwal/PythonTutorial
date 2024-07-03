# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",user="root",password="",database="shop",port=8088)

# open cursor
cursor = mysql_conn.cursor()

try:
    # create table product
    product_table = '''
                    CREATE TABLE product(p_id INT PRIMARY KEY AUTO_INCREMENT,
                    p_name VARCHAR(50),
                    p_price VARCHAR(15),
                    p_quantity INT)
    '''

    # excute table query
    cursor.execute(product_table)

    print("Table created successfully")

except Exception as e:
    print("Table already exist")
    print(e)

finally:
    cursor.close()
    mysql_conn.close()