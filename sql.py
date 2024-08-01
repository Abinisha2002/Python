'''show connection object'''
# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire")
# print(connection)


'''create database'''
# import pymysql as mysql
# connection = mysql.connect(host="localhost",user="root",password="livewire")
# cursor=connection.cursor()
# cursor.execute("create database python19")


'''show databases'''

# import pymysql as  mysql
# conncetion=mysql.connect(host="localhost",user="root",password="livewire")
# cursor=conncetion.cursor()
# cursor.execute("show databases")
# for x in cursor:
#     print(x)


'''create table'''
# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="client1")
# cursor=connection.cursor()
# cursor.execute("create table student(department_id int primary key,department_name varchar(50))")
# cursor.execute("show tables")
# print("number of tables in databases:")
# for x in cursor:
#     print("\t",x)



# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="client1")
# cursor=connection.cursor()
# cursor.execute("create table employees(employee_id int primary key,employee_name varchar(50),department_id int)")
# cursor.execute("show tables")
# print("number of tables in databases:")
# for x in cursor:
#     print("\t",x)

'''row create'''
# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="client1")
# cursor=connection.cursor()
# s="insert into departments values(%s,%s)"
# t=(1,"abis")
# cursor.execute(s,t)
# connection.commit()
# print(cursor.rowcount,"new row inserted",cursor.lastrowid)

''' 2 row create'''
# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="python")
# cursor=connection.cursor()
# s="insert into student values(%s,%s)"
# t=[(2,"abis"),(3,"sumi")]
# cursor.executemany(s,t)
# connection.commit()
# print(cursor.rowcount,"new row inserted",cursor.lastrowid)



# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="client1")
# cursor=connection.cursor()
# cursor.execute("select * from student")
# result=cursor.fetchall()
# print("content in the python:")
# for x in result:
#     print("\t",x)


'''update'''
# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="client1")
# cursor=connection.cursor()
# sql="update employees set employee_name='bala' where employee_id=1;"
# cursor.execute(sql)
# connection.commit()


'''delete'''
# import pymysql as mysql
# connection=mysql.connect(host="localhost",user="root",password="livewire",database="client1")
# cursor=connection.cursor()
# sql="delete from employees where employee_id=1"
# cursor.execute(sql)
# connection.commit()
# print(cursor.rowcount,"record(s) deleted")



import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
# cursor.execute("create database client1")
cursor.execute("show databases")
for x in cursor:
    print(x)
cursor.execute("use client1")
# cursor.execute("create table student(department_id int primary key,department_name.varchar(50))")
cursor.execute("show tables")
print("number of tables in database:")
for x in cursor:
    print("\t",x) 
s="insert into student values(%s,%s)"
t=(2,"abar")
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid)
cursor.execute("select*from student")
result=cursor.fetchall()
print("content in the python:")
for x in result:
    print("\t",x)
sql="update student set department_name='abi' where department_id=1;"
cursor.execute(sql)
connection.commit()
sql="delete from student where department_id=1"
cursor.execute(sql)
connection.commit()
print(cursor.rowcount,"record(s) deleted")       







