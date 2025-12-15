# import mysql.connector as coco
# conn = coco.connect(
#     host="localhost",
#     user="root",
#     password="0786",
#     database="hero"
# )

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     age INT
# )
# """)
# conn.commit

# query = "INSERT INTO students (name, age) VALUES (%s, %s)"
# values = [("Tanzeem", 22), ("Ayesha", 20)]

# cursor.executemany(query, values)
# conn.commit()

# print(cursor.rowcount, "record(s) inserted.")
# cursor.close()
# conn.close()

# cursor = conn.cursor()

# cursor.execute(''' 
# create table studentmarks(
#                id int,
#                student_id int references students(id),
#                subject varchar(100),
#                marks int
#                )
# ''')
# conn.commit()


# tan = conn.cursor()

# tan.execute('''
# create table lala (
#         name varchar(50),
#             id int ,
#             class varchar (50),
#             lala int
#                 )
# ''')
# conn.commit()

# import mysql.connector as nice

# con = nice.connect(
#     host='localhost',
#     user='root',
#     password='0786',
#     database='pythondatabase'
# )

# print(con)

# quary = con.cursor()
# quary.execute('drop database juju')
# quary.execute("create database pythondatabase")

# quary.execute('''
# create table python (
#               id int auto_increment primary key,
#               name varchar(100),
#               branch varchar(50)
#               )
# ''')

# con.commit()
# quary = con.cursor()
# v = 'insert into python(name,branch) values (%s,%s)'
# value = [('tanzeem','it')]
# quary.executemany(v, value)
# con.commit()

# quary = con.cursor()
# quary.execute('show tables')

# for i in quary.fetchall():
#     print(i)

import mysql.connector as cnect 

conn = cnect.connect(
    host= 'localhost',
    user= 'root',
    password='0786',
    database= 'pythondatabase'

)

print("entre in database")

cursor = conn.cursor()
# cursor.execute('show tables')

# for i in cursor.fetchall():
#     print(i)

# insert_record = ('insert into python(name,branch) values(%s,%s)')
# insert_values = [('zaid','farmer')]
# cursor.executemany(insert_record,insert_values)
# conn.commit()
# print("inserted")
cursor.execute("""select * from python 
               order by name desc""")
for row in cursor.fetchall():
    print(row) 
    

