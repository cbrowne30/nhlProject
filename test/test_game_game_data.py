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

from openapi_client.models.game_game_data import GameGameData

class TestGameGameData(unittest.TestCase):
    """GameGameData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameGameData:
        """Test GameGameData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameGameData`
        """
        model = GameGameData()
        if include_optional:
            return GameGameData(
                game = openapi_client.models.game_game_data_game.Game_gameData_game(
                    pk = 2017020851, 
                    season = '20172018', 
                    type = 'R', ),
                datetime = openapi_client.models.game_game_data_datetime.Game_gameData_datetime(
                    date_time = '2018-02-11T03:00Z', 
                    end_date_time = '2018-02-11T05:30:42Z', ),
                status = openapi_client.models.game_game_data_status.Game_gameData_status(
                    abstract_game_state = 'Final', 
                    coded_game_state = '7', 
                    detailed_state = 'Final', 
                    status_code = '7', 
                    start_time_tbd = True, ),
                teams = openapi_client.models.game_game_data_teams.Game_gameData_teams(
                    away = openapi_client.models.team.Team(
                        id = 28, 
                        name = 'San Jose Sharks', 
                        link = '/api/v1/teams/28', 
                        venue = openapi_client.models.venue.Venue(
                            name = 'SAP Center at San Jose', 
                            link = '/api/v1/venues/null', 
                            city = 'San Jose', 
                            time_zone = openapi_client.models.venue_time_zone.Venue_timeZone(
                                id = 'America/Los_Angeles', 
                                offset = -8, 
                                tz = 'PST', ), ), 
                        abbreviation = 'SJS', 
                        tri_code = 'SJS', 
                        team_name = 'Sharks', 
                        location_name = 'San Jose', 
                        first_year_of_play = 1990, 
                        division = openapi_client.models.standings_records_inner_division.Standings_records_inner_division(
                            id = 15, 
                            name = 'Pacific', 
                            link = '/api/v1/divisions/15', ), 
                        conference = openapi_client.models.division_conference.Division_conference(
                            id = 5, 
                            name = 'Western', 
                            link = '/api/v1/conferences/5', ), 
                        franchise = openapi_client.models.franchise.Franchise(
                            id = 29, 
                            name = 'Sharks', 
                            link = '/api/v1/franchises/29', ), 
                        roster = openapi_client.models.team_roster.Team_roster(), 
                        next_game_schedule = openapi_client.models.team_next_game_schedule.Team_nextGameSchedule(
                            total_items = 1, 
                            total_events = 0, 
                            total_games = 1, 
                            total_matches = 0, 
                            dates = [
                                openapi_client.models.team_next_game_schedule_dates_inner.Team_nextGameSchedule_dates_inner(
                                    date = 'Fri Feb 09 19:00:00 EST 2018', 
                                    total_items = 1, 
                                    total_events = 0, 
                                    total_games = 1, 
                                    total_matches = 0, 
                                    games = [
                                        openapi_client.models.team_next_game_schedule_dates_inner_games_inner.Team_nextGameSchedule_dates_inner_games_inner(
                                            game_pk = 2017020851, 
                                            link = '/api/v1/game/2017020851/feed/live', 
                                            game_type = 'R', 
                                            season = '20172018', 
                                            game_date = '2018-02-11T03:00Z', 
                                            status = openapi_client.models.team_next_game_schedule_dates_inner_games_inner_status.Team_nextGameSchedule_dates_inner_games_inner_status(
                                                abstract_game_state = 'Live', 
                                                coded_game_state = '3', 
                                                detailed_state = 'In Progress', 
                                                status_code = '2', 
                                                start_time_tbd = True, ), 
                                            content = openapi_client.models.schedule_game_content.ScheduleGame_content(
                                                link = '/api/v1/game/2017020851/content', ), )
                                        ], 
                                    events = [
                                        None
                                        ], 
                                    matches = [
                                        None
                                        ], )
                                ], ), 
                        short_name = 'San Jose', 
                        official_site_url = 'http://www.sjsharks.com', 
                        franchise_id = 29, 
                        active = True, ), 
                    home = openapi_client.models.team.Team(
                        id = 28, 
                        name = 'San Jose Sharks', 
                        link = '/api/v1/teams/28', 
                        abbreviation = 'SJS', 
                        tri_code = 'SJS', 
                        team_name = 'Sharks', 
                        location_name = 'San Jose', 
                        first_year_of_play = 1990, 
                        short_name = 'San Jose', 
                        official_site_url = 'http://www.sjsharks.com', 
                        franchise_id = 29, 
                        active = True, ), ),
                players = openapi_client.models.player.Player(
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
                        abbreviation = 'C', ), ),
                venue = openapi_client.models.game_game_data_venue.Game_gameData_venue(
                    name = 'SAP Center at San Jose', 
                    link = '/api/v1/venues/null', )
            )
        else:
            return GameGameData(
        )
        """

    def testGameGameData(self):
        """Test GameGameData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
