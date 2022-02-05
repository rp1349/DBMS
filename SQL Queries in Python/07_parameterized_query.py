# This program is NOT vulnerable to SQL Injection
#
#
# In other programming languages "parameterized queries" are often called
# "prepared statements".

import psycopg2  
import psycopg2.extras  # needed for dictionary cursor
import sys

min_salary = input("What is the minimum salary you would like in the results? ")

conn = None
try:
    conn = psycopg2.connect(user="postgres",  # same as pgAdmin
                            password="password",  # same as pgAdmin
                            host="127.0.0.1",
                            port="5432",
                            database="company")  # same as the name of the 
                                                 # company database in pgAdmin
    
    # use a dictionary to access results by column name instead of 
    # column number
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # parameters for SQL query should be a tuple
    parameters = (min_salary, )
    
    # postgres uses %s instead of ? as a placeholder
    query_string = 'SELECT * FROM employee WHERE salary >= %s ORDER BY salary'
    print()
    print(query_string)
    print()
    cursor.execute(query_string, parameters)

    row = cursor.fetchone()
    while row:
        for each in row:
            print(each)
        print()
        row = cursor.fetchone()

except psycopg2.Error as err:
    print("PostgreSQL Error: %s" % err.args[0])
    sys.exit(-1)
finally:
    if conn:
        conn.close()
