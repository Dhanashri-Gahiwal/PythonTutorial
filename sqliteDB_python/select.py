# import sqlite database module
import sqlite3

# database connection
conn = sqlite3.connect("student.db")

# select query
select = "select * from student"

# execute select query
records = conn.execute(select)

# iterate records
for data in records:
    print(data)

# close connection
conn.close()