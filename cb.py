from typing import Dict
Contact = Dict[str, str]
ContactBook = Dict[str, Contact]
def add_contact(contacts: ContactBook) -> None:
    name = input("Name: ").strip()
    if name in contacts:
        print("Contact already exists\n")
        return
    contacts[name] = {
        "phone": input("Phone: ").strip(),
        "email": input("Email: ").strip(),
        "address": input("Address: ").strip(),
    }
    print("Contact added successfully\n")
def view_contacts(contacts: ContactBook) -> None:
    if not contacts:
        print("No contacts found\n")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"- {name} | {info['phone']}")
    print()
def search_contact(contacts: ContactBook) -> None:
    keyword = input("Search by name or phone: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if keyword in name.lower() or keyword in info["phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("No matching contact found\n")
    else:
        print()
def update_contact(contacts: ContactBook) -> None:
    name = input("Enter contact name to update: ").strip()
    if name not in contacts:
        print("Contact not found\n")
        return
    contact = contacts[name]
    contact["phone"] = input(f"Phone ({contact['phone']}): ").strip() or contact["phone"]
    contact["email"] = input(f"Email ({contact['email']}): ").strip() or contact["email"]
    contact["address"] = input(f"Address ({contact['address']}): ").strip() or contact["address"]
    print("Contact updated successfully\n")
def delete_contact(contacts: ContactBook) -> None:
    name = input("Enter contact name to delete: ").strip()
    if name not in contacts:
        print("Contact not found\n")
        return
    del contacts[name]
    print("Contact deleted successfully\n")
def display_menu() -> None:
    print("Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def main() -> None:
    contacts: ContactBook = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")
if __name__ == "__main__":
    main()
