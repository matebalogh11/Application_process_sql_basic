from data_manager import data_handler


def main_menu():

    print("Main menu:\nPlease select a question.\n")
    for menu in range(1, 8):
        print("{0}. Question {0}".format(menu))

    selected_q = int(input("\nSelected question: "))
    fetched_data = data_handler(selected_q)
    return fetched_data


def print_out_data():

    result = main_menu()
    for row in result:
        if len(row) == 2:
            print(row[0], row[1])
        else:
            print(row[0])
