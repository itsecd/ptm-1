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
