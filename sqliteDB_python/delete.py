# import sqlite database module
import sqlite3

# database connection
conn = sqlite3.connect("student.db")

# delete query
delete = "DELETE FROM student WHERE s_id=2" 

# execute delete query
conn.execute(delete)

# save changes(commit)
conn.commit()

# close connection
conn.close()
