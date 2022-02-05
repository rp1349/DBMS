# Queries the company database for all employees, fetches all of the results at once

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
    
    # Retrieve metadata
    # columns = cursor.description
    # print(columns)
    
    rows = cursor.fetchall()   # easy, but dangerous (the query results might not fit in memory)
    for row in rows:
        print(row)

except psycopg2.Error as err:
    print("PostgreSQL Error: %s" % err.args[0])
    sys.exit(-1)
finally:
    if conn:
        conn.close()
