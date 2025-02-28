def get_student_score():
    """Gets the student's score from user input."""
    score = float(input("Enter the student's score: "))  
    return score

def calculate_grade(score):
    """Determines the letter grade based on the score."""
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

# Main program
student_score = get_student_score()  
student_grade = calculate_grade(student_score)  
print(f"The student's grade is: {student_grade}")
