# Queries the company database for all employees, fetches results one row at a time
#
# Practice:
#    1) Print the department name, not the department number; Sort output by employee's last name
#    2) Print the department name along with the number of employees in that department
#

import psycopg2  
import psycopg2.extras  # needed for dictionary cursor
import sys

conn = None
try:
    conn = psycopg2.connect(user="postgres",  # same as pgAdmin
                            password="postgresSU4!",  # same as pgAdmin
                            host="127.0.0.1",
                            port="5432",
                            database="company")  # same as the name of the 
                                                 # company database in pgAdmin
    
    # use a dictionary to access results by column name instead of 
    # column number
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cursor.execute("SELECT * FROM employee")

    row = cursor.fetchone()
    while row:
        print(row["ssn"], row["fname"], row["lname"], row["dno"])
        row = cursor.fetchone()

except psycopg2.Error as err:
    print("PostgreSQL Error: %s" % err.args[0])
    sys.exit(-1)
finally:
    if conn:
        conn.close()
