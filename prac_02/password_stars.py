PASSWORD_LENGTH = 0  # Consider setting it to a positive value to enforce minimum password length.


def main():
    """
    display password length
    """
    password = get_password()
    print(len(password) * '*')


def get_password():
    """
  Prompts the user for a password, returning a password string that meets the minimum length requirement.
    """
    password = input("Please enter a password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid Password")
        password = input("Please enter a password: ")
    return password


main()
