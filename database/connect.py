import mysql.connector
from mysql.connector import Error

def connect():
    """
    Connect to MySQl database
    """
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="python_mysql",
            user="root",
            password = "ubuntu"
        )
        if conn.is_connected():
            print("Connected Successfully")
    except Error as e:
        print(e)
    
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
if __name__ == "__main__":
    connect()