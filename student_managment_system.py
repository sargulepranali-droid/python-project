while True :
    print("\n---student mangement system --- ")
    print("1. add student ")
    print("2. view student")
    print("3. exit")
    choice = input("enter choice: ")
    if choice =="1":
        name =input("enter student name: ")
        marks =  input("enter marks: ")
        with open("student.txt","a")as file:
            file.write(name + " - " + marks+ "\n")
            print("student added successfully!")
    elif choice == "2":
        try:
            with open("student.txt", "r") as file:
                print("\nstudent records:")
                print (file.read())
        except FileNotFoundError:
            print("no records found!")
    elif choice == "3":
        search = input("enter student name to search: ")
        try:
            with open("students.txt", "r") as file:
                data = file.read()
                if search.lower()in data.lower():
                    print("student found!")
                else:
                    print("student not found!")
        except FileNotFoundError:
             print("no record found!")
    elif choice == "4":
        print("thank you!")
        break
    else:
        print("invalind choice")