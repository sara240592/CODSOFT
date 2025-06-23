import json
import os

CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added.")

# View contact list
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

# Search contact
def search_contact(contacts):
    keyword = input("Enter name or phone to search: ")
    results = [c for c in contacts if keyword.lower() in c['name'].lower() or keyword in c['phone']]
    if results:
        for c in results:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
    else:
        print("Contact not found.")

# Update contact
def update_contact(contacts):
    name = input("Enter name to update: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            c["phone"] = input("New phone: ")
            c["email"] = input("New email: ")
            c["address"] = input("New address: ")
            print("Contact updated.")
            return
    print("Contact not found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            print("🗑️ Contact deleted.")
            return
    print("Contact not found.")

# Main menu loop
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        print("===========================")
        choice = input("Choose an option (1–6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
