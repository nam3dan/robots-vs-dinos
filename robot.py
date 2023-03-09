from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        Robo_fist = Weapon("Robo-Fist", 5)
        self.weapon_list = [Robo_fist.name]
        self.active_weapon = self.weapon_list[0]
    
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print('{} has attacked {} and caused {} damage. {}\'s health is now {}'.format(self.name, dinosaur.name, self.active_weapon.attack_power, dinosaur.name, dinosaur.health))