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

from openapi_client.models.game_boxscore_team_team import GameBoxscoreTeamTeam

class TestGameBoxscoreTeamTeam(unittest.TestCase):
    """GameBoxscoreTeamTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameBoxscoreTeamTeam:
        """Test GameBoxscoreTeamTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameBoxscoreTeamTeam`
        """
        model = GameBoxscoreTeamTeam()
        if include_optional:
            return GameBoxscoreTeamTeam(
                id = 28,
                name = 'San Jose Sharks',
                link = '/api/v1/teams/28',
                abbreviation = 'SJS',
                tri_code = 'SJS'
            )
        else:
            return GameBoxscoreTeamTeam(
        )
        """

    def testGameBoxscoreTeamTeam(self):
        """Test GameBoxscoreTeamTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
