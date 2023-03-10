class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack(self, robot):
        robot.health -= self.attack_power
        print('\n{} has attacked {} and caused {} damage. {}\'s health is now {}'.format(self.name, robot.name, self.attack_power, robot.name, robot.health))