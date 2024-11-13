#Project II - Chasyl De Guzman

def main():
    # Step 1: Prompt for the number of students
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

              # Step 2: Collect grades
    grades = []
    for i in range(num_students):
        while True:
            try:
                grade = float(input(f"Enter the grade for student {i+1}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid grade between 0 and 100.")

    # Step 3: Calculate the average grade
    average = sum(grades) / len(grades)
    
    print(f"The class average is: {average:.2f}")

# Run the main function
if __name__ == "__main__":
    main()