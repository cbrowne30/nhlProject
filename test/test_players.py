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

from openapi_client.models.players import Players

class TestPlayers(unittest.TestCase):
    """Players unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Players:
        """Test Players
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Players`
        """
        model = Players()
        if include_optional:
            return Players(
                copyright = '',
                teams = [
                    openapi_client.models.player.Player(
                        id = 8466138, 
                        full_name = 'Joe Thornton', 
                        link = '/api/v1/people/8466138', 
                        first_name = 'Joe', 
                        last_name = 'Thornton', 
                        primary_number = '19', 
                        birth_date = 'Sun Jul 01 20:00:00 EDT 1979', 
                        current_age = 38, 
                        birth_city = 'London', 
                        birth_state_province = 'ON', 
                        birth_country = 'CAN', 
                        nationality = 'CAN', 
                        height = '6' 4"', 
                        weight = 220, 
                        active = True, 
                        alternate_captain = True, 
                        captain = True, 
                        rookie = True, 
                        shoots_catches = 'L', 
                        roster_status = 'I', 
                        current_team = openapi_client.models.player_current_team.Player_currentTeam(
                            id = 28, 
                            name = 'San Jose Sharks', 
                            link = '/api/v1/teams/28', ), 
                        primary_position = openapi_client.models.draft_prospect_primary_position.DraftProspect_primaryPosition(
                            code = 'C', 
                            name = 'Center', 
                            type = 'Forward', 
                            abbreviation = 'C', ), )
                    ]
            )
        else:
            return Players(
                copyright = '',
        )
        """

    def testPlayers(self):
        """Test Players"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
