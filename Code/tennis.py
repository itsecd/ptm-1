# -*- coding: utf-8 -*-

class TennisGameDefactored1:

    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.p_1_points = 0
        self.p_2_points = 0
        
    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.p_1_points += 1
        else:
            self.p_2_points += 1
    
    def score(self):
        result = ""
        temp_score = 0
        if self.p_1_points == self.p_2_points:
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
                3 : "Forty-All",
            }.get(self.p_1_points, "Deuce")
        elif self.p_1_points >= 4 or self.p_2_points >= 4:
            minus_result = self.p_1_points - self.p_2_points
            if minus_result == 1:
                result = "Advantage " + self.player_1_name
            elif minus_result == -1:
                result = "Advantage " + self.player_2_name
            elif minus_result >= 2:
                result = "Win for " + self.player_1_name
            else:
                result = "Win for " + self.player_2_name
        else:
            for i in range(1,3):
                if i == 1:
                    temp_score = self.p_1_points
                else:
                    result += "-"
                    temp_score = self.p_2_points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[temp_score]
        return result


class TennisGameDefactored2:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.p_1_points = 0
        self.p_2_points = 0
        
    def won_point(self, playerName):
        if playerName == self.player_1_name:
            self.p_1_score()
        else:
            self.p_2_score()
    
    def score(self):
        result = ""
        if self.p_1_points == self.p_2_points and self.p_1_points < 4:
            if self.p_1_points == 0:
                result = "Love"
            if self.p_1_points == 1:
                result = "Fifteen"
            if self.p_1_points == 2:
                result = "Thirty"
            if self.p_1_points == 3:
                result = "Forty"
            result += "-All"
        if self.p_1_points == self.p_2_points and self.p_1_points > 3:
            result = "Deuce"
        
        p_1_res = ""
        p_2_res = ""
        if self.p_1_points > 0 and self.p_2_points==0:
            if self.p_1_points == 1:
                p_1_res = "Fifteen"
            if self.p_1_points == 2:
                p_1_res = "Thirty"
            if self.p_1_points == 3:
                p_1_res = "Forty"
            
            p_2_res = "Love"
            result = p_1_res + "-" + p_2_res
        if self.p_2_points > 0 and self.p_1_points == 0:
            if self.p_2_points == 1:
                p_2_res = "Fifteen"
            if self.p_2_points == 2:
                p_2_res = "Thirty"
            if self.p_2_points == 3:
                p_2_res = "Forty"
            
            p_1_res = "Love"
            result = p_1_res + "-" + p_2_res
        
        
        if self.p_1_points > self.p_2_points and self.p_1_points < 4:
            if self.p_1_points == 2:
                p_1_res="Thirty"
            if self.p_1_points == 3:
                p_1_res="Forty"
            if self.p_2_points == 1:
                p_2_res="Fifteen"
            if self.p_2_points == 2:
                p_2_res="Thirty"
            result = p_1_res + "-" + p_2_res
        if self.p_2_points > self.p_1_points and self.p_2_points < 4:
            if self.p_2_points == 2:
                p_2_res="Thirty"
            if self.p_2_points == 3:
                p_2_res="Forty"
            if self.p_1_points == 1:
                p_1_res="Fifteen"
            if self.p_1_points == 2:
                p_1_res="Thirty"
            result = p_1_res + "-" + p_2_res
        
        if self.p_1_points > self.p_2_points and self.p_2_points >= 3:
            result = "Advantage " + self.player_1_name
        
        if self.p_2_points > self.p_1_points and self.p_1_points >= 3:
            result = "Advantage " + self.player_2_name
        
        if self.p_1_points>=4 and self.p_2_points >=0 and (self.p_1_points-self.p_2_points) >= 2:
            result = "Win for " + self.player_1_name
        if self.p_2_points >= 4 and self.p_1_points >= 0 and (self.p_2_points-self.p_1_points) >= 2:
            result = "Win for " + self.player_2_name
        return result
    
    def set_p_1_score(self, number):
        for i in range(number):
            self.p_1_score()
    
    def set_p_2_score(self, number):
        for i in range(number):
            self.p_2_score()
    
    def p_1_score(self):
        self.p_1_points +=1
    
    
    def p_2_score(self):
        self.p_2_points +=1
        
class TennisGameDefactored3:
    def __init__(self, player_1_name, player_2_name):
        self.p_1_name = player_1_name
        self.p_2_name = player_2_name
        self.p_1 = 0
        self.p_2 = 0
        
    def won_point(self, n):
        if n == self.p_1_name:
            self.p_1 += 1
        else:
            self.p_2 += 1
    
    def score(self):
        if self.p_1 < 4 and self.p_2 < 4:
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p_1]
            return s + "-All" if self.p_1 == self.p_2 else s + "-" + p[self.p_2]
        else:
            if self.p_1 == self.p_2:
                return "Deuce"
            s = self.p_1_name if self.p_1 > self.p_2 else self.p_2_name
            return "Advantage " + s if (self.p_1-self.p_2) * (self.p_1-self.p_2) == 1 else "Win for " + s

# NOTE: You must change this to point at the one of the three examples that you're working on!
TennisGame = TennisGameDefactored1
