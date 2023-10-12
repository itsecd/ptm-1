# -*- coding: utf-8 -*-

import unittest

from tennis.tennis import TennisGame


test_cases = [
    (0, 0, "Love-All", 'player1', 'player2'),
    (1, 1, "Fifteen-All", 'player1', 'player2'),
    (2, 2, "Thirty-All", 'player1', 'player2'),
    (3, 3, "Forty-All", 'player1', 'player2'),
    (4, 4, "Deuce", 'player1', 'player2'),

    (1, 0, "Fifteen-Love", 'player1', 'player2'),
    (0, 1, "Love-Fifteen", 'player1', 'player2'),
    (2, 0, "Thirty-Love", 'player1', 'player2'),
    (0, 2, "Love-Thirty", 'player1', 'player2'),
    (3, 0, "Forty-Love", 'player1', 'player2'),
    (0, 3, "Love-Forty", 'player1', 'player2'),
    (4, 0, "Win for player1", 'player1', 'player2'),
    (0, 4, "Win for player2", 'player1', 'player2'),

    (2, 1, "Thirty-Fifteen", 'player1', 'player2'),
    (1, 2, "Fifteen-Thirty", 'player1', 'player2'),
    (3, 1, "Forty-Fifteen", 'player1', 'player2'),
    (1, 3, "Fifteen-Forty", 'player1', 'player2'),
    (4, 1, "Win for player1", 'player1', 'player2'),
    (1, 4, "Win for player2", 'player1', 'player2'),

    (3, 2, "Forty-Thirty", 'player1', 'player2'),
    (2, 3, "Thirty-Forty", 'player1', 'player2'),
    (4, 2, "Win for player1", 'player1', 'player2'),
    (2, 4, "Win for player2", 'player1', 'player2'),

    (4, 3, "Advantage player1", 'player1', 'player2'),
    (3, 4, "Advantage player2", 'player1', 'player2'),
    (5, 4, "Advantage player1", 'player1', 'player2'),
    (4, 5, "Advantage player2", 'player1', 'player2'),
    (15, 14, "Advantage player1", 'player1', 'player2'),
    (14, 15, "Advantage player2", 'player1', 'player2'),

    (6, 4, 'Win for player1', 'player1', 'player2'), 
    (4, 6, 'Win for player2', 'player1', 'player2'), 
    (16, 14, 'Win for player1', 'player1', 'player2'), 
    (14, 16, 'Win for player2', 'player1', 'player2'), 

    (6, 4, 'Win for One', 'One', 'player2'),
    (4, 6, 'Win for Two', 'player1', 'Two'), 
    (6, 5, 'Advantage One', 'One', 'player2'),
    (5, 6, 'Advantage Two', 'player1', 'Two'), 
    ]


def play_game(points_player1, points_player2, name_player1, name_player2):
    game = TennisGame(name_player1, name_player2)
    for i in range(max(points_player1, points_player2)):
        if i < points_player1:
            game.won_point(name_player1)
        if i < points_player2:
            game.won_point(name_player2)
    return game


class TestTennis(unittest.TestCase):
     
    def test_score(self):
        for testcase in test_cases:
            (points_player1, points_player2, score, name_player1, name_player2) = testcase
            game = play_game(points_player1, points_player2, name_player1, name_player2)
            self.assertEquals(score, game.score())
 

if __name__ == "__main__":
    unittest.main()  