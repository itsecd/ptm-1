from yahtzee import Yahtzee


def test_chance_scores_sum_of_all_dice():
        """tests the "Chance" category, which is the sum of all dice.
        It tests that the function returns the expected value for two different sets of dice"""
        expected = 15
        actual = Yahtzee.chance(2, 3, 4, 5, 1)
        assert expected == actual

        assert 16 == Yahtzee.chance(3, 3, 4, 5, 1)


def test_yahtzee_scores_50():
        """tests the "Yahtzee" category, which is five of a kind. It tests that the function
         returns 50 for a set of five matching dice, and 0 for sets that do not have five matching dice"""
        expected = 50
        actual = Yahtzee.yahtzee([4, 4, 4, 4, 4])
        assert expected == actual

        assert 50 == Yahtzee.yahtzee([6, 6, 6, 6, 6])
        assert 0 == Yahtzee.yahtzee([6, 6, 6, 6, 3])


def test_1s():
        """tests the "Ones" category, which is the sum of all ones rolled. It tests that the function
         returns the expected value for four different sets of dice"""
        assert Yahtzee.ones(1, 2, 3, 4, 5) == 1
        assert 2 == Yahtzee.ones(1, 2, 1, 4, 5)
        assert 0 == Yahtzee.ones(6, 2, 2, 4, 5)
        assert 4 == Yahtzee.ones(1, 2, 1, 1, 1)


def test_2s():
        """tests the "Twos" category, which is the sum of all twos rolled. It tests that the function
         returns the expected value for two different sets of dice"""
        assert 4 == Yahtzee.twos(1, 2, 3, 2, 6)
        assert 10 == Yahtzee.twos(2, 2, 2, 2, 2)


def test_threes():
        """tests the "Threes" category, which is the sum of all threes rolled. It tests that the function
         returns the expected value for two different sets of dice"""
        assert 6 == Yahtzee.threes(1, 2, 3, 2, 3)
        assert 12 == Yahtzee.threes(2, 3, 3, 3, 3)


def test_fours_test():
        """tests the "Fours" category, which is the sum of all fours rolled. It tests that the function
         returns the expected value for three different sets of dice"""
        assert 12 == Yahtzee(4, 4, 4, 5, 5).fours()
        assert 8 == Yahtzee(4, 4, 5, 5, 5).fours()
        assert 4 == Yahtzee(4, 5, 5, 5, 5).fours()


def test_fives():
        """tests the "Fives" category, which is the sum of all fives rolled. It tests that the function
         returns the expected value for three different sets of dice"""
        assert 10 == Yahtzee(4, 4, 4, 5, 5).fives()
        assert 15 == Yahtzee(4, 4, 5, 5, 5).fives()
        assert 20 == Yahtzee(4, 5, 5, 5, 5).fives()


def test_sixes_test():
        """tests the "Sixes" category, which is the sum of all sixes rolled. It tests that the function
         returns the expected value for three different sets of dice"""
        assert 0 == Yahtzee(4, 4, 4, 5, 5).sixes()
        assert 6 == Yahtzee(4, 4, 6, 5, 5).sixes()
        assert 18 == Yahtzee(6, 5, 6, 6, 5).sixes()


def test_one_pair():
        """tests the "Pair" category, which is the sum of the highest pair. It tests that the function
         returns the expected value for three different sets of dice"""
        assert 6 == Yahtzee.score_pair(3, 4, 3, 5, 6)
        assert 10 == Yahtzee.score_pair(5, 3, 3, 3, 5)
        assert 12 == Yahtzee.score_pair(5, 3, 6, 6, 5)


def test_two_pair():
        """tests the "Two Pairs" category, which is the sum of the two highest pairs. It tests that the function
         returns the expected value for two different sets of dice"""
        assert 16 == Yahtzee.two_pair(3, 3, 5, 4, 5)
        assert 0 == Yahtzee.two_pair(3, 3, 5, 5, 5)


def test_three_of_a_kind():
        """tests the "Three of a Kind" category, which is the sum of three matching dice. It tests that the
         function returns the expected value for three different sets of dice"""
        assert 9 == Yahtzee.three_of_a_kind(3, 3, 3, 4, 5)
        assert 15 == Yahtzee.three_of_a_kind(5, 3, 5, 4, 5)
        assert 0 == Yahtzee.three_of_a_kind(3, 3, 3, 3, 5)


def test_four_of_a_kind():
        """tests the "Four of a Kind" category, which is the sum of four matching dice. It tests that the
         function returns the expected value for three different sets of dice"""
        assert 12 == Yahtzee.four_of_a_kind(3, 3, 3, 3, 5)
        assert 20 == Yahtzee.four_of_a_kind(5, 5, 5, 4, 5)
        assert 0 == Yahtzee.three_of_a_kind(3, 3, 3, 3, 3)


def test_small_straight():
        """tests the "Small Straight" category, which is a sequence of four dice (1-4 or 2-5 or 3-6).
         It tests that the function returns the expected value for two different sets of dice, and 0 for
        a set that does not have a small straight"""
        assert 15 == Yahtzee.smallStraight(1, 2, 3, 4, 5)
        assert 15 == Yahtzee.smallStraight(2, 3, 4, 5, 1)
        assert 0 == Yahtzee.smallStraight(1, 2, 2, 4, 5)


def test_large_straight():
        """ tests the "Large Straight" category, which is a sequence of five dice (1-5 or 2-6).
         It tests that the function returns the expected value for two different sets of dice,
        and 0 for a set that does not have a large straight"""
        assert 20 == Yahtzee.largeStraight(6, 2, 3, 4, 5)
        assert 20 == Yahtzee.largeStraight(2, 3, 4, 5, 6)
        assert 0 == Yahtzee.largeStraight(1, 2, 2, 4, 5)


def test_full_house():
        """tests the "Full House" category, which is three of a kind and a pair. It tests that
         the function returns the expected value for two different sets of dice, and 0 for a set
        that does not have a full house"""
        assert 18 == Yahtzee.fullHouse(6, 2, 2, 2, 6)
        assert 0 == Yahtzee.fullHouse(2, 3, 4, 5, 6)