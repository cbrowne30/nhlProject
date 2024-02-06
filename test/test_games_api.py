# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.games_api import GamesApi


class TestGamesApi(unittest.TestCase):
    """GamesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GamesApi()

    def tearDown(self) -> None:
        pass

    def test_get_game(self) -> None:
        """Test case for get_game

        Get all available data for an NHL game.
        """
        pass

    def test_get_game_boxscore(self) -> None:
        """Test case for get_game_boxscore

        Get the boxscore for an NHL game.
        """
        pass

    def test_get_game_content(self) -> None:
        """Test case for get_game_content

        Get editorials, video replays and photo highlights for an NHL game.
        """
        pass

    def test_get_game_diff(self) -> None:
        """Test case for get_game_diff

        Get all available data for an NHL game after a specific time.
        """
        pass


if __name__ == '__main__':
    unittest.main()