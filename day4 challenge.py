class Person:
    def __init__(self, initialAge, year):
        self.age = 3
        self.year = 4

        # Add some more code to run some checks on initialAge

    def amIOld(self):
        print("1")

    # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here
        print("O")


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
