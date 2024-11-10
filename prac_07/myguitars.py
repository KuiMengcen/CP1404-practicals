class Guitar:
    def __init__(self, guitar_name="", guitar_year=0, guitar_cost=0):
        self.name = guitar_name
        self.year = guitar_year
        self.cost = guitar_cost

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year


guitars = []
new_guitars = []

in_file = open("guitars.csv", "r")

for item in in_file:
    parts = item.strip().split(',')
    guitar = Guitar(parts[0], int(parts[1]), parts[-1])
    guitars.append(guitar)