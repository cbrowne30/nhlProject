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

from openapi_client.models.team_next_game_schedule_dates_inner_games_inner_teams_away_league_record import TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord

class TestTeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord(unittest.TestCase):
    """TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord:
        """Test TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord`
        """
        model = TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord()
        if include_optional:
            return TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord(
                wins = 23,
                losses = 26,
                ot = 4,
                type = 'league'
            )
        else:
            return TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord(
        )
        """

    def testTeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord(self):
        """Test TeamNextGameScheduleDatesInnerGamesInnerTeamsAwayLeagueRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
