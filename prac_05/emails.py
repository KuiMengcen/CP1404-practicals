def main():
    """Create dictionary of emails-to-names."""
    SPECIAL_CHARACTER = "@"
    email_to_name = {}

    email = input("Enter your email(Must contain @): ")
    while email != "":
        while SPECIAL_CHARACTER not in email:
            print("Error")
            email = input("Enter your email(Must contain @): ")
