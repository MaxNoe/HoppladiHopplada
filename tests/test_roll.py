def test_roll():
    from hoppladihopplada import Dice
    assert Dice.roll() in Dice


def test_rolls():
    from hoppladihopplada import Game, Dice

    roll = Game.roll(6)
    assert len(roll) == 6
    assert all(d in Dice for d in roll)
