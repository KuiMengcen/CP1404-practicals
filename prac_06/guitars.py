from prac_06.guitar import Guitar

def main():
    guitars = []

    print("My Guitars!")

    name = input("Enter guitar name: ")
    while name != "":
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)
        print(f"{guitar_add}, added")
        name = input("Enter guitar name: ")