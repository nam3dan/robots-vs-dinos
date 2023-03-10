from dino import Dinosaur
import random

dino_name_list = ['Reptar','Barney', 'Rex', 'Yoshi', 'Big Bird', 'Gronk', 'Nancy Pelosi', 'Mitch McConnell', 'Godzilla', 'Dino Flintstone']
attack_power = [5,5,5,10,10,20,20,30,40]

class Herd:
    def __init__(self):
        self.dino_herd = []
        self.make_herd()
    
    def make_herd(self):
        dino_counter = 0
        while dino_counter < 3:
            self.name = dino_name_list.pop(dino_name_list.index(dino_name_list[random.randint(0,len(dino_name_list)-1)]))
            self.power = attack_power.pop(attack_power.index(attack_power[random.randint(0,len(attack_power)-1)]))
            name = Dinosaur(self.name, self.power)
            self.dino_herd.append(name)
            dino_counter += 1