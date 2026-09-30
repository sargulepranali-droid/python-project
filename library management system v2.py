while True :
    print("\n---library management system v2 ---")
    print("1. add book ")
    print("2. view book")
    print("3. search book")
    print("4. delete book")
    print("5. exit")
    choice = input("enter choice:")
    if choice == "1":
        book = input("enter your book name:")
        with open("library.txt","a") as file:
            file.write(book + "\n")
        print("book added sucessfully!")
    elif choice == "2":
        try: 
            with open("library.txt", "r")as file:
                books = file.read()
            print("\nbooks in libery:")   
            print(books)     
        except FileNotFoundError:
            print("no books found !")
    elif choice == "3" :
        search_book = input("ente rbook name to search:") 
        try:
            with open ("library.txt", "r") as file:
                books = file.readlines()    
            found = False
            for book in books:
                if search_book.lower() == book.strip(). lower():
                     found =True
                     break
            if found:
                print("book found!")    
            else:
                print("book not found !")  
        except FileNotFoundError:
            print("no books found!")       
    elif choice == "4":
        delete_book = input("enter book name to delete:")
        try:
            with open("library.txt" , "r") as file:
                books = file.readlines()
            with open("library.txt", "w") as file:
                for book in books:
                    if book.strip().lower() != delete_book.lower():
                                                                    file.write(book)  
            print("book deleted sucessfully!")
        except FileNotFoundError:
            print("no books found!")
    elif choice == "5":
        print("thank you!")
        break
    else:
        print("invalid choice")