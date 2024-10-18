def main():
    """Create dictionary of emails-to-names."""
    SPECIAL_CHARACTER = "@"
    email_to_name = {}

    email = input("Enter your email(Must contain @): ")
    while email != "":
        while SPECIAL_CHARACTER not in email:
            print("Error")
            email = input("Enter your email(Must contain @): ")

        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/N) ").upper()
        if confirmation.upper() !="Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Enter your email(Must contain @): ")

    print_email(email_to_name)


def print_email(email_to_name):
    for email, name in email_to_name.items():
        print(f"{name}({email})")


def get_name(email):
    "Extract expected name from email address."
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()