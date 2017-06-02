# This module is for import only!


def sql_requests(path):
    """Contain a list of predefined SQL querys, with the appropriate key return the related data."""

    SQL = {"mentors": """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                FROM mentors
                LEFT JOIN schools USING (city)
                ORDER BY mentors.id;""",
           "all-school": """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                FROM mentors
                RIGHT JOIN schools USING (city)
                ORDER BY mentors.id;""",
           "mentors-by-country": """SELECT COUNT(mentors.first_name) AS Mentors, schools.country
                FROM mentors
                LEFT JOIN schools USING (city)
                GROUP BY schools.country
                ORDER BY schools.country;""",
           "contacts": """SELECT schools.name, mentors.first_name, mentors.last_name
                FROM schools
                INNER JOIN mentors ON (schools.contact_person = mentors.id)
                ORDER BY schools.name;""",
           "applicants": """SELECT first_name, application_code, applicants_mentors.creation_date
                FROM applicants
                INNER JOIN applicants_mentors ON(applicants.id = applicants_mentors.applicant_id)
                WHERE applicants_mentors.creation_date > '20160101'
                ORDER BY applicants_mentors.creation_date DESC;""",
           "applicants-and-mentors": """SELECT  CONCAT(applicants.first_name, ' ', applicants.last_name) AS Applicant,
                applicants.application_code, mentors.nick_name
                FROM applicants
                LEFT JOIN applicants_mentors ON (applicants_mentors.applicant_id = applicants.id)
                LEFT JOIN mentors ON (applicants_mentors.mentor_id = mentors.id);
                """}

    return SQL.get(path)
