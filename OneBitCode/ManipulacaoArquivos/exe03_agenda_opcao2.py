# Agenda de contatos - Opção 2

import os

def add_contacts():
    name = str(input("Type a contact name: ")).capitalize().strip()
    address = str(input((f"Type the {name}'s address: ")))
    phone = str(input(f"Type the {name}'s phone: "))

    contact = f"Name: {name} \nAddress: {address} \nPhone: {phone}\n"

    with open("ArquivosAulas/exe03_contacts.txt", "a", encoding='utf-8') as file:
        file.write(contact)

def view_contacts():
    local = 'ArquivosAulas/exe03_contacts.txt'
    if not os.path.exists(local):
        print("The contact list is empty!")
        return
    with open("ArquivosAulas/exe03_contacts.txt", "r", encoding='utf-8') as file:
        contacts = file.read()
    print("Contacts list")
    print(contacts)

def delete_contacts():
    local = 'ArquivosAulas/exe03_contacts.txt'
    if not os.path.exists(local):
        print("The contact list is empty!")
        return
    with open("ArquivosAulas/exe03_contacts.txt", "w", encoding='utf-8') as file:
        file.write("")

    print("Contacts removed success!")
