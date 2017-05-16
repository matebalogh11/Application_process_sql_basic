import psycopg2


def data_handler(query):

    options = {1: """SELECT first_name, last_name FROM mentors;""",
               2: """SELECT nick_name FROM mentors WHERE city='Miskolc';""",
               3: """SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                     WHERE first_name = 'Carol';""",
               4: """SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                     WHERE email LIKE '%@adipiscingenimmi.edu';""",
               5: """INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                     VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com',54823);
                     SELECT * FROM applicants WHERE application_code = 54823;""",
               6: """UPDATE applicants SET phone_number = '003670/223-7459' WHERE first_name = 'Jemima' AND last_name = 'Foreman';
                     SELECT * FROM applicants WHERE application_code = 58324;""",
               7: """DELETE FROM applicants WHERE email LIKE '%mauriseu.net'; SELECT * FROM applicants;"""}

    try:
        connection_str = "dbname='bmate11' user='bmate11' host='localhost' password='3dc41885'"
        conn = psycopg2.connect(connection_str)
        #  conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(options[query])
        rows = cursor.fetchall()
        return rows
    except:
        print("Uh oh..we cannot connect to your database.")
