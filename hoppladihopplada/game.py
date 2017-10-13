from .dice import Dice, HUTCH_DICE
from .utils import recursive_len, lost, print_points_table


class Game:
    N_DICE = 7

    def __init__(self, players):
        self.players = players

    def reset_dice(self):
        self.n_bunnies = 0
        self.bunny_dice = []
        self.n_hutch_dice = 0
        self.n_carrot_dice = 0
        self.current_roll = None

    @staticmethod
    def roll(n_dice):
        return sorted([Dice.roll() for i in range(n_dice)], key=lambda d: d.value)

    def get_available_dice(self):
        return (
            self.N_DICE -
            self.n_hutch_dice -
            self.n_carrot_dice -
            recursive_len(self.bunny_dice)
        )

    def store_bunnies(self):
        self.n_bunnies += self.count_bunnies()
        self.bunny_dice = []

    def count_bunnies(self):
        n_bunnies = 0
        for d in self.bunny_dice:
            if d == Dice.BUNNY:
                n_bunnies += 1

            elif d == Dice.BUNNIES:
                n_bunnies += 2

            elif isinstance(d, tuple):
                n_bunnies += 10

        return n_bunnies

    def evaluate_points(self):
        n_bunnies = self.n_bunnies + self.count_bunnies()
        return (self.n_hutch_dice + 1) * n_bunnies

    def turn(self, player):
        if self.current_roll is not None:
            if not player.decide_keep_last_roll(self):
                self.reset_dice()

        roll_again = True
        while roll_again:
            available_dice = self.get_available_dice()
            if available_dice == 0:
                if len(self.bunny_dice) > 0:
                    self.store_bunnies()
                    available_dice = self.get_available_dice()
                else:
                    self.update_points(player)
                    self.reset_dice()
                    break

            self.current_roll = self.roll(available_dice)

            if lost(self.current_roll):
                player.notify_lost(self)
                self.reset_dice()
                break

            if all(d == Dice.CARROT for d in self.current_roll):
                self.n_carrot_dice += len(self.current_roll)
                self.current_roll = []
                player.notify_carrots(self)

            else:
                indices = player.select_dice(self)
                self.update_selected_dice(indices)

                for n, hutch_dice in enumerate(HUTCH_DICE):
                    if self.n_hutch_dice == n and hutch_dice in self.current_roll:
                        if player.decide_upgrade_hutch(self):
                            self.current_roll.remove(hutch_dice)
                            self.n_hutch_dice += 1
                        break

            roll_again = player.decide_rolling_again(self)
            print()

        player.points += self.evaluate_points()

    def start(self):
        for p in self.players:
            p.reset()
        self.reset_dice()

        max_points = 0
        while max_points < 333:
            print_points_table(self.players)
            for player in self.players:
                print(2 * '\n')
                print(f'{f"  {player.name}  ":#^40}')
                self.turn(player)

                max_points = max(p.points for p in self.players)
        print_points_table(self.players)

    def update_selected_dice(self, indices):
        selected_dice = [
            self.current_roll.pop(i)
            for i in sorted(indices, reverse=True)
        ]
        selected_dice.sort(key=lambda d: d.value)

        n_single_bunnies = 0
        while Dice.BUNNY in selected_dice:
            n_single_bunnies += 1
            selected_dice.remove(Dice.BUNNY)

        for i in range(n_single_bunnies // 2):
            self.bunny_dice.append((Dice.BUNNY, Dice.BUNNY))

        if n_single_bunnies % 2 == 1:
            self.bunny_dice.append(Dice.BUNNY)

        while selected_dice:
            self.bunny_dice.append(selected_dice.pop())

    def __repr__(self):

        s = ''
        s += 'Bunnies:   {}, Hutch: {}, Carrots: {}, Points: {}'.format(
            self.n_bunnies, self.n_hutch_dice + 1,
            self.n_carrot_dice, self.evaluate_points()
        )
        if self.bunny_dice:
            s += '\nBunny Dice: {}'.format(', '.join(
                b.value
                if not isinstance(b, tuple) else '({0.value} {1.value})'.format(*b)
                for b in self.bunny_dice
            ))
        if self.current_roll is not None:
            s += '\nDice:       '
            s += ', '.join(
                '{}[{}]'.format(d.value, i)
                for i, d in enumerate(self.current_roll)
            )
        return s
