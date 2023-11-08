
class TennisGameDefactored3:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1points = 0
        self.player2points = 0

    def won_point(self, name):
        if name == self.player1Name:
            self.player1points += 1
        else:
            self.player2points += 1

    def score(self):
        if (self.player1points < 4 and self.player2points < 4):
            players = ["Love", "Fifteen", "Thirty", "Forty"]
            result = players[self.player1points]
            return result + "-All" if (self.player1points == self.player2points) else result + "-" + players[self.player2points]
        else:
            if (self.player1points == self.player2points):
                return "Deuce"
            result = self.player1Name if self.player1points > self.player2points else self.player2Name
            return "Advantage " + result if ((self.player1points-self.player2points) * (self.player1points-self.player2points) == 1) else "Win for " + result
