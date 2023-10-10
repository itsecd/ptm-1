from yahtzee import Yahtzee

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_init_score() -> None:
    """Test init_score function"""
    expected_score = 15
    actual_score = Yahtzee.init_score(2, 3, 4, 5, 1)
    assert expected_score == actual_score
    assert 16 == Yahtzee.init_score(3, 3, 4, 5, 1)


def test_check_for_five_identical_dice() -> None:
    """Test check_for_five_identical_dice function"""
    expected_score = 50
    actual_score = Yahtzee.check_for_five_identical_dice([4, 4, 4, 4, 4])
    assert expected_score == actual_score
    assert 50 == Yahtzee.check_for_five_identical_dice([6, 6, 6, 6, 6])
    assert 0 == Yahtzee.check_for_five_identical_dice([6, 6, 6, 6, 3])


def test_check_for_ones() -> None:
    """Test check_for_ones function"""
    assert Yahtzee.check_for_ones(1, 2, 3, 4, 5) == 1
    assert 2 == Yahtzee.check_for_ones(1, 2, 1, 4, 5)
    assert 0 == Yahtzee.check_for_ones(6, 2, 2, 4, 5)
    assert 4 == Yahtzee.check_for_ones(1, 2, 1, 1, 1)


def test_check_for_twos() -> None:
    """Test check_for_twos function"""
    assert 4 == Yahtzee.check_for_twos(1, 2, 3, 2, 6)
    assert 10 == Yahtzee.check_for_twos(2, 2, 2, 2, 2)


def test_check_for_threes() -> None:
    """Test check_for_threes function"""
    assert 6 == Yahtzee.check_for_threes(1, 2, 3, 2, 3)
    assert 12 == Yahtzee.check_for_threes(2, 3, 3, 3, 3)


def test_check_for_fours() -> None:
    """Test check_for_fours function"""
    assert 12 == Yahtzee(4, 4, 4, 5, 5).check_for_fours()
    assert 8 == Yahtzee(4, 4, 5, 5, 5).check_for_fours()
    assert 4 == Yahtzee(4, 5, 5, 5, 5).check_for_fours()


def test_check_for_fives() -> None:
    """Test check_for_fives function"""
    assert 10 == Yahtzee(4, 4, 4, 5, 5).check_for_fives()
    assert 15 == Yahtzee(4, 4, 5, 5, 5).check_for_fives()
    assert 20 == Yahtzee(4, 5, 5, 5, 5).check_for_fives()


def test_check_for_sixes() -> None:
    """Test check_for_sixes function"""
    assert 0 == Yahtzee(4, 4, 4, 5, 5).check_for_sixes()
    assert 6 == Yahtzee(4, 4, 6, 5, 5).check_for_sixes()
    assert 18 == Yahtzee(6, 5, 6, 6, 5).check_for_sixes()


def test_check_for_pairs() -> None:
    """Test check_for_pairs function"""
    assert 6 == Yahtzee.check_for_pairs(3, 4, 3, 5, 6)
    assert 10 == Yahtzee.check_for_pairs(5, 3, 3, 3, 5)
    assert 12 == Yahtzee.check_for_pairs(5, 3, 6, 6, 5)


def test_check_for_two_pairs() -> None:
    """Test check_for_two_pairs function"""
    assert 16 == Yahtzee.check_for_two_pairs(3, 3, 5, 4, 5)
    assert 0 == Yahtzee.check_for_two_pairs(3, 3, 5, 5, 5)


def test_check_for_three_identical_dice() -> None:
    """Test check_for_three_identical_dice function"""
    assert 9 == Yahtzee.check_for_three_identical_dice(3, 3, 3, 4, 5)
    assert 15 == Yahtzee.check_for_three_identical_dice(5, 3, 5, 4, 5)
    assert 0 == Yahtzee.check_for_three_identical_dice(3, 3, 3, 3, 5)


def test_check_for_four_identical_dice() -> None:
    """Test check_for_four_identical_dice function"""
    assert 12 == Yahtzee.check_for_four_identical_dice(3, 3, 3, 3, 5)
    assert 20 == Yahtzee.check_for_four_identical_dice(5, 5, 5, 4, 5)
    assert 0 == Yahtzee.check_for_four_identical_dice(3, 3, 3, 3, 3)


def test_check_for_small_straight() -> None:
    """Test init_score check_for_small_straight"""
    assert 15 == Yahtzee.check_for_small_straight(1, 2, 3, 4, 5)
    assert 15 == Yahtzee.check_for_small_straight(2, 3, 4, 5, 1)
    assert 0 == Yahtzee.check_for_small_straight(1, 2, 2, 4, 5)


def test_check_for_large_straight() -> None:
    """Test check_for_large_straight function"""
    assert 20 == Yahtzee.check_for_large_straight(6, 2, 3, 4, 5)
    assert 20 == Yahtzee.check_for_large_straight(2, 3, 4, 5, 6)
    assert 0 == Yahtzee.check_for_large_straight(1, 2, 2, 4, 5)


def test_check_for_full_house() -> None:
    """Test check_for_full_house function"""
    assert 18 == Yahtzee.check_for_full_house(6, 2, 2, 2, 6)
    assert 0 == Yahtzee.check_for_full_house(2, 3, 4, 5, 6)