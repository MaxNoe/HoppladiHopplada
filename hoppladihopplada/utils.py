from itertools import product
from collections import Iterable

from .dice import Dice


def confirm(question, default=True):
    answer = input(question + ' [Yn]' if default is True else ' [yN]')
    if not answer:
        return default
    return answer.lower().startswith('y')


def recursive_len(iterable):
    return sum(
        recursive_len(l) if isinstance(l, Iterable) else 1
        for l in iterable
    )


def lost(roll):
    if any(d in (Dice.BUNNY, Dice.BUNNIES) for d in roll):
        return False

    if all(Dice.CARROT == d for d in roll):
        return False

    return True


def calculate_loosing_probability(n_dice):
    n = sum(lost(roll) for roll in product(Dice, repeat=n_dice))
    return n / 6**n_dice


def print_points_table(players):
    column_width = [max(3, len(player.name)) for player in players]
    fmt = ' | '.join(f'{{: >{w}d}}' for w in column_width)

    header = ' | '.join(p.name for p in players)
    print('-' * len(header))
    print(header)
    print('-' * len(header))
    print(fmt.format(*[p.points for p in players]))
    print('-' * len(header))
