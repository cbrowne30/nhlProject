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

from openapi_client.models.game_linescore_power_play_info import GameLinescorePowerPlayInfo

class TestGameLinescorePowerPlayInfo(unittest.TestCase):
    """GameLinescorePowerPlayInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameLinescorePowerPlayInfo:
        """Test GameLinescorePowerPlayInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameLinescorePowerPlayInfo`
        """
        model = GameLinescorePowerPlayInfo()
        if include_optional:
            return GameLinescorePowerPlayInfo(
                situation_time_remaining = 0,
                situation_time_elapsed = 72,
                in_situation = True
            )
        else:
            return GameLinescorePowerPlayInfo(
        )
        """

    def testGameLinescorePowerPlayInfo(self):
        """Test GameLinescorePowerPlayInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
