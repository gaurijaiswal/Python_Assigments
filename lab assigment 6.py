students = {}

def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    students[id] = name
    print("Student added.")

def view_students():
    print("Student List:")
    for id, name in students.items():
        print(id, name)

def update_student():
    id = input("Enter ID to update: ")
    if id in students:
        name = input("Enter new name: ")
        students[id] = name
        print("Updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    id = input("Enter ID to delete: ")
    if id in students:
        del students[id]
        print("Deleted successfully.")
    else:
        print("Student not found.")

def search_student():
    id = input("Enter ID to search: ")
    if id in students:
        print("Student found:", students[id])
    else:
        print("Student not found.")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Search 6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        search_student()
    else:
        break