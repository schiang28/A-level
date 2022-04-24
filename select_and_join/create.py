import sqlite3

conn = sqlite3.connect("test.db")

print("Opened database successfully")

stmt = """CREATE TABLE IF NOT EXISTS COMPANY
        (ID INT PRIMARY KEY,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);"""

conn.execute(stmt)

print("Table created successfully")

conn.close()
