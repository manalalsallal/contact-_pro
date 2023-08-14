
import json


con = 'contact.json'
def load_contacts():
    try:
        with open(con) as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts



def store_json_data(contacts):
    with open(con, 'w') as file:
         json.dump(contacts, file , indent=4)



def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    store_json_data(contacts)
    print("Contact created successfully.")

def display_contact():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contacts):
            print(f"#{idx+1}: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")



def update_contact():
    contact_id = int(input("Enter the contact ID to update: "))
    if contact_id <= 0 or contact_id > len(contacts):
        print("Invalid contact ID.")
        return

    contact = contacts[contact_id - 1]
    print("Current contact details:")
    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    name = input("Enter the new name: ")
    phone = input("Enter the new phone number : ")
    email = input("Enter the new email address: ")

    contact['name'] = name if name else contact['name']
    contact['phone'] = phone if phone else contact['phone']
    contact['email'] = email if email else contact['email']
    store_json_data(contacts)
    print("Contact updated successfully.")



def delete_contact():
    contact_id = int(input("Enter the contact ID to delete: "))
    if contact_id <= 0 or contact_id > len(contacts):
        print("Invalid contact ID.")
        return

    del contacts[contact_id - 1]
    store_json_data(contacts)
    print("Contact deleted successfully.")



def search_contact():
       
        if contacts:
            search_term = input("Enter a name or phone number to search: ")
            found_contacts = []
            for contact in contacts:
                if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                    found_contacts.append(contact)
            
            if found_contacts:
                print("Matching contacts:")
                for idx, contact in enumerate(found_contacts, start=1):
                    print(f"Contact {idx}:")
                    print(f"Name: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print()
            else:
                print("No matching contacts found.")
        else:
            print("No contacts found.")

contacts = load_contacts()

while True:
    choice=int(input('''
    1. Add new contact \n
    2. display contact \n
    3. search contact \n
    4. update contact \n
    5. Delet contact \n
    6. Exit \n
    enter your choice: '''))


    if choice == 1:
       add_contact()
        
    elif choice == 2:
       display_contact()

    elif choice == 3:
        search_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
       delete_contact() 
       
    else:
        break
