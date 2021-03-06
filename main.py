from flask import Flask, render_template, url_for, redirect
from data_manager import data_handler
from sql_query import sql_requests

app = Flask(__name__)


@app.route("/")
def root_page():
    """List the menu options, in the tuple block the second item define the url path."""
    menu_options = (("Mentors and schools page", "mentors"),
                    ("All school page", "all-school"),
                    ("Contacts page-m", "mentors-by-country"),
                    ("Contacts page-s", "contacts"),
                    ("Applicants page", "applicants"),
                    ("Applicants and mentors page", "applicants-and-mentors"))

    return render_template("main_page.html", menu=menu_options)


@app.route("/<page>/")
def questions(page=None):
    """Send a SQL query to data_manager, check if it's valid then return the data."""
    SQL = sql_requests(page)
    if SQL:
        result, header = data_handler(SQL)
        return render_template("answers.html", result=result, header=header)
    return redirect(url_for("root_page"))

if __name__ == "__main__":
    app.run()
