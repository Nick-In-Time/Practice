import random
#Dice roller class
class Die :
    def __init__( self, sides) :
        self.numsides = sides

    def __str__( self ) :
        return "( The die has " + str(self.numsides) + " sides)"

    def roll(self):
        return random.randrange(1, self.numsides+1, 1)

    
die1 = Die(6)
print(die1.__str__())
print(die1.roll())
#print(die1.roll())
#print(die1.roll())
#print(die1.roll())
