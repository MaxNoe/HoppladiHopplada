def test_lost():
    from hoppladihopplada import Dice
    from hoppladihopplada.utils import lost

    assert lost([Dice.CARROT, Dice.HUTCH5, Dice.HUTCH3])
    assert not lost([Dice.CARROT, Dice.HUTCH5, Dice.BUNNY])
    assert not lost([Dice.CARROT, Dice.BUNNIES])
    assert not lost([Dice.CARROT, Dice.CARROT])
    assert not lost([Dice.CARROT for i in range(6)])
    assert lost([Dice.HUTCH4, Dice.HUTCH3])
