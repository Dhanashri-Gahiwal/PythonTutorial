# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",port=8088,user="root",password="",database="employeeDB")

# open cursor
cursor = mysql_conn.cursor()

try:
    # table create
    emptbl = '''
            CREATE TABLE employee(
            e_id INT PRIMARY KEY AUTO_INCREMENT,
            e_name VARCHAR(50),
            e_email VARCHAR(50) UNIQUE,
            e_phone VARCHAR(10) UNIQUE,
            e_designation VARCHAR(50),
            e_salary VARCHAR(10)
            )
    '''

    # execute database
    cursor.execute(emptbl)

    print("Table created successfully")

except Exception as e:
    print("Table already exist")
    print(e)

finally:
    # close cursor & connection
    cursor.close()
    mysql_conn.close()