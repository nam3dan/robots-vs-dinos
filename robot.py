from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Robo-Fist", 20)
    
    def attack(self, dinosaur):
        dinosaur.health -= 