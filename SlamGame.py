
#Slam Game class that accesses player class and die class
class Slam :
    def __init__(self, pnum):
        self.playernum = pnum

    
    #def __str__

    def sidenum (self, num):
        self.diesides = num
        return self.diesides
        
    def initroll(self):
        self.thenum = die1.roll()
        return self.thenum
    
die1 = DiePracticeClass(self.diesides)
slammer = Slam(5)
print(slammer.initroll())
