import psycopg2


def data_handler(query):

    options = {1: """SELECT first_name, last_name FROM mentors"""}

    try:
        connection_str = "dbname='bmate11' user='bmate11' host='localhost' password='3dc41885'"
        conn = psycopg2.connect(connection_str)
        cursor = conn.cursor()
        cursor.execute(options[query])
        rows = cursor.fetchall()
        return rows
    except:
        print("Uh oh..we cannot connect to your database.")