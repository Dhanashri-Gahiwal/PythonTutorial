# import sqlite database module
import sqlite3

# database connection
conn = sqlite3.connect("student.db")

# insert query
insert = '''
        insert into student(s_name,s_email,s_class) values('Shital','shital@gmail.com','10th')
'''

# execute insert query
conn.execute(insert)

# save changes(commit)
conn.commit()

# close connection
conn.close()