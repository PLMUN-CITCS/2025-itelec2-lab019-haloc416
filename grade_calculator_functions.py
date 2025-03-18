def get_student_score() -> float:
    """
    Asks the user to input a score between 0 and 100.
    
    If the input is invalid (not a number or out of range), it will ask again until 
    a valid score is provided.
    
    Returns:
        float: The valid score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_grade(score: float) -> str:

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def main():

    student_score = get_student_score()
    grade = calculate_grade(student_score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()