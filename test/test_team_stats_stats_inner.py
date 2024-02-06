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

from openapi_client.models.team_stats_stats_inner import TeamStatsStatsInner

class TestTeamStatsStatsInner(unittest.TestCase):
    """TeamStatsStatsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamStatsStatsInner:
        """Test TeamStatsStatsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamStatsStatsInner`
        """
        model = TeamStatsStatsInner()
        if include_optional:
            return TeamStatsStatsInner(
                type = openapi_client.models.team_stats_stats_inner_type.TeamStats_stats_inner_type(
                    display_name = 'statsSingleSeason', ),
                splits = [
                    openapi_client.models.team_stats_stats_inner_splits_inner.TeamStats_stats_inner_splits_inner(
                        stat = openapi_client.models.team_stats_stats_inner_splits_inner_stat.TeamStats_stats_inner_splits_inner_stat(
                            games_played = 55, 
                            wins = 29, 
                            losses = 18, 
                            ot = 8, 
                            pts = 66, 
                            pt_pctg = '60.0', 
                            goals_per_game = 2.891, 
                            goals_against_per_game = 2.745, 
                            ev_gga_ratio = 0.8532, 
                            power_play_percentage = '23.9', 
                            power_play_goals = 44, 
                            power_play_goals_against = 26, 
                            power_play_opportunities = 184, 
                            penalty_kill_percentage = '84.6', 
                            shots_per_game = 32.8, 
                            shots_allowed = 30.2182, 
                            win_score_first = 0.679, 
                            win_opp_score_first = 0.37, 
                            win_lead_first_per = 0.85, 
                            win_lead_second_per = 0.952, 
                            win_outshoot_opp = 0.467, 
                            win_outshot_by_opp = 0.6, 
                            face_offs_taken = 3300, 
                            face_offs_won = 1675, 
                            face_offs_lost = 1625, 
                            face_off_win_percentage = '50.8', 
                            shooting_pctg = 8.8, 
                            save_pctg = 0.909, ), 
                        team = openapi_client.models.player_current_team.Player_currentTeam(
                            id = 28, 
                            name = 'San Jose Sharks', 
                            link = '/api/v1/teams/28', ), )
                    ]
            )
        else:
            return TeamStatsStatsInner(
        )
        """

    def testTeamStatsStatsInner(self):
        """Test TeamStatsStatsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
