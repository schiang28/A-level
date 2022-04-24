import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")

stmt = """INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
      VALUES ('Paul', 32, 'California', 20000.00 )"""

conn.execute(stmt)

stmt = """INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
      VALUES ('Allen', 25, 'Texas', 15000.00 )"""

conn.execute(stmt)

stmt = """INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) 
      VALUES ('Teddy', 23, 'Norway', 20000.00 )"""

conn.execute(stmt)

stmt = """INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
      VALUES ('Mark', 25, 'Richmond ', 65000.00 )"""

conn.execute(stmt)

stmt = """INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
      VALUES ('Sophie', 16, 'Cambridge', 15000.00 )"""

conn.execute(stmt)

conn.commit()
print("Records created successfully")
conn.close()
