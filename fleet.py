from robot import Robot
from weapon import Weapon
import random

robot_name_list = ['R2-D2','ChatGPT', 'C3PO', 'Terminator', 'Optimus Prime', 'Roomba', 'HAL 9000', 'Kitt', 'Golden Readon', 'CNN News Anchor']
weapons_name_list = ['Laser Gun','Laser Eyes','Machine Gun','Light Saber', 'Dino-bomb', 'Irish Car Bomb', 'Drone Strike', 'Crotch Rocket', 'Pulse Grenade']
weapon_power = [5,5,10,10,10,20,20,20,40]

class Fleet:
    def __init__(self):
        self.robot_fleet = []
        self.make_fleet()

    def make_fleet(self):
         robo_counter = 0
         while robo_counter < 3:
            weapon_counter = 0
            self.name = robot_name_list.pop(robot_name_list.index(robot_name_list[random.randint(0,len(robot_name_list)-1)]))
            name = Robot(self.name)
            self.robot_fleet.append(name)
            print(name.name)
            while weapon_counter < 3:
                self.weapon = weapons_name_list.pop(weapons_name_list.index(weapons_name_list[random.randint(0,len(weapons_name_list)-1)]))
                self.power = weapon_power.pop(weapon_power.index(weapon_power[random.randint(0,len(weapon_power)-1)]))
                weapon = Weapon(self.weapon,self.power)
                name.weapon_list.append(weapon)
                weapon_counter += 1
            robo_counter += 1




