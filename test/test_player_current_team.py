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

from openapi_client.models.player_current_team import PlayerCurrentTeam

class TestPlayerCurrentTeam(unittest.TestCase):
    """PlayerCurrentTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerCurrentTeam:
        """Test PlayerCurrentTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerCurrentTeam`
        """
        model = PlayerCurrentTeam()
        if include_optional:
            return PlayerCurrentTeam(
                id = 28,
                name = 'San Jose Sharks',
                link = '/api/v1/teams/28'
            )
        else:
            return PlayerCurrentTeam(
        )
        """

    def testPlayerCurrentTeam(self):
        """Test PlayerCurrentTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()