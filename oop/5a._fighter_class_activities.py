#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

class Fighter:
    def __init__(self,Playername, BeginHealth, Dominant_Hand, Off_Hand):
        self.Playername = Playername
        self.Health = BeginHealth
        self.Dominant_Hand = Dominant_Hand
        self.Off_Hand = Off_Hand
   
    def report(self):
        print(self.Playername+':', 'Health:', str(self.Health))

    def random_attack(self):
        Attack_power= random.randint(((self.Dominant_Hand/2)*((self.Dominant_Hand*2)*((self.Off_Hand/100)))))
        return Attack_power
Fighter1 = Fighter("Player", 100, 25, 10)
Troll = Fighter("Troll", 150, 20, 5)

Fighter1.report()
Troll.report()
print("""you are fighting a troll
      
      you attack the troll""")
Troll.Health= Troll.Health - Fighter1.random_attack()
Troll.report()