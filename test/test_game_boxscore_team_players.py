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

from openapi_client.models.game_boxscore_team_players import GameBoxscoreTeamPlayers

class TestGameBoxscoreTeamPlayers(unittest.TestCase):
    """GameBoxscoreTeamPlayers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameBoxscoreTeamPlayers:
        """Test GameBoxscoreTeamPlayers
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameBoxscoreTeamPlayers`
        """
        model = GameBoxscoreTeamPlayers()
        if include_optional:
            return GameBoxscoreTeamPlayers(
                person = openapi_client.models.game_boxscore_team_players_person.GameBoxscoreTeam_players_person(
                    id = 8471709, 
                    full_name = 'Marc-Edouard Vlasic', 
                    link = '/api/v1/people/8471709', 
                    shoots_catches = 'L', 
                    roster_status = 'Y', ),
                jersey_number = '44',
                position = openapi_client.models.game_boxscore_team_players_position.GameBoxscoreTeam_players_position(
                    code = 'D', 
                    name = 'Defenseman', 
                    type = 'Defenseman', 
                    abbreviation = 'D', ),
                stats = openapi_client.models.game_boxscore_team_players_stats.GameBoxscoreTeam_players_stats(
                    skater_stats = openapi_client.models.game_boxscore_team_players_stats_skater_stats.GameBoxscoreTeam_players_stats_skaterStats(
                        time_on_ice = '23:04', 
                        assists = 0, 
                        goals = 0, 
                        shots = 2, 
                        hits = 0, 
                        power_play_goals = 0, 
                        power_play_assists = 0, 
                        penalty_minutes = 0, 
                        face_off_wins = 0, 
                        faceoff_taken = 0, 
                        takeaways = 0, 
                        giveaways = 1, 
                        short_handed_goals = 0, 
                        short_handed_assists = 0, 
                        blocked = 0, 
                        plus_minus = 1, 
                        even_time_on_ice = '18:12', 
                        power_play_time_on_ice = '1:07', 
                        short_handed_time_on_ice = '3:45', ), )
            )
        else:
            return GameBoxscoreTeamPlayers(
        )
        """

    def testGameBoxscoreTeamPlayers(self):
        """Test GameBoxscoreTeamPlayers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()