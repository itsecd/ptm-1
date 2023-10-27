class Yahtzee:

    @staticmethod
    def chance(digits):
        return sum(digits)

    @staticmethod
    def yahtzee(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

    @staticmethod
    def ones_twos_threes(digits, mod):
        sum = 0
        for digit in digits:
            if digit == mod:
                sum += mod
        return sum

    def __init__(self, digits):
        self.dice = digits[:]

    def fours_fives_sixes(self, mod):
        sum = 0
        for elem in self.dice:
            if elem == mod:
                sum += mod
        return sum

    @staticmethod
    def score_pair(digits):
        counts = [0 for i in range(6)]
        for digit in digits:
            counts[digit - 1] += 1
        for index in range(len(counts)):
            if counts[5 - index] == 2:
                return (6 - index) * 2
        return 0

    @staticmethod
    def two_pair(digits):
        counts = [0 for i in range(6)]
        for digit in digits:
            counts[digit - 1] += 1
        counter = 0
        score = 0
        for i in range(len(counts)):
            if counts[5 - i] == 2:
                counter += 1
                score += (6 - i)

        return score * 2 if counter == 2 else 0

    @staticmethod
    def three_four_pair(digits, mod):
        tallies = [0 for i in range(6)]
        for digit in digits:
            tallies[digit - 1] += 1
        for i in range(6):
            if (tallies[i] == mod):
                return (i + 1) * mod
        return 0

    @staticmethod
    def small_straight(digits):
        tallies = [0 for i in range(6)]
        for digit in digits:
            tallies[digit - 1] += 1
        for i in range(4):
            if tallies[i] != 1:
                return 0
        return 15

    @staticmethod
    def large_straight(digits):
        tallies = [0 for i in range(6)]
        for digit in digits:
            tallies[digit - 1] += 1
        for i in range(5):
            if tallies[i] != 1:
                return 0
        return 20

    @staticmethod
    def full_house(digits):
        find_two_flag = False
        find_three_flag = False

        two_index = 0
        three_index = 0

        tallies = [0 for i in range(6)]
        for digit in digits:
            tallies[digit - 1] += 1

        for i in range(6):
            if tallies[i] == 2:
                find_two_flag = True
                two_index = i + 1
            if tallies[i] == 3:
                find_three_flag = True
                three_index = i + 1

        if find_two_flag and find_three_flag:
            return two_index * 2 + three_index * 3
        return 0
