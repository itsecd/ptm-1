class Yahtzee:

    @staticmethod
    def init_score(dice_1, dice_2, dice_3, dice_4, dice_5):
        total_score = 0
        total_score += dice_1
        total_score += dice_2
        total_score += dice_3
        total_score += dice_4
        total_score += dice_5
        return total_score

    @staticmethod
    def check_for_five_identical_dice(dice):
        count = [0]*(len(dice)+1)
        for one_dice in dice:
            count[one_dice-1] += 1

        for i in range(len(count)):
            if count[i] == 5:
                return 50
        return 0
    
    @staticmethod
    def check_for_ones( dice_1,  dice_2,  dice_3,  dice_4,  dice_5):
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
    def check_for_twos( dice_1,  dice_2,  dice_3,  dice_4,  dice_5):
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
    def check_for_threes( dice_1,  dice_2,  dice_3,  dice_4,  dice_5):
        sum = 0
        if (dice_1 == 3):
             sum += 3
        if (dice_2 == 3):
             sum += 3
        if (dice_3 == 3):
             sum += 3
        if (dice_4 == 3):
             sum += 3
        if (dice_5 == 3):
             sum += 3
        return sum

    def __init__(self, dice_1, dice_2, dice_3, dice_4, dice_5):
        self.dice = [0]*5
        self.dice[0] = dice_1
        self.dice[1] = dice_2
        self.dice[2] = dice_3
        self.dice[3] = dice_4
        self.dice[4] = dice_5
    
    def check_for_fours(self):
        sum = 0
        for i in range(5):
            if (self.dice[i] == 4): 
                sum += 4
        return sum    

    def check_for_fives(self):
        sum = 0
        i = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                sum = sum + 5
        return sum    

    def check_for_sixes(self):
        sum = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def check_for_pairs( dice_1,  dice_2,  dice_3,  dice_4,  dice_5):
        count = [0]*6
        count[dice_1-1] += 1
        count[dice_2-1] += 1
        count[dice_3-1] += 1
        count[dice_4-1] += 1
        count[dice_5-1] += 1
        i = 0
        for i in range(6):
            if (count[6-i-1] == 2):
                return (6-i)*2
        return 0
    
    @staticmethod
    def check_for_two_pairs( dice_1,  dice_2,  dice_3,  dice_4,  dice_5):
        count = [0]*6
        count[dice_1-1] += 1
        count[dice_2-1] += 1
        count[dice_3-1] += 1
        count[dice_4-1] += 1
        count[dice_5-1] += 1
        pairs_count = 0
        score = 0
        for i in range(6):
            if (count[6-i-1] == 2):
                pairs_count = pairs_count+1
                score += (6-i)
                    
        if (pairs_count == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def check_for_four_identical_dice( dice_1,  dice_2,  dice_3,  
                                       dice_4,  dice_5):
        count = [0]*6
        count[dice_1-1] += 1
        count[dice_2-1] += 1
        count[dice_3-1] += 1
        count[dice_4-1] += 1
        count[dice_5-1] += 1
        for i in range(6):
            if (count[i] == 4):
                return (i+1) * 4
        return 0    

    @staticmethod
    def check_for_three_identical_dice( dice_1,  dice_2,  dice_3,
                                        dice_4,  dice_5):
        count = [0]*6
        count[dice_1-1] += 1
        count[dice_2-1] += 1
        count[dice_3-1] += 1
        count[dice_4-1] += 1
        count[dice_5-1] += 1
        for i in range(6):
            if (count[i] == 3):
                return (i+1) * 3
        return 0    

    @staticmethod
    def check_for_small_straight( dice_1,  dice_2,  dice_3,  dice_4,  dice_5):
        count = [0]*6
        count[dice_1-1] += 1
        count[dice_2-1] += 1
        count[dice_3-1] += 1
        count[dice_4-1] += 1
        count[dice_5-1] += 1
        if (count[0] == 1 and
            count[1] == 1 and
            count[2] == 1 and
            count[3] == 1 and
            count[4] == 1):
            return 15
        return 0    

    @staticmethod
    def check_for_large_straight( dice_1,  dice_2,  dice_3,  dice_4,  dice_5):
        count = [0]*6
        count[dice_1-1] += 1
        count[dice_2-1] += 1
        count[dice_3-1] += 1
        count[dice_4-1] += 1
        count[dice_5-1] += 1
        if (count[1] == 1 and
            count[2] == 1 and
            count[3] == 1 and
            count[4] == 1
            and count[5] == 1):
            return 20
        return 0    

    @staticmethod
    def check_for_full_house( d1,  d2,  d3,  d4,  d5):
        count = []
        one_pair = False
        i = 0
        pair_number = 0
        one_triple = False
        triple_number = 0
        count = [0]*6
        count[d1-1] += 1
        count[d2-1] += 1
        count[d3-1] += 1
        count[d4-1] += 1
        count[d5-1] += 1

        for i in range(6):
            if (count[i] == 2): 
                one_pair = True
                pair_number = i+1
        for i in range(6):
            if (count[i] == 3): 
                one_triple = True
                triple_number = i+1
            
        if (one_pair and one_triple):
            return pair_number * 2 + triple_number * 3
        else:
            return 0