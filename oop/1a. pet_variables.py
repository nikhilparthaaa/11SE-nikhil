name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

# ACTIVITIES:
#Theere are many ways to complete these tasks. How will you do them?
#1 Increase age by 1 year
#2 Change the address to 17 Park Street
#3 No longer vaccinated (change state of vaccinated)
#4 Prompt user for updated credit card number and save new number
#5 Change owner name to Alex Jones
#6 Subtract $25 from account balance

age=age+1
print("age:", age)

billing_address="17 Park St"
print(billing_address)

Vaccinated=False
print("vaccinted:", vaccinated)

Q_update=input("Update credit card number? ")
if Q_update=="yes":
    ccard=input("New number: ")
print(ccard)

owner_name = "Alex Jones"
print(owner_name)

account_balance = account_balance-25
print(account_balance)