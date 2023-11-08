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
