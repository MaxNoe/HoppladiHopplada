from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name
        self.reset()

    @abstractmethod
    def select_dice(self, game):
        pass

    @abstractmethod
    def decide_rolling_again(self, game):
        pass

    @abstractmethod
    def decide_keep_last_roll(self, game):
        pass

    @abstractmethod
    def decide_upgrade_hutch(self, game):
        pass

    @abstractmethod
    def notify_lost(self):
        pass

    @abstractmethod
    def notify_carrots(self, game):
        pass

    def reset(self):
        self.points = 0
