#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Example of creating a table and inserting values

import psycopg2  
import psycopg2.extras  # needed for dictionary cursor
import sys

conn = None
try:
    conn = psycopg2.connect(user="postgres",  # same as pgAdmin
                            password="5436",  # same as pgAdmin
                            host="127.0.0.1",
                            port="5432",
                            database="Company")  # same as the name of the 
                                                 # marina database in pgAdmin
    
    # use a dictionary to access results by column name instead of 
    # column number
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # create new table for contracts
    cursor.execute("DROP TABLE IF EXISTS contract")
    
    # NOTE: postgres uses the keyword 'SERIAL' instead of 'AUTOINCREMENT'
    create_string = """CREATE TABLE emp_contact_info (
                       ssn     VARCHAR(50) NOT NULL,
                       phone   VARCHAR(50) NOT NULL,
                       email   VARCHAR(50) NOT NULL,
                       PRIMARY KEY(ssn) 
                       )"""
    cursor.execute(create_string)

    # insert contracts 
    new_contracts = (('888665555', '662.567.8059', 'keds@gmail.com'),
                     ('987654321', '205.648.3339', 'ocean@yahoo.com'),
                     ('987987987', '901.978.3989', 'coffee@gmail.com'))
                    
    # postgres uses %s instead of ? as a placeholder
    insert_string = "INSERT INTO emp_contact_info(ssn, phone, email) VALUES (%s, %s, %s)"
    cursor.executemany(insert_string, new_contracts)
    conn.commit()  # save changes to the table

    # are they in the table?
    cursor.execute("SELECT * FROM emp_contact_info")
    row = cursor.fetchone()
    while row:
        print(row["ssn"], row["phone"], row["email"])
        row = cursor.fetchone()

except psycopg2.Error as err:
    if conn:
        conn.rollback()  # reverse any changes before the commit

    print("PostgreSQL Error: %s" % err.args[0])
    sys.exit(-1)
finally:
    if conn:
        conn.close()


# In[ ]:




