class Library:
    def __init__(self):
        self.name=input("Name:")
        self.author=input("author:")
        self.page=int(input("Name of page:"))

library=[]

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Delete Book")
    print("4. Display Books")
    print("5. Exit")

    ch=int(input("Enter your choice :"))

    match ch:
        case 1:
            a=Library()
            library.append(a)
        
        case 2:
            n=input("Name:")
            for i in library:
                if i.name==n:
                    print(i.name,i.author,i.page)
                    break
            else:
                print("Book not found")
        
        case 3:
            n=input("Name:")
            for i in library:
                if i.name==n:
                    library.remove(i)
                    print("Book deleted successfully!")
                    break
            else:
                print("Book not found")
        
        case 4:
            for i in library:
                print(i.name,i.author,i.page)
        
        case 5:
            break



    
