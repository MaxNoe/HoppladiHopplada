import random
from enum import Enum


class Dice(Enum):
    BUNNY = 'B'
    BUNNIES = 'BB'
    HUTCH3 = 'H3'
    HUTCH4 = 'H4'
    HUTCH5 = 'H5'
    CARROT = 'C'

    @classmethod
    def roll(cls):
        return random.choice(list(cls))


HUTCH_DICE = [Dice.BUNNIES, Dice.HUTCH3, Dice.HUTCH4, Dice.HUTCH5]
