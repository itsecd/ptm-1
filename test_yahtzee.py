from yahtzee import Yahtzee

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance_scores_sum_of_all_dice():
    expected = 15
    actual = Yahtzee.chance([2, 3, 4, 5, 1])
    assert expected == actual
    assert 16 == Yahtzee.chance([3, 3, 4, 5, 1])


def test_yahtzee_scores_50():
    expected = 50
    actual = Yahtzee.yahtzee([4, 4, 4, 4, 4])
    assert expected == actual
    assert 50 == Yahtzee.yahtzee([6, 6, 6, 6, 6])
    assert 0 == Yahtzee.yahtzee([6, 6, 6, 6, 3])


def test_ones():
    assert Yahtzee.ones_twos_threes([1, 2, 3, 4, 5], 1) == 1
    assert 2 == Yahtzee.ones_twos_threes([1, 2, 1, 4, 5], 1)
    assert 0 == Yahtzee.ones_twos_threes([6, 2, 2, 4, 5], 1)
    assert 4 == Yahtzee.ones_twos_threes([1, 2, 1, 1, 1], 1)


def test_twos():
    assert 4 == Yahtzee.ones_twos_threes([1, 2, 3, 2, 6], 2)
    assert 10 == Yahtzee.ones_twos_threes([2, 2, 2, 2, 2], 2)


def test_threes():
    assert 6 == Yahtzee.ones_twos_threes([1, 2, 3, 2, 3], 3)
    assert 12 == Yahtzee.ones_twos_threes([2, 3, 3, 3, 3], 3)


def test_fours():
    assert 12 == Yahtzee([4, 4, 4, 5, 5]).fours_fives_sixes(4)
    assert 8 == Yahtzee([4, 4, 5, 5, 5]).fours_fives_sixes(4)
    assert 4 == Yahtzee([4, 5, 5, 5, 5]).fours_fives_sixes(4)


def test_fives():
    assert 10 == Yahtzee([4, 4, 4, 5, 5]).fours_fives_sixes(5)
    assert 15 == Yahtzee([4, 4, 5, 5, 5]).fours_fives_sixes(5)
    assert 20 == Yahtzee([4, 5, 5, 5, 5]).fours_fives_sixes(5)


def test_sixes():
    assert 0 == Yahtzee([4, 4, 4, 5, 5]).fours_fives_sixes(6)
    assert 6 == Yahtzee([4, 4, 6, 5, 5]).fours_fives_sixes(6)
    assert 18 == Yahtzee([6, 5, 6, 6, 5]).fours_fives_sixes(6)


def test_one_pair():
    assert 6 == Yahtzee.score_pair([3, 4, 3, 5, 6])
    assert 10 == Yahtzee.score_pair([5, 3, 3, 3, 5])
    assert 12 == Yahtzee.score_pair([5, 3, 6, 6, 5])


def test_two_pair():
    assert 16 == Yahtzee.two_pair([3, 3, 5, 4, 5])
    assert 0 == Yahtzee.two_pair([3, 3, 5, 5, 5])


def test_three_pair():
    assert 9 == Yahtzee.three_four_pair([3, 3, 3, 4, 5], 3)
    assert 15 == Yahtzee.three_four_pair([5, 3, 5, 4, 5], 3)
    assert 0 == Yahtzee.three_four_pair([3, 3, 3, 3, 5], 3)


def test_four_pair():
    assert 12 == Yahtzee.three_four_pair([3, 3, 3, 3, 5], 4)
    assert 20 == Yahtzee.three_four_pair([5, 5, 5, 4, 5], 4)
    assert 0 == Yahtzee.three_four_pair([3, 3, 3, 3, 3], 4)


def test_small_straight():
    assert 15 == Yahtzee.small_straight([1, 2, 3, 4, 5])
    assert 15 == Yahtzee.small_straight([2, 3, 4, 5, 1])
    assert 0 == Yahtzee.small_straight([1, 2, 2, 4, 5])


def test_large_straight():
    assert 20 == Yahtzee.large_straight([6, 2, 3, 4, 5])
    assert 20 == Yahtzee.large_straight([2, 3, 4, 5, 6])
    assert 0 == Yahtzee.large_straight([1, 2, 2, 4, 5])


def test_full_house():
    assert 18 == Yahtzee.full_house([6, 2, 2, 2, 6])
    assert 0 == Yahtzee.full_house([2, 3, 4, 5, 6])
