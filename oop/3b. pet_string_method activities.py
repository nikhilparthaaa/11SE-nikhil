# Learning intentions:
# - Create some default attributes of the class
# - Create the special print method that prints the status of the object

class Pet:
    def __init__(self, name, category, age = 0, ccard = 'XXXX-XXXX-XXXX-XXXX', vaccinated = False):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = ccard
        self.vaccinated = vaccinated

default = Pet('unknown', 'unknown', 0, 'XXXX-XXXX-XXXX-XXXX', False)

#ACTIVITIES:
#1. Add a default new credit card value  of unknown

#2. In the __str__ method, let the user know if the pet has registered payment details  

#3. Add the vaccinated status and include it in the special __str__ function
print("pet name:", default.name)
print("species:", default.category)
print('pet age:', default.age)
print('vaccinated:', default.vaccinated)
print('credit card:', default.ccard)
print(" ")



pet = Pet(input("input pet name: "), input("species: "), int(input("age: ")), input("credit card: "), bool(input("vaccinated? True/False:")))
print(" ")

if len(pet.ccard) == 19 and len(pet.ccard.split()) == 4:
    pet.ccard=pet.ccard
else:
    pet.ccard = 'XXXX-XXXX-XXXX-XXXX'

if pet.ccard == 'XXXX-XXXX-XXXX-XXXX':
    print("credit card not registered")
    print(" ")

print("pet name:", pet.name)
print("species:", pet.category)
print('pet age:', pet.age)
print('vaccinated:', pet.vaccinated)   
print('credit card:', pet.ccard)