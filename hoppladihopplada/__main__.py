from .game import Game
from .players import TerminalPlayer
from .utils import confirm


def main():
    more = True
    players = []
    while more:
        name = input('Please enter a player name > ')
        players.append(TerminalPlayer(name))
        more = confirm('Do you want to add another player?')

    g = Game(players)
    g.start()


if __name__ == '__main__':
    main()
