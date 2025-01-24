dict1={}
n=6
for i in range(n):
    print("Enter your choice: ")
    print("1. Add a contact")
    print("2. Delete a contact")
    print("3. Edit a contact")
    print("4. Search a contact")
    print("5. List all contact")
    print("6. Exit")

    x=input("enter the choice: ")
    if x=="1":
        name=input("Enter the name: ")
        phone=input("Enter the number: ")
        dict1[name]=phone
        print("Contact added successfully")

    elif x=="2":
        name=input("Enter the name to delete ")
        if name in dict1:
            del dict1[name]
            print(f"Contact deleted successfully")
        else:
            print("Contact not found")

    elif x=="3":
        name=input("Enter contact name to edit: ")
        if name in dict1:
            phone = input("Enter the new phone number: ")
            dict1[name]=phone
            print(f"Contact updated successfully.")

    elif x=="4":
        name=input("Enter contact name to search: ")
        if name in dict1:
            print(f"Contact {name}: {dict1[name]}")
        else:
            print(f"Contact {name} not found.")

    elif x=="5":
        if dict1:
            print("Listing all contacts:")
            print("Name    Number")
            for name, phone in dict1.items():
                print(f"{name}  :  {phone}")

    elif x =="6":
        print("Exit the program")
        break

    else:
        print("Invalid choice.")