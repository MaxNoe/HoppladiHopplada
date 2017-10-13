from .base import Player
from ..dice import Dice
from ..utils import confirm


class TerminalPlayer(Player):
    def select_dice(self, game):
        print(game)
        print()
        print('Please select at least one bunny dice')
        while True:
            try:
                indices = list(map(
                    int,
                    map(
                        str.strip,
                        input('Enter dice indices seperated by ",": ').split(',')
                    )
                ))

                assert all(
                    game.current_roll[idx] in (Dice.BUNNY, Dice.BUNNIES)
                    for idx in indices
                )
                break
            except (ValueError, IndexError, AssertionError) as e:
                print(e)
                print('Invalid input')
                continue

        print()
        return indices

    def decide_upgrade_hutch(self, game):
        return confirm('Do yo want to upgrade your Hutch?')

    def decide_rolling_again(self, game):
        print(game)
        return confirm('Do you want to roll again?')

    def decide_keep_last_roll(self, game):
        print(game)
        return confirm('Do you want to keep the last roll?')

    def notify_carrots(self, game):
        print(game)
        print('You rolled only carrots, lucky you!')

    def notify_lost(self, game):
        print(game)
        print()
        print('Düdümm, you lost')
        print()
