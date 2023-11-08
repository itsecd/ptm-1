
class TennisGameDefactored1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        data = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All",
        }
        tempScore = 0
        if (self.p1points == self.p2points):
            return data.get(self.p1points, "Deuce")

        if (self.p1points >= 4 or self.p2points >= 4):
            result_dif = self.p1points - self.p2points

            if (result_dif == 1):
                return f"Advantage {self.player1Name}"
            elif (result_dif == -1):
                return f"Advantage {self.player2Name}"
            elif (result_dif >= 2):
                return f"Win for {self.player1Name}"
            else:
                return f"Win for {self.player2Name}"
        for i in range(1, 3):
            if (i == 1):
                tempScore = self.p1points
            else:
                result += "-"
                tempScore = self.p2points
            result += data[tempScore]
        return result


class TennisGameDefactored2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < 4):
            if (self.p1points == 0):
                result = "Love"
            if (self.p1points == 1):
                result = "Fifteen"
            if (self.p1points == 2):
                result = "Thirty"
            if (self.p1points == 3):
                result = "Forty"
            result += "-All"
        if (self.p1points == self.p2points and self.p1points > 3):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points == 0):
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points == 0):
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p1points < 4):
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if (self.p2points > self.p1points and self.p2points < 4):
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name

        if (self.p1points >= 4 and self.p2points >= 0 and (self.p1points-self.p2points) >= 2):
            result = "Win for " + self.player1Name
        if (self.p2points >= 4 and self.p1points >= 0 and (self.p2points-self.p1points) >= 2):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1


class TennisGameDefactored3:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1 = 0
        self.player2 = 0

    def won_point(self, number):
        if number == self.player1Name:
            self.player1 += 1
        else:
            self.player2 += 1

    def score(self):
        if (self.player1 < 4 and self.player2 < 4):
            players = ["Love", "Fifteen", "Thirty", "Forty"]
            s = players[self.player1]
            return s + "-All" if (self.player1 == self.player2) else s + "-" + players[self.player2]
        else:
            if (self.player1 == self.player2):
                return "Deuce"
            s = self.player1Name if self.player1 > self.player2 else self.player2Name
            return "Advantage " + s if ((self.player1-self.player2) * (self.player1-self.player2) == 1) else "Win for " + s
