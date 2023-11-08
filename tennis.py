
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
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        data = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        if (self.p1points == self.p2points and self.p1points < 4):
            result = f"{data[self.p1points]}-All"
        if (self.p1points == self.p2points and self.p1points > 3):
            result = "Deuce"

        player1res = ""
        player2res = ""
        if (self.p1points > 0 and self.p2points == 0):
            player1res = f"{data[self.p1points]}"
            player2res = "Love"
            result = f"{player1res}-{player2res}"

        if (self.p2points > 0 and self.p1points == 0):

            player2res = f"{data[self.p2points]}"
            player1res = "Love"
            result = f"{player1res}-{player2res}"

        if (self.p1points > self.p2points and self.p1points < 4) or (self.p2points > self.p1points and self.p2points < 4):

            player1res = f"{data[self.p1points]}"
            player2res = f"{data[self.p2points]}"

            result = f"{player1res}-{player2res}"

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name

        if (self.p1points >= 4 and self.p2points >= 0 and self.p1points-self.p2points >= 2):
            result = "Win for " + self.player1Name
        if (self.p2points >= 4 and self.p1points >= 0 and self.p2points-self.p1points >= 2):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        self.p1points += number

    def SetP2Score(self, number):
        self.p2points += number


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
