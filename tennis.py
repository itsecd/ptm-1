# -*- coding: utf-8 -*-

class tennis_game_defactored_one:

    def __init__(self, first_player_name: str, second_player_name: str) -> None:
        '''
        This function initialises players

        Parameters:
            first_player_name: first player name
            second_player_name: second player name
        '''
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.first_player_points = 0
        self.second_player_points = 0
        
    def won_point(self, player_name: str) -> None:
        '''
        This function adds the point to the winner

        Parameters:
            player_name: player name
        '''
        if player_name == self.first_player_name:
            self.first_player_points += 1
        else:
            self.second_player_points += 1
    
    def score(self) -> str:
        '''
        This function calculates the score depend on score of the game

        Returns:
            str: the resulting score
        '''
        result = ""
        temp_score = 0

        if (self.first_player_points == self.second_player_points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
                3: "Forty-All",
                }.get(self.first_player_points, "Deuce")
        elif (self.first_player_points >= 4 or 
              self.second_player_points >= 4):
            sub_result = self.first_player_points - self.second_player_points

            if (sub_result == 1):
                result = "Advantage " + self.first_player_name
            elif (sub_result == -1):
                result = "Advantage " + self.second_player_name
            elif (sub_result >= 2):
                result = "Win for " + self.first_player_name
            else:
                result  ="Win for " + self.second_player_name
        else:
            for i in range(1, 3):
                if (i == 1):
                    temp_score = self.first_player_points
                else:
                    result += "-"
                    temp_score = self.second_player_points

                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                    }[temp_score]
                
        return result


class tennis_game_defactored_two:

    def __init__(self, first_player_name: str, second_player_name: str) -> None:
        '''
        This function initialises players

        Parameters:
            first_player_name: first player name
            second_player_name: second player name
        '''
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.first_player_points = 0
        self.second_player_points = 0

    def won_point(self, player_name: str) -> None:
        '''
        This function adds the point to the winner

        Parameters:
            player_name: player name
        '''
        if player_name == self.first_player_name:
            self.first_player_score()
        else:
            self.second_player_score()

    def score(self) -> str:
        '''
        This function calculates the score depend on score of the game

        Returns:
            str: the resulting score
        '''
        result = ""

        if (self.first_player_points == self.second_player_points and
            self.first_player_points < 4):

            if (self.first_player_points == 0):
                result = "Love"

            if (self.first_player_points == 1):
                result = "Fifteen"

            if (self.first_player_points == 2):
                result = "Thirty"

            if (self.first_player_points == 3):
                result = "Forty"

            result += "-All"

        if (self.first_player_points == self.second_player_points and
            self.first_player_points > 3):
            result = "Deuce"
        
        first_player_result = ""
        second_player_result = ""

        if (self.first_player_points > 0 and self.second_player_points == 0):
            if (self.first_player_points == 1):
                first_player_result = "Fifteen"

            if (self.first_player_points == 2):
                first_player_result = "Thirty"

            if (self.first_player_points == 3):
                first_player_result = "Forty"
            
            second_player_result = "Love"
            result = first_player_result + "-" + second_player_result

        if (self.second_player_points > 0 and self.first_player_points == 0):
            if (self.second_player_points == 1):
                second_player_result = "Fifteen"

            if (self.second_player_points == 2):
                second_player_result = "Thirty"

            if (self.second_player_points == 3):
                second_player_result = "Forty"
            
            first_player_result = "Love"
            result = first_player_result + "-" + second_player_result

        if (self.first_player_points > self.second_player_points and
            self.first_player_points < 4):
            if (self.first_player_points == 2):
                first_player_result = "Thirty"

            if (self.first_player_points == 3):
                first_player_result = "Forty"

            if (self.second_player_points == 1):
                second_player_result = "Fifteen"

            if (self.second_player_points == 2):
                second_player_result = "Thirty"

            result = first_player_result + "-" + second_player_result

        if (self.second_player_points > self.first_player_points and
            self.second_player_points < 4):
            if (self.second_player_points == 2):
                second_player_result = "Thirty"

            if (self.second_player_points == 3):
                second_player_result = "Forty"

            if (self.first_player_points == 1):
                first_player_result = "Fifteen"

            if (self.first_player_points == 2):
                first_player_result = "Thirty"

            result = first_player_result + "-" + second_player_result

        if (self.first_player_points > self.second_player_points and
            self.second_player_points >= 3):
            result = "Advantage " + self.first_player_name

        if (self.second_player_points > self.first_player_points and
            self.first_player_points >= 3):
            result = "Advantage " + self.second_player_name
        
        if (self.first_player_points >= 4 and
            self.second_player_points >= 0 and
            (self.first_player_points - self.second_player_points) >= 2):
            result = "Win for " + self.first_player_name

        if (self.second_player_points >= 4 and
            self.first_player_points >= 0 and
            (self.second_player_points - self.first_player_points) >= 2):
            result = "Win for " + self.second_player_name

        return result

    def set_first_player_score(self, number: int) -> None:
        '''
        This function sets the first player score

        Parameters:
            number: points amount
        '''
        for i in range(number):
            self.first_player_score()

    def set_second_player_number(self, number: int) -> None:
        '''
        This function sets the second player score

        Parameters:
            number: points amount
        '''
        for i in range(number):
            self.second_player_score()

    def first_player_score(self) -> None:
        '''
        This function adds one point to the first player
        '''
        self.first_player_points += 1

    def second_player_score(self) -> None:
        '''
        This function adds one point to the second player
        '''
        self.second_player_points += 1


class tennis_game_defactored_three:

    def __init__(self, first_player_name: str, second_player_name: str) -> None:
        '''
        This function initialises players

        Parameters:
            first_player_name: first player name
            second_player_name: second player name
        '''
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.first_player = 0
        self.second_player = 0

    def won_point(self, name: str) -> None:
        '''
        This function adds the point to the winner

        Parameters:
            player_name: player name
        '''
        if name == self.first_player_name:
            self.first_player += 1
        else:
            self.second_player += 1

    def score(self) -> str:
        '''
        This function calculates the score depend on score of the game

        Returns:
            str: the resulting score
        '''
        if (self.first_player < 4 and self.second_player < 4):
            amount = ["Love", "Fifteen", "Thirty", "Forty"]
            source = amount[self.first_player]

            if(self.first_player == self.second_player):
                return source + "-All"
            else:
                return source + "-" + amount[self.second_player]
        else:
            if (self.first_player == self.second_player):
                return "Deuce"

            if(self.first_player > self.second_player):
                source = self.first_player_name
            else:
                source = self.second_player_name

            if((self.first_player - self.second_player) \
               * (self.first_player - self.second_player) == 1):
                return "Advantage " + source
            else:
                return "Win for " + source


tennis_game = tennis_game_defactored_one