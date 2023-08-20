#3. Create SQLite Database and Perform Operations on Tables

import sqlite3
try:
    conn = sqlite3.connect('test1.db')
    print("Opened database successfully");
    cur=conn.cursor()

    #Creating Table
    """conn.execute('''CREATE TABLE STUDENT
    (ROLLNO INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,SEMESTER INT,PERCENTAGE REAL);''')"""
    #print("Student Table Created...")
    """conn.execute("INSERT INTO STUDENT (ROLLNO,NAME,SEMESTER,PERCENTAGE) VALUES(1, 'ABC', 2, 70.50 )");
    conn.execute("INSERT INTO STUDENT (ROLLNO,NAME,SEMESTER,PERCENTAGE) VALUES(2, 'XYZ', 3, 75.50 )");
    conn.execute("INSERT INTO STUDENT (ROLLNO,NAME,SEMESTER,PERCENTAGE) VALUES(3, 'MPO', 2, 70.50 )");
    #print("Student Data Inserted...")
    print ("Total number of rows inserted :", conn.total_changes)"""
   
    conn.commit()
    query="SELECT ROLLNO, NAME, SEMESTER, PERCENTAGE from STUDENT"
    cur.execute(query)
    result=cur.fetchall()
    print("Table Contents.....")
    for row in result:
        print ("ROLLNO = ", row[0])
        print ("NAME = ", row[1])
        print ("SEMESTER = ", row[2])
        print ("PERCENTAGE = ", row[3], "\n")
    query1="UPDATE STUDENT set PERCENTAGE = 80.60 where ROLLNO = 1"
    cur.execute(query1)
    conn.commit()
    print ("Total number of rows updated :", conn.total_changes)
    query2="DELETE from STUDENT where ROLLNO = 2"
    cur.execute(query2)
    conn.commit()
    print ("Total number of rows deleted :", conn.total_changes)

except DatabaseError:
    print('Connection Error')
finally :
    conn.close()