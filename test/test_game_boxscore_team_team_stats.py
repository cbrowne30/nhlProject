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

from openapi_client.models.game_boxscore_team_team_stats import GameBoxscoreTeamTeamStats

class TestGameBoxscoreTeamTeamStats(unittest.TestCase):
    """GameBoxscoreTeamTeamStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameBoxscoreTeamTeamStats:
        """Test GameBoxscoreTeamTeamStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameBoxscoreTeamTeamStats`
        """
        model = GameBoxscoreTeamTeamStats()
        if include_optional:
            return GameBoxscoreTeamTeamStats(
                team_skater_stats = openapi_client.models.game_boxscore_team_team_stats_team_skater_stats.GameBoxscoreTeam_teamStats_teamSkaterStats(
                    goals = 6, 
                    pim = 6, 
                    shots = 30, 
                    power_play_percentage = '0.0', 
                    power_play_goals = 0, 
                    power_play_opportunities = 1, 
                    face_off_win_percentage = '59.3', 
                    blocked = 21, 
                    takeaways = 9, 
                    giveaways = 6, 
                    hits = 15, )
            )
        else:
            return GameBoxscoreTeamTeamStats(
        )
        """

    def testGameBoxscoreTeamTeamStats(self):
        """Test GameBoxscoreTeamTeamStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
