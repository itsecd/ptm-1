class Yahtzee:

    @staticmethod
    def chance(dice_1, dice_2, dice_3, dice_4, dice_5):
        total_score = 0
        total_score += dice_1
        total_score += dice_2
        total_score += dice_3
        total_score += dice_4
        total_score += dice_5
        return total_score

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
    def ones(dice_1, dice_2, dice_3, dice_4, dice_5):
        sum = 0
        if (dice_1 == 1):
            sum += 1
        if (dice_2 == 1):
            sum += 1
        if (dice_3 == 1):
            sum += 1
        if (dice_4 == 1):
            sum += 1
        if (dice_5 == 1): 
            sum += 1
        return sum
    
    @staticmethod
    def twos(dice_1, dice_2, dice_3, dice_4, dice_5):
        sum = 0
        if (dice_1 == 2):
            sum += 2
        if (dice_2 == 2):
            sum += 2
        if (dice_3 == 2):
            sum += 2
        if (dice_4 == 2):
            sum += 2
        if (dice_5 == 2):
            sum += 2
        return sum
    
    @staticmethod
    def threes(dice_1, dice_2, dice_3, dice_4, dice_5):
        s = 0
        if (dice_1 == 3):
            s += 3
        if (dice_2 == 3):
            s += 3
        if (dice_3 == 3):
            s += 3
        if (dice_4 == 3):
            s += 3
        if (dice_5 == 3):
            s += 3
        return s
    
    def __init__(self, dice_1, dice_2, dice_3, dice_4, dice_5):
        self.dice = [0] * 5
        self.dice[0] = dice_1
        self.dice[1] = dice_2
        self.dice[2] = dice_3
        self.dice[3] = dice_4
        self.dice[4] = dice_5
    
    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4): 
                sum += 4
        return sum
    
    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                s = s + 5
        return s
    
    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def score_pair(dice_1, dice_2, dice_3, dice_4, dice_5):
        counts = [0] * 6
        counts[dice_1 - 1] += 1
        counts[dice_2 - 1] += 1
        counts[dice_3 - 1] += 1
        counts[dice_4 - 1] += 1
        counts[dice_5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0
    
    @staticmethod
    def two_pair(dice_1, dice_2, dice_3, dice_4, dice_5):
        counts = [0] * 6
        counts[dice_1 - 1] += 1
        counts[dice_2 - 1] += 1
        counts[dice_3 - 1] += 1
        counts[dice_4 - 1] += 1
        counts[dice_5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] == 2):
                n = n + 1
                score += (6 - i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind(dice_1, dice_2, dice_3, dice_4, dice_5):
        counts = [0] * 6
        counts[dice_1 - 1] += 1
        counts[dice_2 - 1] += 1
        counts[dice_3 - 1] += 1
        counts[dice_4 - 1] += 1
        counts[dice_5 - 1] += 1
        for i in range(6):
            if (counts[i] == 4):
                return (i + 1) * 4
        return 0
    
    @staticmethod
    def three_of_a_kind(dice_1, dice_2, dice_3, dice_4, dice_5):
        t = [0] * 6
        t[dice_1 - 1] += 1
        t[dice_2 - 1] += 1
        t[dice_3 - 1] += 1
        t[dice_4 - 1] += 1
        t[dice_5 - 1] += 1
        for i in range(6):
            if (t[i] == 3):
                return (i+1) * 3
        return 0
    
    @staticmethod
    def small_straight(dice_1, dice_2, dice_3, dice_4, dice_5):
        counts = [0] * 6
        counts[dice_1 - 1] += 1
        counts[dice_2 - 1] += 1
        counts[dice_3 - 1] += 1
        counts[dice_4 - 1] += 1
        counts[dice_5 - 1] += 1
        if (counts[0] == 1 and
            counts[1] == 1 and
            counts[2] == 1 and
            counts[3] == 1 and
            counts[4] == 1):
            return 15
        return 0
    
    @staticmethod
    def large_straight(dice_1, dice_2, dice_3, dice_4, dice_5):
        counts = [0] * 6
        counts[dice_1 - 1] += 1
        counts[dice_2 - 1] += 1
        counts[dice_3 - 1] += 1
        counts[dice_4 - 1] += 1
        counts[dice_5 - 1] += 1
        if (counts[1] == 1 and
            counts[2] == 1 and
            counts[3] == 1 and
            counts[4] == 1
            and counts[5] == 1):
            return 20
        return 0
    
    @staticmethod
    def full_house(dice_1, dice_2, dice_3, dice_4, dice_5):
        counts = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        counts = [0] * 6
        counts[dice_1 - 1] += 1
        counts[dice_2 - 1] += 1
        counts[dice_3 - 1] += 1
        counts[dice_4 - 1] += 1
        counts[dice_5 - 1] += 1

        for i in range(6):
            if (counts[i] == 2): 
                _2 = True
                _2_at = i + 1
        for i in range(6):
            if (counts[i] == 3): 
                _3 = True
                _3_at = i + 1
            
        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0