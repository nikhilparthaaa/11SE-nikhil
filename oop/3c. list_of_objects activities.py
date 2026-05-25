# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets


class Pet:
    def __init__(self, name, category, age = 0, ccard = 'XXXX-XXXX-XXXX-XXXX', vaccinated = False):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = ccard
        self.vaccinated = vaccinated

p1 = Pet('Cupcake', 'Dog', 12, '1234-5678-1234-5678', False)
p2 = Pet('Galaxy destroyer', 'cat', 4, '1234-5678-9012-3456', False)
p3 = Pet('leonard', 'dog', 3, '6543-2109-8765-4321', True)

info = [p1, p2, p3]

for i in info:
    print(" ")
    print("pet name:", i.name)
    print("species:", i.category)
    print('pet age:', i.age)
    print('vaccinated:', i.vaccinated)
    print('credit card:', i.ccard)

#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list