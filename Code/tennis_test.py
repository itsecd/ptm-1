# -*- coding: utf-8 -*-

import pytest
from tennis import TennisGame

from tennis_unittest import test_cases, play_game

class TestTennis:

    @pytest.mark.parametrize('p_1_points p_2_points score p_1_name p_2_name'.split(), test_cases)
    def test_get_score(self, p_1_points, p_2_points, score, p_1_name, p_2_name):
        game = play_game(p_1_points, p_2_points, p_1_name, p_2_name)
        assert score == game.score()
