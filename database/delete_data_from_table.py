"""To delete data from a table from a Python Program
3 Main steps:
connect
commit
and close """

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def delete_book(book_id):
    db_config = read_db_config()

    query = "DELETE FROM books WHERE id = %s"

    try:
        # connect to the database server
        conn = MySQLConnection(**db_config)

        # Execute the query
        cursor = conn.cursor()
        cursor.execute(query, (book_id,))
        
        # accept the change
        conn.commit()

    except Error as error:
        print("Error occurred", error)
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    delete_book(50)
