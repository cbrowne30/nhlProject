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

from openapi_client.models.team_next_game_schedule_dates_inner_games_inner_teams_home import TeamNextGameScheduleDatesInnerGamesInnerTeamsHome

class TestTeamNextGameScheduleDatesInnerGamesInnerTeamsHome(unittest.TestCase):
    """TeamNextGameScheduleDatesInnerGamesInnerTeamsHome unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamNextGameScheduleDatesInnerGamesInnerTeamsHome:
        """Test TeamNextGameScheduleDatesInnerGamesInnerTeamsHome
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamNextGameScheduleDatesInnerGamesInnerTeamsHome`
        """
        model = TeamNextGameScheduleDatesInnerGamesInnerTeamsHome()
        if include_optional:
            return TeamNextGameScheduleDatesInnerGamesInnerTeamsHome(
                league_record = openapi_client.models.team_next_game_schedule_dates_inner_games_inner_teams_home_league_record.Team_nextGameSchedule_dates_inner_games_inner_teams_home_leagueRecord(
                    wins = 28, 
                    losses = 18, 
                    ot = 8, 
                    type = 'league', ),
                score = 2,
                team = openapi_client.models.player_current_team.Player_currentTeam(
                    id = 28, 
                    name = 'San Jose Sharks', 
                    link = '/api/v1/teams/28', )
            )
        else:
            return TeamNextGameScheduleDatesInnerGamesInnerTeamsHome(
        )
        """

    def testTeamNextGameScheduleDatesInnerGamesInnerTeamsHome(self):
        """Test TeamNextGameScheduleDatesInnerGamesInnerTeamsHome"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
