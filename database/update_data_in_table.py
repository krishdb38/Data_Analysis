"""
The following example updates the title of a book specified by a book id
"""

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def update_book(book_id, title):
    # read database configuration
    db_config = read_db_config()

    # Prepare query and data
    query = """ UPDATE books SET\
        title = %s\
        WHERE id = %s"""

    data = (title, book_id)
    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)
        
        # accept the changes
        conn.commit()

    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    update_book(37,"This book is written by krish")
