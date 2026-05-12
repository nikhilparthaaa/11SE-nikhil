#Tutorial 3 Lists:
#1. Create an example of parallel lists eg: pet_name, species, age, vaccination_status for three pets
pet_name = ['Jack', 'jenny', 'ovuevuevue']
species = ['dog', 'cat', 'hamster']
age = [5,8,1]
vaccination_status = [True, False, True]

for i in range(len(pet_name)):
    print(pet_name[i])
    print(species[i])
    print(age[i])
    print(vaccination_status[i])
    print('')


#2. Use a for loop to print parallel list details. This will mean that one complete printout will look like:
'''
Pet name: Foxy
Species: Dog
Age: 8
Vaccination Status: False
'''
#3. Demonstrate what happens when an item is deleted




  #ACTIVITIES:
# In each activity test out that the printing of data is still valid
#1. Add a new animal named Hootie, its a blowfish, it is 34 years
#2. Vaccinate an unvaccinated animal (create vaccination)
#3. Remove an animal and make sure that all the printing is correct

pet_name = ['Jack', 'jenny', 'ovuevuevue', 'hootie']
species = ['dog', 'cat', 'hamster', 'blowfish']
age = [5,8,1,13]
vaccination_status = [True, False, True, False]

for i in range(len(pet_name)):
    print(pet_name[i])
    print(species[i])
    print(age[i])
    print(vaccination_status[i])
    print('')
