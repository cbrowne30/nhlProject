# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.player_stats_stats_inner_splits_inner_stat import PlayerStatsStatsInnerSplitsInnerStat

class TestPlayerStatsStatsInnerSplitsInnerStat(unittest.TestCase):
    """PlayerStatsStatsInnerSplitsInnerStat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerStatsStatsInnerSplitsInnerStat:
        """Test PlayerStatsStatsInnerSplitsInnerStat
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerStatsStatsInnerSplitsInnerStat`
        """
        model = PlayerStatsStatsInnerSplitsInnerStat()
        if include_optional:
            return PlayerStatsStatsInnerSplitsInnerStat(
                time_on_ice = '862:13',
                assists = '23',
                goals = 13,
                pim = 38,
                shots = 75,
                games = 47,
                hits = 32,
                power_play_goals = 7,
                power_play_points = 18,
                power_play_time_on_ice = 1.337,
                even_time_on_ice = 1.337,
                penalty_minutes = 38,
                face_off_pct = 52.04,
                shot_pct = 17.3,
                game_winning_goals = 1,
                over_time_goals = 0,
                short_handed_goals = 0,
                short_handed_points = 0,
                short_handed_time_on_ice = '00:55',
                blocked = 18,
                plus_minus = -9,
                points = 36,
                shifts = 1077,
                time_on_ice_per_game = '18:20',
                even_time_on_ice_per_game = '14:44',
                short_handed_time_on_ice_per_game = '00:01',
                power_play_time_on_ice_per_game = '03:35',
                rank_power_play_goals = '1st',
                rank_blocked_shots = '405th',
                rank_assists = '51st',
                rank_shot_pct = '246th',
                rank_goals = '13th',
                rank_hits = '19th',
                rank_penalty_minutes = '111th',
                rank_short_handed_goals = '133rd',
                rank_plus_minus = '176th',
                rank_shots = '2nd',
                rank_points = '20th',
                rank_overtime_goals = '9th',
                rank_games_played = '1st',
                goals_in_first_period = 6,
                goals_in_second_period = 3,
                goals_in_third_period = 4,
                goals_trailing_by_one = 2,
                goals_trailing_by_two = 1,
                goals_trailing_by_three_plus = 1,
                goals_when_tied = 4,
                goals_leading_by_one = 2,
                goals_leading_by_two = 3
            )
        else:
            return PlayerStatsStatsInnerSplitsInnerStat(
        )
        """

    def testPlayerStatsStatsInnerSplitsInnerStat(self):
        """Test PlayerStatsStatsInnerSplitsInnerStat"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()