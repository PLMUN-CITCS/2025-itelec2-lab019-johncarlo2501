def get_student_score():

 while True:
   try:
     score = float(input("Enter the student's score: "))
    if 0 <= score <= 100:
      return score
    else:
     print("Please enter a valid score between 0 and 100.")
   except ValueError:
        print("Invalid input. Please enter a numeric value.")

def calculate_grade(score):
    
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

if __name__ == "__main__":
    student_score = get_student_score()  
    student_grade = calculate_grade(student_score)  

    print(f"The student's grade is: {student_grade}")  

    print(f"The student's grade is: {student_grade}")

