def get_student_score():
    """Handles user input to obtain the student's score."""
    while True:
        try:
            score = float(input("Enter the student's score: "))  # Get user input and convert to float
            if 0 <= score <= 100:  # Ensure the score is within a valid range
                return score
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score):
    """Determines the letter grade based on the given score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main program execution
if __name__ == "__main__":
    student_score = get_student_score()  # Get student score
    student_grade = calculate_grade(student_score)  # Determine the grade

    # Display the result
    print(f"The student's grade is: {student_grade}")  # Fixed missing print statement
