#
# from https://pynative.com/python-postgresql-tutorial/
#

# see the above web page for instructions on installing the psycopg2 module (API)
import psycopg2  

try:
    connection = psycopg2.connect(user="postgres",  # same as pgAdmin
                                  password="postgresSU4!",  # same as pgAdmin
                                  host="127.0.0.1",
                                  port="5432",
                                  database="company")  # same as the name of the 
                                                       # company database in pgAdmin

    cursor = connection.cursor()
    
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
