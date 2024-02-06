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

from openapi_client.models.schedule_game_teams_away_league_record import ScheduleGameTeamsAwayLeagueRecord

class TestScheduleGameTeamsAwayLeagueRecord(unittest.TestCase):
    """ScheduleGameTeamsAwayLeagueRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleGameTeamsAwayLeagueRecord:
        """Test ScheduleGameTeamsAwayLeagueRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleGameTeamsAwayLeagueRecord`
        """
        model = ScheduleGameTeamsAwayLeagueRecord()
        if include_optional:
            return ScheduleGameTeamsAwayLeagueRecord(
                wins = 23,
                losses = 27,
                ot = 4,
                type = 'league'
            )
        else:
            return ScheduleGameTeamsAwayLeagueRecord(
        )
        """

    def testScheduleGameTeamsAwayLeagueRecord(self):
        """Test ScheduleGameTeamsAwayLeagueRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
