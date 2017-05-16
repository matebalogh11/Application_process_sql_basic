from data_manager import data_handler
import sys


def main_menu():

    print("\nMain menu:\nPlease select a question.\n")
    for menu in range(1, 8):
        print("{0}. Question {0}".format(menu))
    print("8. Press 0 to exit.")

    selected_q = int(input("\nSelected question: \n"))
    if not selected_q:
        sys.exit()

    fetched_data = data_handler(selected_q)
    return fetched_data


def print_out_data():

    result = main_menu()
    for row in result:
        if len(row) == 1:
            print(row[0])
        elif len(row) == 2:
            print(row[0], row[1])
        else:
            print(row[0], row[1], row[2], row[3], row[4], row[5])
