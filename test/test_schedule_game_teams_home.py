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

from openapi_client.models.schedule_game_teams_home import ScheduleGameTeamsHome

class TestScheduleGameTeamsHome(unittest.TestCase):
    """ScheduleGameTeamsHome unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleGameTeamsHome:
        """Test ScheduleGameTeamsHome
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleGameTeamsHome`
        """
        model = ScheduleGameTeamsHome()
        if include_optional:
            return ScheduleGameTeamsHome(
                league_record = openapi_client.models.schedule_game_teams_home_league_record.ScheduleGame_teams_home_leagueRecord(
                    wins = 29, 
                    losses = 18, 
                    ot = 8, 
                    type = 'league', ),
                score = 6,
                team = openapi_client.models.player_current_team.Player_currentTeam(
                    id = 28, 
                    name = 'San Jose Sharks', 
                    link = '/api/v1/teams/28', )
            )
        else:
            return ScheduleGameTeamsHome(
        )
        """

    def testScheduleGameTeamsHome(self):
        """Test ScheduleGameTeamsHome"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
