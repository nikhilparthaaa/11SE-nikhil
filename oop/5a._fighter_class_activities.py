#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

class Fighter:
    def __init__(self,Playername, BeginHealth = 100, Dominant_Hand = 25, Off_Hand = 10):
        self.Playername = Playername
        self.Health = BeginHealth
        self.Dominant_Hand = Dominant_Hand
        self.Off_Hand = Off_Hand

    def report(self):
        print(self.Playername+':', 'Health:', str(self.Health))

    def random_attack(self):
        Attack_power = random.randint(self.Dominant_Hand//2-self.Off_Hand, self.Dominant_Hand*2-self.Off_Hand) #Subtracts the offhand(shield) from the attack power 
        return Attack_power

Player = Fighter("Player", 100, 35, 20)
Troll = Fighter("Troll", 350, 20, 5)

print(Player.Playername, "Health:", Player.Health, "Dominant Hand Attack Power:", Player.Dominant_Hand, "Off Hand of enemy:", Player.Off_Hand)
print(Troll.Playername, "Health:", Troll.Health, "Dominant Hand Attack Power:", Troll.Dominant_Hand, "Off Hand of enemy:", Troll.Off_Hand)
print("    ")
print("you are fighting a troll")
print("    ")
while Player.Health!=0 and Troll.Health!=0:

    Player.report()
    Troll.report()

    turn = random.randint(0,1)
    if turn == 0:
        print("you Hit first this round")
        Troll.Health -= Player.random_attack()
        print("you hit the troll for", Player.random_attack(), "damage")
        Troll.Health -= Player.random_attack()
        print("you hit once more for", Player.random_attack(), "damage")
    else:
        print("the troll hits first this round")
        Player.Health -= Troll.random_attack()
        print("the troll hits you for", Troll.random_attack(), "damage")
        Troll.Health -= Player.random_attack()
        print("you retaliate for", Player.random_attack(), "damage")

    if Troll.Health <= 0:
        Troll.Health = 0

    elif Player.Health <= 0:
        Player.Health = 0
    
    else:
        print(" ")

    if Troll.Health == 0:
        win=True
        print("winnner: Player")

    elif Player.Health == 0:
        win=True
        print("winner: Troll")

    else:
        print("next round")

if win == True:
    print(" ")
    Player.report()
    Troll.report()