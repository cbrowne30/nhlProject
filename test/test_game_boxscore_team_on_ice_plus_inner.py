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

from openapi_client.models.game_boxscore_team_on_ice_plus_inner import GameBoxscoreTeamOnIcePlusInner

class TestGameBoxscoreTeamOnIcePlusInner(unittest.TestCase):
    """GameBoxscoreTeamOnIcePlusInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameBoxscoreTeamOnIcePlusInner:
        """Test GameBoxscoreTeamOnIcePlusInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameBoxscoreTeamOnIcePlusInner`
        """
        model = GameBoxscoreTeamOnIcePlusInner()
        if include_optional:
            return GameBoxscoreTeamOnIcePlusInner(
                player_id = 8477180,
                shift_duration = 458,
                stamina = 33
            )
        else:
            return GameBoxscoreTeamOnIcePlusInner(
        )
        """

    def testGameBoxscoreTeamOnIcePlusInner(self):
        """Test GameBoxscoreTeamOnIcePlusInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
