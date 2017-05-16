from data_manager import data_handler


def main_menu():

    print("Main menu:\nPlease select a question.\n")
    for menu in range(1, 8):
        print("{0}. Question {0}".format(menu))
    selected_q = int(input("\nSelected question: "))
    return selected_q


def console_app():

    selected_q = main_menu()
    fetched_data = data_handler(selected_q)
    return fetched_data


def print_out_data():

    result = console_app()
    for row in result:
        print(row[0], row[1])