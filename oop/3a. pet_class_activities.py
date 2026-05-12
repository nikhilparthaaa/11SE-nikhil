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
        se;f.billing = billing_address
        self.owner = owner_name
        self.account = account_balance

p1=pet('Bonnie', 'cat', 12, True)

print(p1.name)
print(p1.category)
print(p1.age)
print('vaccinated:',p1.vaccine)

p2=pet('Foxy', "dog", '15', "False")
#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)