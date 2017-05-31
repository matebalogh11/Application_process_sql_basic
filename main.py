from flask import Flask, render_template, url_for
from data_manager import data_handler

app = Flask(__name__)


@app.route("/")
def root_page():
    menu_options = [("Mentors and schools page", "mentors")]

    return render_template("main_page.html", menu=menu_options)


@app.route("/mentors")
def mentors():
    SQL = """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
             FROM mentors
             LEFT JOIN schools USING (city)
             ORDER BY mentors.id;"""
    result, header = data_handler(SQL)
    return render_template("answers.html", result=result, header=header)

if __name__ == "__main__":
    app.run(debug=True)


#   ("All school page", "all-school"),
#   ("Contacts page-m", "mentors-by-country"),
#   ("Contacts page-s", "contacts"), ("Applicants page", "applicants"),
#   ("Applicants and mentors page", "applicants-and-mentors")