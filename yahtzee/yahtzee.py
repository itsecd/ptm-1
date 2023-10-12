class Yahtzee:

    @staticmethod
    def chance(dice1, dice2, dice3, dice4, dice5):
        total = 0
        total += dice1
        total += dice2
        total += dice3
        total += dice4
        total += dice5
        return total

    @staticmethod
    def yahtzee(dice):
        counts = [0] * (len(dice)+1)
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
    
    @staticmethod
    def ones(dice1, dice2, dice3, dice4, dice5):
        sum = 0
        if dice1 == 1:
            sum += 1
        if dice2 == 1:
            sum += 1
        if dice3 == 1:
            sum += 1
        if dice4 == 1:
            sum += 1
        if dice5 == 1: 
            sum += 1
        return sum
    
    @staticmethod
    def twos(dice1, dice2, dice3, dice4, dice5):
        sum = 0
        if dice1 == 2:
            sum += 2
        if dice2 == 2:
            sum += 2
        if dice3 == 2:
            sum += 2
        if dice4 == 2:
            sum += 2
        if dice5 == 2:
            sum += 2
        return sum
    
    @staticmethod
    def threes(dice1, dice2, dice3, dice4, dice5):
        s = 0
        if dice1 == 3:
            s += 3
        if dice2 == 3:
            s += 3
        if dice3 == 3:
            s += 3
        if dice4 == 3:
            s += 3
        if dice5 == 3:
            s += 3
        return s

    def __init__(self, dice1, dice2, dice3, dice4, dice5):
        self.dice = [0] * 5
        self.dice[0] = dice1
        self.dice[1] = dice2
        self.dice[2] = dice3
        self.dice[3] = dice4
        self.dice[4] = dice5
    
    def fours(self):
        sum = 0
        for at in range(5):
            if self.dice[at] == 4: 
                sum += 4
        return sum
    
    def fives(self):
        sum = 0
        at = 0
        for at in range(len(self.dice)): 
            if self.dice[at] == 5:
                sum = sum + 5
        return sum

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if self.dice[at] == 6:
                sum = sum + 6
        return sum
    
    @staticmethod
    def one_pair(dice1, dice2, dice3, dice4, dice5):
        counts = [0] * 6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        at = 0
        for at in range(6):
            if counts[6-at-1] == 2:
                return (6-at) * 2
        return 0
    
    @staticmethod
    def two_pair(dice1, dice2, dice3, dice4, dice5):
        counts = [0] * 6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if counts[6-i-1] == 2:
                n = n + 1
                score += (6-i)     
        if n == 2:
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind(dice1, dice2, dice3, dice4, dice5):
        counts = [0] * 6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        for i in range(6):
            if counts[i] == 4:
                return (i+1) * 4
        return 0
    
    @staticmethod
    def three_of_a_kind(dice1, dice2, dice3, dice4, dice5):
        counts = [0] * 6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        for i in range(6):
            if counts[i] == 3:
                return (i+1) * 3
        return 0
    
    @staticmethod
    def small_straight(dice1, dice2, dice3, dice4, dice5):
        counts = [0] * 6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        if (counts[0] == 1 and
            counts[1] == 1 and
            counts[2] == 1 and
            counts[3] == 1 and
            counts[4] == 1):
            return 15
        return 0
    
    @staticmethod
    def large_straight(dice1, dice2, dice3, dice4, dice5):
        counts = [0] * 6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        if (counts[1] == 1 and
            counts[2] == 1 and
            counts[3] == 1 and
            counts[4] == 1
            and counts[5] == 1):
            return 20
        return 0
    
    @staticmethod
    def full_house(dice1, dice2, dice3, dice4, dice5):
        counts = []
        counts = [0] * 6
        counts[dice1-1] += 1
        counts[dice2-1] += 1
        counts[dice3-1] += 1
        counts[dice4-1] += 1
        counts[dice5-1] += 1
        i = 0
        _2 = False
        _2_at = 0
        _3 = False
        _3_at = 0
        for i in range(6):
            if counts[i] == 2: 
                _2 = True
                _2_at = i + 1
        for i in range(6):
            if counts[i] == 3: 
                _3 = True
                _3_at = i + 1
        if _2 and _3:
            return _2_at * 2 + _3_at * 3
        else:
            return 0