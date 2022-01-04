import sqlite3 

a=sqlite3.connect('newdata.db')
a.execute('''CREATE TABLE IF NOT EXISTS STUDENT(NAME TEXT,AGE INT)''')
print("table created")

a.execute("insert into student(name,age) values('xyz',56)")

a.commit()
a.close()