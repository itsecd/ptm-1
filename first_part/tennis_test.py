# -*- coding: utf-8 -*-

import pytest

from first_part.tennis import TennisGame
from first_part.tennis_unitest import test_cases, play_game

class TestTennis:

    @pytest.mark.parametrize('points_player_1 points_player_2 score player_1_name player_2_name'.split(), test_cases)
    def test_get_score(self, points_player_1, points_player_2, score, player_1_name, player_2_name):
        """ Проверяет правильность получения текущего счета в игре тенниса. """
        game = play_game(points_player_1, points_player_2, player_1_name, player_2_name)
        assert score == game.score()