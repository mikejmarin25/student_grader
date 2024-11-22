def calculate_grade(average):
    """Returns a grade based on the average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def main():
    """Main program loop."""
    print("Welcome to the Student Grader Program!")
    students = []

    while True:
        print("\nOptions:")
        print("1. Add a new student")
        print("2. Display all students' grades")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice not in {"1", "2", "3"}:
            print("Invalid choice. Please try again.")
            continue

        if choice == "3":
            print("Exiting the program. Goodbye!")
            break

        if choice == "1":
            name = input("Enter the student's name: ")
            try:
                scores = input("Enter the student's scores separated by commas (e.g., 85,90,78): ")
                scores = [float(score.strip()) for score in scores.split(",")]
            except ValueError:
                print("Invalid input. Make sure to enter numeric scores separated by commas.")
                continue

            average = sum(scores) / len(scores)
            grade = calculate_grade(average)
            students.append({"name": name, "scores": scores, "average": average, "grade": grade})
            print(f"{name}'s data added successfully.")

        elif choice == "2":
            if not students:
                print("No student data available.")
            else:
                print("\nStudent Grades:")
                for student in students:
                    print(f"Name: {student['name']}, Average: {student['average']:.2f}, Grade: {student['grade']}")