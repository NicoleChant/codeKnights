from __future__ import annotations
from attr import s , field
from attr.validators import instance_of
from typing import Union , ClassVar
import random
import logging

logging.basicConfig(level = logging.INFO ,
                                format = "%(asctime)s:%(message)s")


@s(slots=True)
class Player:

    name : str = field(converter = str)
    health : float = field(converter = float)
    armor : float = field(converter = float)
    lower_damage : float = field(converter = float)
    upper_damage : float = field(converter = float)
    dodge_chance : float = field(converter = float)
    max_health : float = field(init = False)
    target : Union[None,Character] = field(init = False , default = None)

    def __attrs_post_init__(self) -> None:
        self.max_health = self.health
        logging.info(f"Player {self.name} has been instantiated!")

    def is_alive(self):
        return self.health > 0

    def resurrect(self):
        self.health = self.max_health
        logging.info(f"Player {self.name} can now breathe again.")

    @target.validator
    def check(self , attribute , value):
        if not isinstance(value ,  Player) and value is not None:
            raise TypeError(f"Target must be of type {type(self).__name__}.")

    def set_target(self , other : Player ):
        self.target = other
        logging.info(f"{self.name} stares aggresively at {other.name}.")

    def generate_unmitigated_damage(self) -> float:
        return random.random()*( self.upper_damage - self.lower_damage) + self.lower_damage

    @staticmethod
    def damage_discount(armor : float , cap : float = 1) -> float:
        return min( cap , 1 - armor/(armor + 100))

    def generate_combat_event(self) -> str:
        if random.random() <= self.target.dodge_chance:
            return "Dodged"
        return "Normal"

    def active_damage_reduction(self):
        return Player.damage_discount(self.target.armor)

    def attack(self):
        unmitigated_damage = self.generate_unmitigated_damage()
        combat_event = self.generate_combat_event()
        if combat_event == "Normal":
            mitigated_damage = self.active_damage_reduction()*unmitigated_damage
            logging.info(f"Player {self.name} strikes {self.target.name} for {mitigated_damage:1.2f} damage (physical)!")
        else:
            mitigated_damage = 0
            logging.info(f"Player {self.target.name} dodges {self.name}'s attack!")
        self.target.health -= mitigated_damage
        if not self.target.is_alive():
            logging.info(f"Player {self.target.name} has deceased :(")


class Game:

    def set_targets(self , players):
        ##Setting Targets
        for idx in range(len(players)):
            players[idx].set_target(players[ (idx+1)%len(players)])

    def start(self , players):
        logging.info("Game has been initialized!")
        rounds = 1

        self.set_targets(players)

        while True:
            logging.info("*"*25 + f" Round {rounds} " + "*"*25)
            length = len(players)
            players = [player for player in players if player.is_alive()]

            if length > len(players) > 1:
                self.set_targets(players)

            if len(players) <= 1:
                logging.info(f"Game has ended in {rounds=}!")
                break

            for player in players:
                player.attack()
            rounds += 1

        if players:
            logging.info(f"Player {players[0].name} is victorious!")
        else:
            logging.info("The game ended in a DRAW!")


def main():
    players =   [   Player( name = "Nicole",health = 100, armor = 0, lower_damage = 10, upper_damage = 10 , dodge_chance = 0.2),
                          Player("Alice",120,10,5,20,0.2),
                          Player("Bob",150,5,1,20,0.1)
                        ]


    Game().start(players)

if __name__ == "__main__": main()
