from random import randrange

class BadGuy():
    
    def __init__(self):
        self.name = ''
        self.health_points = randrange(50)
        self.armor = randrange(10)
        self.damage = randrange(15)
        self.resource = randrange(100)
        
    def attack(self):
        return self.damage
    
    def armor(self):
        return self.armor
    
    def getHP(self):
        return self.health_points
    
    def healthPointsMessage(self):
        print("{}'s health is currently: {}".format(self.name, self.health_points) )
    
    def reduceHealthPoints(self, damage):
        if damage > self.armor:
            self.health_points = self.health_points - ( damage - self.armor)
            print("{} has taken {} damage! Current HP is {}.".format(self.name, damage - self.armor, self.getHP()))
        else:
            self.health_points -= 1
            print("{} has taken {} damage! Current HP is {}.".format(self.name, 1, self.getHP()))
            
    def getResource(self):
        return self.resource
    
    def getName(self):
        return self.name

class Barbarian(BadGuy):
    def __init__(self):
        BadGuy.__init__(self)
        self.name = "Bill the Barbarian"
    
    def welcome(self):
        return "You hear from the darkness... 'My name is {0}, you killed my father. Prepare to die!'".format(self.name)
    
class Archer(BadGuy):
    def __init__(self):
        BadGuy.__init__(self)
        self.name = "Elfy the Elf"
    
    def welcome(self):
        return "A tiny man flies through the air yelling, '{}, will succeed where others have failed!'".format(self.name)
    
class Yoda(BadGuy):
    def __init__(self):
        BadGuy.__init__(self)
        self.name = "Darth Yoda"
    
    def welcome(self):
        return "'Finish your quest, you will not...', {} says calmly.".format(self.name)
    
class TrollKing(BadGuy):
    def __init__(self):
        self.name = "Troll King"
        self.health_points = randrange(300)
        self.armor = randrange(11)
        self.damage = randrange(20)
        self.resource = randrange(10000)
        

class Hero():
    def __init__(self, heroName):
        self.name = heroName
        self.health_points = 150
        self.damage = 12
        self.armor = 10
        self.resource = 0

    def attack(self):
        return self.damage
    
    def armor(self):
        return self.armor
    
    def getHP(self):
        return self.health_points
    
    def setHP(self):
        self.health_points = 150
        print("\nThe Divine intervenes. HP has been set to max.\n")
    
    def healthPointsMessage(self):
        print("{}'s health is currently: {}".format(self.name, self.health_points) )
    
    def reduceHealthPoints(self, damage):
        if damage > self.armor:
            self.health_points = self.health_points - ( damage - self.armor)
            print("{} has taken {} damage! Current HP is {}.".format(self.name, damage - self.armor, self.getHP()))
        else:
            self.health_points -= 1
            print("{} has taken {} damage! Current HP is {}.".format(self.name, 1, self.getHP()))
        
    def welcome(self):
        return "{} goes where no one has ever dared journey, valiantly charging into the darkness.".format(self.name)
    
    def addResource(self, resource):
        self.resource += resource
        print("You found {} gold! You now have {} gold.".format(resource, self.resource))
        
    def getResource(self):
        return self.resource
        
    def getName(self):
        return self.name
# m = Barbarian()       
# h = Hero("Jesse")
# print(h.welcome())
# 
# for i in range(5):
#     h.reduceHealthPoints(m.attack())
#     h.get_HP()
# 
# 
# 
# 
# 
# 
# m = Barbarian()
# print(m.attack())
# print(m.get_HP())
# print(m.welcome())
# print()
# a = Archer()
# print(a.attack())
# print(a.get_HP())
# print(a.welcome())
# print()
# y = Yoda()
# print(y.attack())
# print(y.get_HP())
# print(y.welcome())