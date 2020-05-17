from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchone():
    try:
        dbconfig = read_db_config() # file returns parameter in dict
        conn = MySQLConnection(**dbconfig)  # pass dict
        cursor = conn.cursor()
        cursor.execute("Select * FROM books")

        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    query_with_fetchone()
