file = open("contacts. txt", "a")
name = input("enter name: ")
number = input("enter number:")
file. write(name + " - " + number + "\n")
file.close()
print("contact saved!")
file = open("contacts.txt" , "r")
data = file.read()
print("\nsaved contacts:")
print(repr(data))
file.close()
search = input("\nenter name to search: ").strip()
if search in data:
    print("contact found!")
else:
    print("contact not found!")
delete_name = input("\nenter name to delete: ")
lines = open("contacts.txt", "r").readlines()
file = open("contacts.txt", "w")
for line in lines:
    if delete_name not in line:
        file.write(line)
file.close()
print("contact deleted!")
lines = open("contacts.txt", "r").readlines()
file  = open("contacts.txt", "w")
for line in lines:
    if update_name in line:
        update_name = input ("enter name to updat: ")
        new_number = input ("enter new number: ")
        file.write(update_name + " - " + new_number + "\n")
    else:
        file.write(line)
file.close()
print("contact updated")
old_name = input("enter old name : ")
new_name = input("enter new name : ")
lines = open ("contacts.txt", "r").readlines()
file = open("contacts.txt", "w")
for line in lines:
    if old_name in line :
        number = line.split(" _ ")[1]
        file.write(new_name + " _ " + number)
    else:
        file.write(line)
file.close()
print("name updated!")