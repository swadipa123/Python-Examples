import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO employee(FIRST_NAME,
   LAST_NAME, AGE, GENDER, INCOME)
   VALUES ('Mac1', 'Mohan1', 201, 'M', 2000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()