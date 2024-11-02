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

    guitars.append(Guitar("Gibson L-5 CES", 1992, 16035.40))
    guitars.append(Guitar("Frender Sratocruisers", 2014, 765.4))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars:")

        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:<23} ({1.year:<4}), worth ${1.cost:10,.2f}").format(i, guitar, vintage_string)
        else:
            print("No guitars :( Quick, go and buy one!")
