from fleet import Fleet
from herd import Herd
import random
from time import sleep

map_list = ['in Vietnam','in St. Louis','on The Moon', 'at Your Mother\'s house','between Steve Buscemi\'s teeth']
print_pacing = 2

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
    
    def run_game(self):
        self.display_welcome()
        while len(self.fleet.robot_fleet) > 0 and len(self.herd.dino_herd) > 0:
            self.battle_phase()
            self.display_winner()
        self.display_final_winner()

    def display_winner(self):
        sleep(print_pacing)
        if winner == 1:
            print(f"\n{user.name} has murdered {target.name}.")
        elif winner == 0:
            print(f"\n{target.name} has murdered {user.name}.")
        else:
            print(f"\nBoth {user.name} and {target.name} have died.")
        sleep(print_pacing)

    def display_welcome(self):
        print("\n\nWelcome to the epic fight between Robots and Dinosaurs.......")
        sleep(print_pacing)
        print(f"\n\nToday's fight will take place {map_list[random.randint(0,len(map_list)-1)]}.")
        sleep(print_pacing)
        print('\n\nLet\'s meet today\'s fighters.')
        sleep(print_pacing)
        print('\n\nFrom the Dinosaurs:')
        for i in self.herd.dino_herd:
            print(i.name + ": At-Pwr: " +str(i.attack_power))
        sleep(print_pacing)
        print('\n\nFrom the Robots:')
        for i in self.fleet.robot_fleet:
            print("\n" + i.name)
            for x in i.weapon_list:
                print('     ' + x.name + ': At-Pwr: ' + str(x.attack_power))
        sleep(print_pacing)
        print("\nYou will be controlling the Robots today")
        sleep(print_pacing)
        print("\n Let the battle begin..............")
        sleep(print_pacing)
    
    def battle_phase(self):
        global target
        global user
        global winner
        print("\nPlease select your Robot.")
        robot_numbering = 1
        for i in self.fleet.robot_fleet:
            print(f"\n{robot_numbering}. " + i.name)
            robot_numbering += 1 
        robot_selection = int(input("\nPlease enter # of your Robot: ")) - 1 
        print(f"\n{self.fleet.robot_fleet[robot_selection].name} has been selected.")
        user = self.fleet.robot_fleet[robot_selection]
        print("\nPlease select which Dinosaur, you'd like to attack")
        choice_numbering = 1
        for i in self.herd.dino_herd:
            print(f"\n{choice_numbering}. " + i.name)
            choice_numbering += 1
        choice_numbering = 1
        target_selection = int(input("\nPlease enter # of your target: ")) - 1
        target = self.herd.dino_herd[target_selection]
        print(f"\n{user.name} is attacking {target.name}")
        while target.health > 0 and user.health > 0:
            for i in user.weapon_list:
                print(f"\n{choice_numbering}. " + i.name + ": At Pwr:" + str(i.attack_power))
                choice_numbering += 1
            choice_numbering = 1
            attack_selection = int(input("\nPlease select a Weapon: ")) - 1
            user.active_weapon = user.weapon_list[attack_selection]
            user.attack(target)
            sleep(print_pacing)
            if target.health > 0:
                target.attack(user)
            sleep(print_pacing)
        if target.health <= 0:
            self.herd.dino_herd.remove(target)
            winner = 1
        elif user.health <= 0:
            self.fleet.robot_fleet.remove(user)
            winner = 0
        else:
            self.fleet.robot_fleet.remove(user)
            self.herd.dino_herd.remove(target)
            winner = 2
        return target, user, winner
    
    def display_final_winner(self):
        if len(self.fleet.robot_fleet) > len(self.herd.dino_herd):
            print('\n The Robots have won!')
            
        elif len(self.fleet.robot_fleet) < len(self.herd.dino_herd):
            print('\n The Dinosaurs have won!')
        else:
            print('\nSweet Baby Jesus, it\'s a tie!')


