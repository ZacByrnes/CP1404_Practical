"""
CP1404/CP5632 Practical - Suggested Solution
Guitar program.
"""
PRESENT YEAR = 2018
VINTAGE_AGE = 50

class Guitar:
    def main():
        name = input("Enter Name: ")
        #Always Error Check
        while name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            print("My guitar: {}, first made in {} costed ${}".format(name, year, cost))

    def __init__(self, name, year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self, ):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self, ):
        return PRESENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt(self, other):
        return self.year < other.year
    main()