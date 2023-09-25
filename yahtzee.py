class Yahtzee:
    @staticmethod
    def chance(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        total = 0
        total += d1
        total += d2
        total += d3
        total += d4
        total += d5
        return total

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
    def ones(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        sum = 0
        if d1 == 1:
            sum += 1
        if d2 == 1:
            sum += 1
        if d3 == 1:
            sum += 1
        if d4 == 1:
            sum += 1
        if d5 == 1:
            sum += 1
        return sum

    @staticmethod
    def twos(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        sum = 0
        if d1 == 2:
            sum += 2
        if d2 == 2:
            sum += 2
        if d3 == 2:
            sum += 2
        if d4 == 2:
            sum += 2
        if d5 == 2:
            sum += 2
        return sum

    @staticmethod
    def threes(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        sum = 0
        if d1 == 3:
            sum += 3
        if d2 == 3:
            sum += 3
        if d3 == 3:
            sum += 3
        if d4 == 3:
            sum += 3
        if d5 == 3:
            sum += 3
        return sum

    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int) -> None:
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5

    def fours(self) -> int:
        sum = 0
        for at in range(5):
            if self.dice[at] == 4:
                sum += 4
        return sum

    def fives(self) -> int:
        sum = 0
        for i in range(len(self.dice)):
            if self.dice[i] == 5:
                sum = sum + 5
        return sum

    def sixes(self) -> int:
        sum = 0
        for at in range(len(self.dice)):
            if self.dice[at] == 6:
                sum = sum + 6
        return sum

    @staticmethod
    def score_pair(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        for at in range(6):
            if counts[6 - at - 1] == 2:
                return (6 - at) * 2
        return 0

    @staticmethod
    def two_pair(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if counts[6 - i - 1] == 2:
                n = n + 1
                score += (6 - i)
        if n == 2:
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] == 4:
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] == 3:
                return (i + 1) * 3
        return 0

    @staticmethod
    def small_straight(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def large_straight(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1 and
                tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def full_house(d1: int, d2: int, d3: int, d4: int, d5: int) -> int:
        double_flag = False
        double_value = 0
        triple_flag = False
        triple_value = 0
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] == 2:
                double_flag = True
                double_value = i + 1
        for i in range(6):
            if tallies[i] == 3:
                triple_flag = True
                triple_value = i + 1
        if double_flag and triple_flag:
            return double_value * 2 + triple_value * 3
        else:
            return 0