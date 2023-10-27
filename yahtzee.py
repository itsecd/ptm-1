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
    def smallStraight(digits):
        tallies = [0 for i in range(6)]
        for digit in digits:
            tallies[digit - 1] += 1
        for i in range(4):
            if tallies[i] != 1:
                return 0
        return 15

    @staticmethod
    def largeStraight(digits):
        tallies = [0 for i in range(6)]
        for digit in digits:
            tallies[digit - 1] += 1
        for i in range(5):
            if tallies[i] != 1:
                return 0
        return 20

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0


if __name__ == "__main__":
    print(Yahtzee.score_pair([5, 3, 3, 3, 5]))
