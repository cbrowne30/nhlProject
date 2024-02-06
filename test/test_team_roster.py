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

from openapi_client.models.team_roster import TeamRoster

class TestTeamRoster(unittest.TestCase):
    """TeamRoster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamRoster:
        """Test TeamRoster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamRoster`
        """
        model = TeamRoster()
        if include_optional:
            return TeamRoster(
                roster = [
                    openapi_client.models.roster.Roster(
                        person = openapi_client.models.roster_person.Roster_person(
                            id = 8466138, 
                            full_name = 'Joe Thornton', 
                            link = '/api/v1/people/8466138', ), 
                        jersey_number = 19, 
                        position = openapi_client.models.draft_prospect_primary_position.DraftProspect_primaryPosition(
                            code = 'C', 
                            name = 'Center', 
                            type = 'Forward', 
                            abbreviation = 'C', ), )
                    ]
            )
        else:
            return TeamRoster(
        )
        """

    def testTeamRoster(self):
        """Test TeamRoster"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
