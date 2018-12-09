import pymysql
db = pymysql.connect("localhost","root","","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


sql = "SELECT * FROM EMPLOYEE"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      gender = row[3]
      income = row[4]
      # Now print fetched result
      print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
         (fname, lname, age, gender, income ))
except:
   print ("Error: unable to fetch data")

# disconnect from server
db.close()