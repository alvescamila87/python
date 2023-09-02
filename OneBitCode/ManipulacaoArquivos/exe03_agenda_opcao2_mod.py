from exe03_agenda_opcao2 import *

def main():
    while True:
        print("\nContacts book")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete contacts")
        print("4. Exit")

        choice = int(input("Select an option (1-4): \n "))
        if choice == 1:
            add_contacts()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            delete_contacts()
        elif choice == 4:
            break
        else:
            print("Type any option listed!")

main()