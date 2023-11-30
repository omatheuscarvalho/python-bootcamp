import os

def insert_list(listt):
    os.system('cls clear')
    item = input("Type a value to add in the list: ")
    listt.append(item)
def delete_item_list(listt):
    os.system('cls clear')
    try:
        index = int(input("Type the index to delete: "))
        del listt[index]
    except (IndexError, ValueError):
        print("Invalid index. Please enter a valid index.")
def list_list(listt):
    os.system('cls clear')
    if len(listt) == 0: 
        print("Empty List! ")
        return
    for index, item in enumerate(listt):
        print(index, item)

def menu(listt):
    try:
        print("Select an option: ")
        option = input("[i]nsert [d]elete [l]ist: ").lower()

        if option == 'i':
            insert_list(listt)
        elif option == 'd':
            delete_item_list(listt)
        elif option == 'l':
            list_list(listt)
        else:
            print("Invalid option. Please select a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    new_list = []
    while True:
        menu(new_list)
        #os.system('cls clear')
        #option = input("Enter c to cancel: ")
        #if option.lower() == 'c': break 
main()