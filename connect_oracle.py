import cx_Oracle
import pandas as pd

# TODO change path of Oracle Instant Client to yours
cx_Oracle.init_oracle_client(lib_dir = "/Users/enriquegrijalva/csc423/instantclient_19_8")

# TODO change credentials
# Connect as user "user" with password "mypass" to the "CSC423" service
# running on lawtech.law.miami.edu
connection = cx_Oracle.connect(
    "engrcsc423", "c05295", "lawtech.law.miami.edu/CSC_423")
cursor = connection.cursor()

#Display all Schedules
cursor.execute("""
    SELECT *
    FROM schedule
    """)

# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine

#Display the name of the tutor whose ID is 001
cursor.execute("""
    SELECT tutorName
    FROM TUTOR
    where tutorID = 001
    """)  

# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine

#Display the name of the student that had an enrollment confirmation number of 10201
cursor.execute("""
    SELECT s.stuName
    FROM student s
    join enrollment e on s.stuID = e.stuID
    where e.enrollNum = 10201
    """)  

# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine

#Display Mario Sanchez Phone Number
cursor.execute("""
    SELECT stuPhone
    FROM student 
    where stuName = 'Mario Sanchez'
    """)  

# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine

#Display the description of the course number 003
cursor.execute("""
    SELECT crsDescription
    FROM course 
    where crsNum = 0003
    """)  

# get column names from cursor
columns = [c[0] for c in cursor.description]
# fetch data
data = cursor.fetchall()
# bring data into a pandas dataframe for easy data transformation
df = pd.DataFrame(data, columns = columns)
print(df) # examine
