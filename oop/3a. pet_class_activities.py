# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class pet:
    def __init__(self, pet_name, category, age, vaccine, credit_card, billing_address, owner_name, account_balance):
        self.name=pet_name
        self.category = category
        self.age = age
        self.vaccine = vaccine
        self.credit = credit_card
        self.billing = billing_address
        self.owner = owner_name
        self.account = account_balance

p1=pet('Bonnie', 'cat', 12, True, '1234-5678-9012-3456', '32 unknown park', 'John', 0)

print(p1.name)
print(p1.category)
print(p1.age)
print('vaccinated:',p1.vaccine)
print(p1.credit)
print(p1.billing)
print(p1.owner)
print(p1.account)
print(" ")
p2=pet('Foxy', "dog", '15', "False", '6543-2109-8765-4321', '23 unknown street', 'unknown', 0)
print(p2.name)
print(p2.category)
print(p2.age)
print('vaccinated:',p2.vaccine)
print(p2.credit)
print(p2.billing)
print(p2.owner)
print(p2.account)
print(" ")

#ACTIVITIES:
#1. Print out vaccination status of Bonnie

#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)