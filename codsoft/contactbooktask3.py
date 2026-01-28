# conact book 
contacts = []

while True:
    print("\n1 Add  2 View  3 Search  4 Delete  5 Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts.append([name, phone])
        print("Added")

    elif ch == 2:
        for c in contacts:
            print(c[0], "-", c[1])

    elif ch == 3:
        name = input("Enter name: ")
        for c in contacts:
            if c[0] == name:
                print(c)


    elif ch == 4:
        name = input("Enter name to delete: ")
        for c in contacts:
            if c[0] == name:
                contacts.remove(c)
                print("Deleted")

    elif ch == 5:
        break

    else:
        print("Wrong choice")
