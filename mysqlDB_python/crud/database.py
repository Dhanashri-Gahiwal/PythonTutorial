# import mysql database module
import pymysql as mq

# connect to mysql
mysql_conn = mq.connect(host="localhost",user="root",password="",port=8088)

# open cursor
cursor = mysql_conn.cursor()

try:
    # create database
    shop_db = "CREATE DATABASE shop"

    # execute database query
    cursor.execute(shop_db)

    print("Database created successfully")

except:
    print("Database already exist")