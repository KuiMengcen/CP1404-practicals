MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
MENU = "(G)et a valid score \n(P)int resut \n(S)how starts \n(Quit)"


def main():
    """Displaying main menu"""
    student_score = -1
    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            student_score = get_score()
        elif choice == "p":
            student_score = Validate_score(student_score)
            print(get_grade(student_score))
        elif choice == "S":
            student_score = Validate_score(student_score)
            display_stars(student_score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter choice: ").upper()

    print("Farewell")


def Validate_score(student_score):
    """check uer entered score"""
    if student_score == -1:
        student_score = get_score()
    return student_score


def display_stars(student_score):
    """display stars"""
    print(int(student_score) * "*")


def get_score():
    """Verification Score"""
    student_score = float(input("Enter Score: "))
    while student_score < MINIMUM_SCORE or student_score > MAXIMUM_SCORE:
        print("Invalid score")
        student_score = float(input("Enter Score: "))
    return student_score


if __name__ == '__main__':
    main()
