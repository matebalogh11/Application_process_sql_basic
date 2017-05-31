from data_manager import data_handler
from sys import exit
from os import system

# This module is for import only!


def main_menu():
    """Print out the options panel connects to the database trough data_handler"""
    menu_options = {1: "Name of the mentors", 2: "Nicknames for mentors from Miskolc", 3: "Carol Something + phone",
                    4: "Girl from Adipiscingenimmi University", 5: "New student Markus",
                    6: "Phone number change for Jemima", 7: "Students who canceled  the application"}
    print("\nMain menu:\nPlease select a question.\n")
    for i, menu in enumerate(menu_options, start=1):
        print("{0}. {1}".format(i, menu_options.get(i)))
    print("0. Press 0 to exit.")

    selected_q = int(input("\nSelected question: \n"))
    if not selected_q:
        print("Exiting...")
        exit()
    fetched_data = data_handler(selected_q)
    return fetched_data, selected_q


def data_coordinator():
    """Handle errors, fetch the data table and send it to print_row"""
    try:
        system("clear")
        result, selected_q = main_menu()
        print_row(selected_q, result)
    except ValueError:
        print("Please add a valid number for menu option!")
        input("Press Enter to continue.")


def print_row(q_number, result):
    """Print out the chosen data from the database in a pretty way"""
    system("clear")
    header_row = {1: ["firs_name", "last_name"], 2: ["nick_name"], 3: ["full_name", "phone_number"],
                  4: ["phone_number"], 5: ["id", "firs_name", "last_name", "phone_number", "email", "application_code"]}

    paired_dict = {1: 1, 2: 2, 3: 3, 4: 3, 5: 5, 6: 4, 7: 5}
    columns = [column for column in header_row.get(paired_dict[q_number])]
    print("\n")
    if len(columns) < 5:
        print(("{}     " * len(columns)).format(*columns))
        print("-"*len(columns*14))
    else:
        padding = 38 if q_number == 7 else 20
        print("{:<2}  {:>12}  {:>10}  {:>16}  {:>{x}}  {:>20}".format(*columns, x=padding))
        print("-"*len(columns*18))

    for row in result:
        if len(row) == 1:
            print("{}".format(row[0]))
        elif len(row) == 2:
            print("{0:<12}   {w:<10}".format(row[0], w=row[1]))
        else:
            padding = 46 if q_number == 7 else 26
            print(("{:<2}   {:>10}   {:>10}   {:>10}   {:>{x}}   {:>10}").format(
                row[0], row[1], row[2], row[3], row[4], row[5], x=padding))
    input("\nPlease press Enter to continue")


