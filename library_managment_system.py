books = []
while True:
    print("\n======library managment system ===")
    print("1 .add book")
    print("2. view books")
    print("3. search book")
    print("4. delet book")
    print("5. update book")
    print("6. exit")
    choice = input("enter your choice : ")
    if choice == "1":
        book_name = input("enter your book name:")
        books.append(book_name)
        print(" book added sucessfully! ")
    elif choice == "2":
        if len(books)== 0:
            print("no books available!")
        else:
            print("\nbooks in library:")
        for book in books:
            print (book)
    elif choice == "3":
        search_book = input("enter book name to search:")
        if search_book in books:
            print("book found !")
        else :
            print("book not found")
    elif choice == "4":
        delete_book = input("enter book name to delete: ")
        if delete_book in books:
            books.remove(delete_book)
            print("book deletedsuccessfully!")
        else:
            print("book not found!")
    elif choice == "5" :
        old_book = input("enter old book name:")
        if old_book in books:   
            new_book = input("enter new book name:") 
            index = books.index(old_book)
            books[index] = new_book
            print("book updated successfully!")
        else: print("book not found!")    
    elif choice == "6":
        print("thank you")
        break
    else:
        print("invalid choice")