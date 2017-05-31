from flask import Flask, render_template, url_for, redirect
from data_manager import data_handler
from sql_query import sql_requests

app = Flask(__name__)


@app.route("/", defaults={'path': ''})
@app.route("/<path:path>")
def root_page(path):
    """Central coordinator/url-catcher"""
    if path and path != "favicon.ico":
        SQL = sql_requests(path)
        result, header = data_handler(SQL)
        return render_template("answers.html", result=result, header=header)
    else:
        menu_options = (("Mentors and schools page", "mentors"),
                        ("All school page", "all-school"),
                        ("Contacts page-m", "mentors-by-country"),
                        ("Contacts page-s", "contacts"),
                        ("Applicants page", "applicants"),
                        ("Applicants and mentors page", "applicants-and-mentors"))

        return render_template("main_page.html", menu=menu_options)


if __name__ == "__main__":
    app.run(debug=True)
