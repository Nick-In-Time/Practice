
#Player class
class Player :
    def __init__(self, pscore, pname):
        self.score = pscore
        self.name = pname

    def __str__(self):
        return str(self.name) + " has " + str(self.score) + " points."

    def addpts(self, apts):
        self.score = self.score + apts
        return self.score

joe = Player(0, "Joe")
print(joe.__str__())
joe.addpts(5)
print(joe.__str__())
