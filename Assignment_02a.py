grades = {}
while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. View All Grades")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
        print("Student added successfully!")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade: ")
            grades[name] = grade
            print("Grade updated!")
        else:
            print("Student not found!")
    elif choice == '3':
        print("\nAll Student Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again!")
