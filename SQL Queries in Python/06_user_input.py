# This program is vulnerable to SQL Injection
# https://xkcd.com/327/

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
    
    query_string = 'SELECT * FROM employee WHERE salary >= ' + str( min_salary) + ' ORDER BY salary'
    print()
    print(query_string)
    print()
    cursor.execute(query_string)

    row = cursor.fetchone()
    while row:
        for each in row:
            #print(each, end=" ")
            print(each)
        print()
        row = cursor.fetchone()

except psycopg2.Error as err:
    print("PostgreSQL Error: %s" % err.args[0])
    sys.exit(-1)
finally:
    if conn:
        conn.close()
