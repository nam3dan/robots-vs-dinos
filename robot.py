from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon_list = [Weapon("Robo-Fist", 5)]
        self.active_weapon = self.weapon_list[0]
    
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print('\n{} has attacked {} and caused {} damage. {}\'s health is now {}'.format(self.name, dinosaur.name, self.active_weapon.attack_power, dinosaur.name, dinosaur.health))