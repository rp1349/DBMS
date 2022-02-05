# Queries the company database for all employees, fetches results one row at a time
#
# Practice:
#    1) Add a header row before the query results
#    2) Sort the results by employee salary 
#

import psycopg2  
import sys

conn = None
try:
    conn = psycopg2.connect(user="postgres",  # same as pgAdmin
                            password="postgresSU4!",  # same as pgAdmin
                            host="127.0.0.1",
                            port="5432",
                            database="company")  # same as the name of the 
                                                 # company database in pgAdmin
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")

    row = cursor.fetchone()
    while row:
        print(row[0], row[1], row[2], row[3], row[7])
        row = cursor.fetchone()

except psycopg2.Error as err:
    print("PostgreSQL Error: %s" % err.args[0])
    sys.exit(-1)
finally:
    if conn:
        conn.close()
