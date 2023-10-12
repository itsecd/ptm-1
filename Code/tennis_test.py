# -*- coding: utf-8 -*-

import pytest
from tennis import TennisGame

from tennis_unittest import test_cases, play_game

class TestTennis:
    @pytest.mark.parametrize('p_1_points p_2_points score p_1_name p_2_name'.split(), test_cases)
    def test_get_score(self, p_1_points:int, p_2_points:int, score:int, p_1_name:str, p_2_name:str):
        """A test if returned value equals to expected ones

        Args:
            p_1_points (int): Player 1 game score
            p_2_points (int): Player 2 game score
            score (int): _description_
            p_1_name (str): Player 1 nickname
            p_2_name (str): Player 2 nickname
        """
        game = play_game(p_1_points, p_2_points, p_1_name, p_2_name)
        assert score == game.score()
