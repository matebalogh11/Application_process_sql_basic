from data_manager import data_handler
import sys
import os


def main_menu():

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
        sys.exit()
    fetched_data = data_handler(selected_q)
    return fetched_data, selected_q


def visualize_data():

    try:
        os.system("clear")
        result, selected_q = main_menu()
        print_row(selected_q, result)
    except ValueError:
        print("Please add a valid number for menu option!")
        input("Press Enter to continue.")


def print_row(q_number, result):

    os.system("clear")
    header_row = {1: ["firs_name", "last_name"], 2: ["nick_name"], 3: ["full_name", "phone_number"],
                  4: ["full_name", "phone_number"],
                  5: ["id", "firs_name", "last_name", "phone_number", "email", "application_code"],
                  6: ["phone_number"], 7: ["id", "firs_name", "last_name", "phone_number", "email", "application_code"]}
    columns = [column for column in header_row.get(q_number)]
    print("\n")
    print(("{}      "*len(columns)).format(*columns))
    print("-"*len(columns*16))

    for row in result:
        if len(row) == 1:
            print("{}".format(row[0]))
        elif len(row) == 2:
            print("{0:<12}   {w:<10}".format(row[0], w=row[1]))
        else:
            print(("{:<2}   {:>10}   {:>10}   {:>10}   {:>46}   {:>10}").format(
                   row[0], row[1], row[2], row[3], row[4], row[5]))
    input("\nPlease press Enter to continue")
