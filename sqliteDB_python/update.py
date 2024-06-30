# import sqlite database module
import sqlite3

# database connection
conn = sqlite3.connect("student.db")

# update query
update = "UPDATE student SET s_name = 'Savita' WHERE s_id=1" 

# execute update query
conn.execute(update)

# save changes(commit)
conn.commit()

# close connection
conn.close()
