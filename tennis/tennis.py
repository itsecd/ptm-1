# -*- coding: utf-8 -*-

class TennisGameDefactored1:

    def __init__(self, name_player1, name_player2):
        self.name_player1 = name_player1
        self.name_player2 = name_player2
        self.points_player1 = 0
        self.points_player2 = 0
        
    def won_point(self, name_player):
        if name_player == self.name_player1:
            self.points_player1 += 1
        else:
            self.points_player2 += 1
    
    def score(self):
        result = ""
        temp_score = 0
        if self.points_player1 == self.points_player2:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
                3: "Forty-All",
            }.get(self.points_player1, "Deuce")
        elif self.points_player1 >= 4 or self.points_player2 >= 4:
            minus_result = self.points_player1 - self.points_player2
            if minus_result == 1:
                result = "Advantage " + self.name_player1
            elif minus_result == -1:
                result = "Advantage " + self.name_player2
            elif minus_result >= 2:
                result = "Win for " + self.name_player1
            else:
                result = "Win for " + self.name_player2
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.points_player1
                else:
                    result += "-"
                    temp_score = self.points_player2
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result


class TennisGameDefactored2:

    def __init__(self, name_player1, name_player2):
        self.name_player1 = name_player1
        self.name_player2 = name_player2
        self.points_player1 = 0
        self.points_player2 = 0
        
    def won_point(self, name_player):
        if name_player == self.name_player1:
            self.score_player1()
        else:
            self.score_player2()
    
    def score(self):
        result = ""
        if self.points_player1 == self.points_player2 and self.points_player1 < 4:
            if self.points_player1 == 0:
                result = "Love"
            if self.points_player1 == 1:
                result = "Fifteen"
            if self.points_player1 == 2:
                result = "Thirty"
            if self.points_player1 == 3:
                result = "Forty"
            result += "-All"
        if self.points_player1 == self.points_player2 and self.points_player1 > 3:
            result = "Deuce"
        
        result_player1 = ""
        result_player2 = ""
        if self.points_player1 > 0 and self.points_player2 == 0:
            if self.points_player1 == 1:
                result_player1 = "Fifteen"
            if self.points_player1 == 2:
                result_player1 = "Thirty"
            if self.points_player1 == 3:
                result_player1 = "Forty"
            result_player2 = "Love"
            result = result_player1 + "-" + result_player2

        if self.points_player2 > 0 and self.points_player1 == 0:
            if self.points_player2 == 1:
                result_player2 = "Fifteen"
            if self.points_player2 == 2:
                result_player2 = "Thirty"
            if self.points_player2 == 3:
                result_player2 = "Forty"
            result_player1 = "Love"
            result = result_player1 + "-" + result_player2

        if self.points_player1 > self.points_player2 and self.points_player1 < 4:
            if self.points_player1 == 2:
                result_player1 = "Thirty"
            if self.points_player1 == 3:
                result_player1 = "Forty"
            if self.points_player2 == 1:
                result_player2 = "Fifteen"
            if self.points_player2 == 2:
                result_player2 = "Thirty"
            result = result_player1 + "-" + result_player2

        if self.points_player2 > self.points_player1 and self.points_player2 < 4:
            if self.points_player2 == 2:
                result_player2 = "Thirty"
            if self.points_player2 == 3:
                result_player2 = "Forty"
            if self.points_player1 == 1:
                result_player1 = "Fifteen"
            if self.points_player1 == 2:
                result_player1 = "Thirty"
            result = result_player1 + "-" + result_player2
        
        if self.points_player1 > self.points_player2 and self.points_player2 >= 3:
            result = "Advantage " + self.name_player1
        if self.points_player2 > self.points_player1 and self.points_player1 >= 3:
            result = "Advantage " + self.name_player2
        
        if self.points_player1 >= 4 and self.points_player2 >= 0 and self.points_player1 - self.points_player2 >= 2:
            result = "Win for " + self.name_player1
        if self.points_player2 >= 4 and self.points_player1 >= 0 and self.points_player2 - self.points_player1 >= 2:
            result = "Win for " + self.name_player2
        return result
    
    def set_score_player1(self, number):
        for i in range(number):
            self.score_player1()
    
    def set_score_player2(self, number):
        for i in range(number):
            self.score_player2()
    
    def score_player1(self):
        self.points_player1 += 1
    
    def score_player2(self):
        self.points_player2 += 1
        

class TennisGameDefactored3:
    
    def __init__(self, name_player1, name_player2):
        self.name_player1 = name_player1
        self.name_player2 = name_player2
        self.points_player1 = 0
        self.points_player2 = 0
        
    def won_point(self, name_player):
        if name_player == self.name_player1:
            self.points_player1 += 1
        else:
            self.points_player2 += 1
    
    def score(self):
        if self.points_player1 < 4 and self.points_player2 < 4:
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            result = points[self.points_player1]
            return result + "-All" if self.points_player1 == self.points_player2 else result + "-" + points[self.points_player2]
        else:
            if self.points_player1 == self.points_player2:
                return "Deuce"
            result = self.name_player1 if self.points_player1 > self.points_player2 else self.name_player2
            return "Advantage " + result if (self.points_player1-self.points_player2) * (self.points_player1-self.points_player2) == 1 else "Win for " + result

# NOTE: You must change this to point at the one of the three examples that you're working on!
TennisGame = TennisGameDefactored1