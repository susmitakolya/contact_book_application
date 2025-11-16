def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email},{address}\n")
    print(f"\n Contact '{name}' added successfully!\n")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("\n No contacts found.\n")
            return

        print("\n Contact List:")
        print("-" * 50)
        for line in contacts:
            name, phone, email, address = line.strip().split(",")
            print(f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}")
            print("-" * 50)
    except FileNotFoundError:
        print("\n No contacts file found. Add a contact first.\n")


def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False

    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email, address = line.strip().split(",")
                if search_name in name.lower():
                    print("\n Contact Found:")
                    print("-" * 50)
                    print(f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}")
                    print("-" * 50)
                    found = True
                    break

        if not found:
            print(f"\n No contact found with name '{search_name}'.\n")
    except FileNotFoundError:
        print("\n No contacts file found. Add a contact first.\n")


def main():
    while True:
        print("""===== CONTACT BOOK MENU =====
1. Add Contact
2. View All Contacts
3. Search Contact
4. Exit
============================= """)
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("\n Exiting Contact Book. Goodbye!\n")
            break
        else:
            print("\n Invalid choice! Please enter 1-4.\n")


if __name__ == "__main__":
    main()