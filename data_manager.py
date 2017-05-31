import psycopg2
from login import DB, USER, HOST, PW

# This module is for import only!


def data_handler(SQL):
    """Connect to the selected database and gather the requested data"""

    try:
        connection_str = "dbname='{}' user='{}' host='{}' password='{}'".format(DB, USER, HOST, PW)
        conn = psycopg2.connect(connection_str)
        cursor = conn.cursor()
        cursor.execute(SQL)
        result = cursor.fetchall()
        header = [desc[0] for desc in cursor.description]
        return result, header
    except Exception:
        print("Uh oh.. cannot connect to the database")
    finally:
        if conn:
            conn.close()