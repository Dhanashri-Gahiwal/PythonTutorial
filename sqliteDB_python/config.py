# import sqlite database module
import sqlite3

# database connection
conn = sqlite3.connect("student.db")

# create table query
student_table = '''
                CREATE TABLE student(
                s_id INTEGER PRIMARY KEY AUTOINCREMENT,
                s_name VARCHAR(50),
                s_email VARCHAR(50),
                s_class VARCHAR(5)
                )
'''

# execute table query
conn.execute(student_table)

# close connection
conn.close()