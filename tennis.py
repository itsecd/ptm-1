

class TennisGameDefactored1:

    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.points_player_1 = 0
        self.points_player_2 = 0

    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.points_player_1 += 1
        else:
            self.points_player_2 += 1

    def score(self):
        result = ""
        temp_score = 0
        if (self.points_player_1 == self.points_player_2):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
                3: "Forty-All",
            }.get(self.points_player_1, "Deuce")
        elif (self.points_player_1 >= 4 or self.points_player_2 >= 4):
            minus_result = self.points_player_1 - self.points_player_2
            if (minus_result == 1):
                result = "Advantage " + self.player_1_name
            elif (minus_result == -1):
                result = "Advantage " + self.player_2_name
            elif (minus_result >= 2):
                result = "Win for " + self.player_1_name
            else:
                result = "Win for " + self.player_2_name
        else:
            for i in range(1, 3):
                if (i == 1):
                    temp_score = self.points_player_1
                else:
                    result += "-"
                    temp_score = self.points_player_2
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result


class TennisGameDefactored2:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.points_player_1 = 0
        self.points_player_2 = 0
        
    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.score_player_1()
        else:
            self.score_player_2()
    
    def score(self):
        result = ""
        if (self.points_player_1 == self.points_player_2 and self.points_player_1 < 4):
            if (self.points_player_1 == 0):
                result = "Love"
            if (self.points_player_1 == 1):
                result = "Fifteen"
            if (self.points_player_1 == 2):
                result = "Thirty"
            if (self.points_player_1 == 3):
                result = "Forty"
            result += "-All"
        if (self.points_player_1==self.points_player_2 and self.points_player_1 > 3):
            result = "Deuce"
        
        result_player_1 = ""
        result_player_2 = ""
        if (self.points_player_1 > 0 and self.points_player_2 == 0):
            if (self.points_player_1 == 1):
                result_player_1 = "Fifteen"
            if (self.points_player_1 == 2):
                result_player_1 = "Thirty"
            if (self.points_player_1 == 3):
                result_player_1 = "Forty"
            result_player_2 = "Love"
            result = result_player_1 + "-" + result_player_2

        if (self.points_player_2 > 0 and self.points_player_1 == 0):
            if (self.points_player_2 == 1):
                result_player_2 = "Fifteen"
            if (self.points_player_2 == 2):
                result_player_2 = "Thirty"
            if (self.points_player_2 == 3):
                result_player_2 = "Forty"
            result_player_1 = "Love"
            result = result_player_1 + "-" + result_player_2
        
        if (self.points_player_1 > self.points_player_2 and self.points_player_1 < 4):
            if (self.points_player_1 == 2):
                result_player_1 = "Thirty"
            if (self.points_player_1 == 3):
                result_player_1 = "Forty"
            if (self.points_player_2 == 1):
                result_player_2 = "Fifteen"
            if (self.points_player_2 == 2):
                result_player_2 = "Thirty"
            result = result_player_1 + "-" + result_player_2
        
        if (self.points_player_2 > self.points_player_1 and self.points_player_2 < 4):
            if (self.points_player_2 == 2):
                result_player_2 = "Thirty"
            if (self.points_player_2 == 3):
                result_player_2 = "Forty"
            if (self.points_player_1 == 1):
                result_player_1 = "Fifteen"
            if (self.points_player_1 == 2):
                result_player_1 = "Thirty"
            result = result_player_1 + "-" + result_player_2
        
        if (self.points_player_1 > self.points_player_2 and self.points_player_2 >= 3):
            result = "Advantage " + self.player_1_name
        if (self.points_player_2 > self.points_player_1 and self.points_player_1 >= 3):
            result = "Advantage " + self.player_2_name
        
        if (self.points_player_1 >=4 and self.points_player_2 >=0 and (self.points_player_1 - self.points_player_2) >= 2):
            result = "Win for " + self.player_1_name
        if (self.points_player_2 >=4 and self.points_player_1 >=0 and (self.points_player_2 - self.points_player_1) >=2):
            result = "Win for " + self.player_2_name
        return result
    
    def set_score_player_1(self, number):
        for i in range(number):
            self.score_player_1()
    
    def set_score_player_2(self, number):
        for i in range(number):
            self.score_player_2()
    
    def score_player_1(self):
        self.points_player_1 +=1
    
    def score_player_2(self):
        self.points_player_2 +=1
        
        
class TennisGameDefactored3:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.points_player_1 = 0
        self.points_player_2  = 0
        
    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.points_player_1 += 1
        else:
            self.points_player_2 += 1
    
    def score(self):
        if (self.points_player_1 < 4 and self.points_player_2  < 4):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            score = points[self.points_player_1]
            return score + "-All" if (self.points_player_1 == self.points_player_2 ) else score + "-" + points[self.points_player_2 ]
        else:
            if (self.points_player_1 == self.points_player_2 ):
                return "Deuce"
            score = self.player_1_name if self.points_player_1 > self.points_player_2  else self.player_2_name
            return "Advantage " + score if ((self.points_player_1-self.points_player_2 )*(self.points_player_1-self.points_player_2 ) == 1) else "Win for " + s

TennisGame = TennisGameDefactored1