
# import sqlite3

# conn = sqlite3.connect("student.db")

# print("Connected")

# studentTableSchema = """
# CREATE TABLE IF NOT EXISTS students(
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# age  INTEGER NOT NULL
# )
# """

# conn.execute(studentTableSchema)

# conn.execute(
#     "INSERT INTO students(id,name,age) VALUES(?,?,?)",
#     (1,"MYA MYA",16)
# )

# conn.commit()



import sqlite3

conn = sqlite3.connect("school.db")

print("Connected")



studentschema = """
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER NOT NULL,
course_id INTEGER, 
FOREIGN KEY (course_id) REFERENCES courses(id)
)
"""

courses_schema = """
CREATE TABLE IF NOT EXISTS courses(
id  INTEGER PRIMARY KEY,
title TEXT NOT NULL
)
"""

conn.execute(studentschema)
conn.execute(courses_schema)
conn.commit()

# conn.execute(
#     "INSERT INTO courses(id,title) VALUES(?,?)",
#     (1,"PYTHON")
# )

# conn.execute(
#     "INSERT INTO courses(id,title) VALUES(?,?)",
#     (2,"DATA SCIENCE")
# )

# conn.execute(
#     "INSERT INTO courses(id,title) VALUES(?,?)",
#     (3,"WEB DEVELOPMENT")
# )

# conn.execute(
#     "INSERT INTO courses(id,title) VALUES(?,?)",
#     (4,"JAVA")
# )

# conn.execute(
#     "INSERT INTO courses(id,title) VALUES(?,?)",
#     (5,"JAVASCRIPT")
# )
# conn.commit()

# conn.execute(
#     "INSERT INTO students(id,name,age,course_id) VALUES(?,?,?,?)",
#     (1,"Alice",20,1)
# )

# conn.execute(
#     "INSERT INTO students(id,name,age,course_id) VALUES(?,?,?,?)",
#     (2,"Bob",22,None)
# )
# conn.commit()

