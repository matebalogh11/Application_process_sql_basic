import psycopg2


def data_handler(query):

    options = {1: """SELECT first_name, last_name FROM mentors""",
               2: """SELECT nick_name FROM mentors WHERE city='Miskolc'""",
               3: """SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM applicants"""}

    try:
        connection_str = "dbname='bmate11' user='bmate11' host='localhost' password='3dc41885'"
        conn = psycopg2.connect(connection_str)
        cursor = conn.cursor()
        cursor.execute(options[query])
        rows = cursor.fetchall()
        return rows
    except:
        print("Uh oh..we cannot connect to your database.")