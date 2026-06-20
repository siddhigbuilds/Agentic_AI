contact={}


while True:
    print("\n\n===== CONTACT BOOK =====")
    print("1.Add contact\n")
    print("2. View Contacts\n")
    print("3. Search Contact\n")
    print("4. Delete Contact\n")
    print("5. Exit\n")

    ch=int(input("Enter your choice :"))
    match ch:
     case 1:
        name=input("Enter Name :")
        phone=int(input("Enter Phone Numebr :"))
        contact[name]=phone
        print("Contact Added")

     case 2:
        for i in contact.items():
            print(i)
     case 3:
        n=input("Enter name to find :")
        for  i in contact.items():
         if n==i[0]:
            print(i)
            break
        else:
            print("Contact not found")

     case 4:
        d=input("Enter the contact to be deleted :")
        if d in contact:
            del contact[d]
            print("Contact Deleted successfully!")
        else:
            print("Contact not found")
     case 5:
        print("invalid choice")