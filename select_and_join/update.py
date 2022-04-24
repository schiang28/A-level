import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")

stmt = "UPDATE COMPANY set SALARY = 25000.00 WHERE NAME='Mark';"
conn.execute(stmt)

stmt = "UPDATE COMPANY set SALARY = 90000.00 WHERE NAME = 'Teddy';"
conn.execute(stmt)

conn.commit()

print("Total number of rows updated :", conn.total_changes)
conn.close()
