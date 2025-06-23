import json
import os

CONTACTS_DATA_FILE = 'contacts.json' # Renamed for clarity

# Load contacts from file
def retrieve_contacts(): # Renamed function
    """
    Loads contact data from the JSON file.
    Returns an empty list if the file does not exist.
    """
    if os.path.exists(CONTACTS_DATA_FILE):
        with open(CONTACTS_DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Save contacts to file
def store_contacts(contact_list): # Renamed function and parameter
    """
    Saves the current list of contacts to the JSON file.
    """
    with open(CONTACTS_DATA_FILE, 'w') as f:
        json.dump(contact_list, f, indent=4)

# Add new contact
def create_contact(contact_list): # Renamed function and parameter
    """
    Prompts the user for new contact details (name, phone, email, address)
    and adds them to the contact list.
    """
    contact_name = input("Name: ")
    contact_phone = input("Phone: ")
    contact_email = input("Email: ")
    contact_address = input("Address: ")
    
    contact_list.append({
        "name": contact_name,
        "phone": contact_phone,
        "email": contact_email,
        "address": contact_address
    })
    print("Contact added.")

# View contact list
def display_contacts(contact_list): # Renamed function and parameter
    """
    Displays all contacts currently stored in the list.
    """
    if not contact_list:
        print("No contacts found.")
        return
    for index, contact_info in enumerate(contact_list, 1): # Renamed loop variables
        print(f"{index}. {contact_info['name']} - {contact_info['phone']}")

# Search contact
def find_contact(contact_list): # Renamed function and parameter
    """
    Prompts the user for a keyword (name or phone) and displays matching contacts.
    """
    search_keyword = input("Enter name or phone to search: ") # Renamed variable
    search_results = [
        contact_item for contact_item in contact_list 
        if search_keyword.lower() in contact_item['name'].lower() or search_keyword in contact_item['phone']
    ] # Renamed list comprehension variable
    
    if search_results:
        for found_contact in search_results: # Renamed loop variable
            print(f"\nName: {found_contact['name']}\nPhone: {found_contact['phone']}\nEmail: {found_contact['email']}\nAddress: {found_contact['address']}")
    else:
        print("Contact not found.")

# Update contact
def modify_contact(contact_list): # Renamed function and parameter
    """
    Prompts the user for a contact name to update and allows modification
    of their phone, email, and address.
    """
    name_to_update = input("Enter name to update: ") # Renamed variable
    for contact_entry in contact_list: # Renamed loop variable
        if contact_entry["name"].lower() == name_to_update.lower():
            contact_entry["phone"] = input("New phone: ")
            contact_entry["email"] = input("New email: ")
            contact_entry["address"] = input("New address: ")
            print("Contact updated.")
            return
    print("Contact not found.")

# Delete contact
def remove_contact(contact_list): # Renamed function and parameter
    """
    Prompts the user for a contact name to delete and removes it from the list.
    """
    name_to_delete = input("Enter name to delete: ") # Renamed variable
    for contact_item in contact_list: # Renamed loop variable
        if contact_item["name"].lower() == name_to_delete.lower():
            contact_list.remove(contact_item)
            print("🗑️ Contact deleted.")
            return
    print("Contact not found.")

# Main menu loop
def run_contact_book(): # Renamed function
    """
    The main function to run the contact book application,
    handling user interaction and menu navigation.
    """
    all_contacts = retrieve_contacts() # Renamed variable
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        print("===========================")
        user_choice = input("Choose an option (1–6): ") # Renamed variable

        if user_choice == "1":
            create_contact(all_contacts)
        elif user_choice == "2":
            display_contacts(all_contacts)
        elif user_choice == "3":
            find_contact(all_contacts)
        elif user_choice == "4":
            modify_contact(all_contacts)
        elif user_choice == "5":
            remove_contact(all_contacts)
        elif user_choice == "6":
            store_contacts(all_contacts) # Call the renamed save function
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run_contact_book() # Call the renamed main function
