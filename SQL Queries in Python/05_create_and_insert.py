# Example of creating a table and inserting values

import psycopg2  
import psycopg2.extras  # needed for dictionary cursor
import sys

conn = None
try:
    conn = psycopg2.connect(user="postgres",  # same as pgAdmin
                            password="password",  # same as pgAdmin
                            host="127.0.0.1",
                            port="5432",
                            database="company")  # same as the name of the 
                                                 # marina database in pgAdmin
    
    # use a dictionary to access results by column name instead of 
    # column number
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # create new table for contracts
    cursor.execute("DROP TABLE IF EXISTS contract")
    
    # NOTE: postgres uses the keyword 'SERIAL' instead of 'AUTOINCREMENT'
    create_string = """CREATE TABLE contract (
                       contract_id   SERIAL,
                       other_party   VARCHAR(50) NOT NULL,
                       date_signed   DATE NOT NULL,
                       PRIMARY KEY(contract_id) 
                       )"""
    cursor.execute(create_string)

    # insert contracts 
    new_contracts = (('FedEx', '2020-03-14'),
                     ('Amazon', '2020-05-24'),
                     ('NBC', '2020-05-25'))
                    
    # postgres uses %s instead of ? as a placeholder
    insert_string = "INSERT INTO contract(other_party, date_signed) VALUES (%s, %s)"
    cursor.executemany(insert_string, new_contracts)
    conn.commit()  # save changes to the table

    # are they in the table?
    cursor.execute("SELECT * FROM contract")
    row = cursor.fetchone()
    while row:
        print(row["contract_id"], row["other_party"], row["date_signed"])
        row = cursor.fetchone()

except psycopg2.Error as err:
    if conn:
        conn.rollback()  # reverse any changes before the commit

    print("PostgreSQL Error: %s" % err.args[0])
    sys.exit(-1)
finally:
    if conn:
        conn.close()
