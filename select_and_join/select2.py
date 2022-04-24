import sqlite3
import os

db = "sims.db"

# Delete the database of it exists
if os.path.isfile(db):
    os.remove(db)

# Connect to the database
conn = sqlite3.connect(db)

# A script can contain more than one SQL statement
script = """
CREATE TABLE students (
    id int,
    name varchar(255) not null,
    age int not null,
    year int not null,
    primary key (id)
);

CREATE TABLE teachers (
    id int,
    salutation varchar(255) not null,
    name varchar(255) not null,
    subject varchar(255) not null,
    primary key (id)
);

CREATE TABLE teaches (
    id        int,
    teacherid int not null,
    studentid int not null,
    primary key(id),
    foreign key(teacherid) references teachers(id),
    foreign key(studentid) references students(id)
);
"""

conn.executescript(script)

# This is data to insert into the database
students = """
ID  Name    Age Year
1   Jane    13  10
2   Fred    14  11
3   George  13  10
4   Sam     15  12
5   Bill    13  10
6   Olivia  15  12
7   Susan   15  11
"""

teachers = """
ID  Salutation  Name    Subject
1   Mr          Smith   Geography
2   Ms          Jones   CompSci
3   Dr          Lambert History
4   Dr          Holland Music
5   Mr          Rolfe   Maths
6   Miss        Wareham Maths
"""

teaches = """
ID  StudentID   TeacherID
1   1           5
2   3           5
3   5           3
4   1           3
5   7           2
6   2           2
"""

for line in students.splitlines()[2:]:
    id, name, age, year = line.split()
    # Create a statement and execute it
    stmt = (
        f"INSERT INTO students (id,name,age,year) VALUES ({id},'{name}',{age},{year})"
    )
    conn.execute(stmt)

for line in teachers.splitlines()[2:]:
    id, salutation, name, subject = line.split()
    stmt = f"INSERT INTO teachers (id,salutation,name,subject) VALUES ({id},'{salutation}','{name}','{subject}')"
    conn.execute(stmt)

for line in teaches.splitlines()[2:]:
    id, studentid, teacherid = line.split()
    stmt = f"INSERT INTO teaches (id,studentid,teacherid) VALUES ({id},{studentid},{teacherid})"
    conn.execute(stmt)

conn.commit()

age = input("Enter Age: ")

# A select statement which includes a join
query = f"""SELECT students.name, teachers.name, teachers.salutation
  FROM students
  INNER JOIN teaches ON students.ID = teaches.StudentID
  INNER JOIN teachers ON teaches.TeacherID = teachers.ID
  WHERE students.age = {age}
  ORDER BY students.name;"""

results = conn.execute(query)

for sname, tname, salutation in results:
    print(f"For {age} year-old students, {salutation} {tname} teaches {sname}")

# Remove this line to complete the exercise
# quit()

# Write a statement to alter the table structure to add a 'Postcode' field which is 10 characters

stmt = "ALTER TABLE students ADD Postcode varchar(10)"

conn.execute(stmt)

students = """
ID  Postcode
1   CB1 9XJ
2   CB2 5HD
3   CB20 4PS
4   PE19 3XR
5   CO9 2AQ
6   IP4 7DP
7   PE25 8SC
"""

for line in students.splitlines()[2:]:
    id, postcode1, postcode2 = line.split()
    # Create an update statement to set the postcode
    stmt = f"UPDATE students SET Postcode = '{postcode1} {postcode2}' WHERE ID={id}"
    conn.execute(stmt)

conn.commit()
quit()
# George leaves. Delete their record.
stmt = "DELETE FROM Student WHERE name = 'George';"

conn.execute(stmt)

query = f"""SELECT students.postcode, students.name, teachers.name, teachers.salutation
  FROM students
  INNER JOIN teaches ON students.ID = teaches.StudentID
  INNER JOIN teachers ON teachers.ID = teaches.TeacherID
  ORDER BY students.name DESC;"""

results = conn.execute(query)

for spcode, sname, tname, salutation in results:
    print(f"{salutation} {tname} teacher student {sname} who lives at {spcode}")

conn.close()
