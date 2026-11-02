"""Student Grade Tracker

A beginner-friendly command-line app for recording student grades
and viewing class statistics.
"""

students = []


def add_student():
    """Add a student's name and numeric grade."""
    name = input("Student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        grade = float(input("Grade (0-100): "))
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 100.")
        return
    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        return

    # Improvement opportunity for Unit 3:
    # This version checks that the grade is numeric, but does not yet
    # reject values outside the 0-100 range.
    students.append({"name": name, "grade": grade})
    print(f"Added {name}.")


def show_students():
    """Display all students and their grades."""
    if not students:
        print("No students have been added yet.")
        return

    print("\nStudent grades")
    print("-" * 30)
    for student in students:
        print(f"{student['name']}: {student['grade']:.1f}")
    print("-" * 30)


def show_average():
    """Calculate and display the class average."""
    if not students:
        print("Add at least one student first.")
        return

    average = sum(student["grade"] for student in students) / len(students)
    print(f"Class average: {average:.2f}")


def main():
    """Run the application menu."""
    while True:
        print("\n=== Student Grade Tracker ===")
        print("1. Add a student")
        print("2. View all students")
        print("3. Calculate class average")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            show_average()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
