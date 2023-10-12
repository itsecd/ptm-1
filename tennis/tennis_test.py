# -*- coding: utf-8 -*-

import pytest

from tennis.tennis import TennisGame
from tennis.tennis_unittest import test_cases, play_game


class TestTennis:

    @pytest.mark.parametrize('points_player1 points_player2 score name_player1 name_player2'.split(), test_cases)
    def test_get_score(self, points_player1, points_player2, score, name_player1, name_player2):
        game = play_game(points_player1, points_player2, name_player1, name_player2)
        assert score == game.score()