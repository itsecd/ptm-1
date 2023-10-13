# -*- coding: utf-8 -*-

import unittest

from tennis import TennisGame

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

def play_game(points_player_1, points_player_2, player_1_name, player_2_name):
    """ Воспроизводит игру с заданными очками и именами игроков. """
    game = TennisGame(player_1_name, player_2_name)
    for i in range(max(points_player_1, points_player_2)):
        if i < points_player_1:
            game.won_point(player_1_name)
        if i < points_player_2:
            game.won_point(player_2_name)
    return game

class TestTennis(unittest.TestCase):
     
    def test_Score(self):
        """ Проверяет правильность получения текущего счета в игре тенниса. """
        for testcase in test_cases:
            (points_player_1, points_player_2, score, player_1_name, player_2_name) = testcase
            game = play_game(points_player_1, points_player_2, player_1_name, player_2_name)
            self.assertEquals(score, game.score())
 
if __name__ == "__main__":
    unittest.main() 
        