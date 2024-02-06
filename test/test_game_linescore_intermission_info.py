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

from openapi_client.models.game_linescore_intermission_info import GameLinescoreIntermissionInfo

class TestGameLinescoreIntermissionInfo(unittest.TestCase):
    """GameLinescoreIntermissionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameLinescoreIntermissionInfo:
        """Test GameLinescoreIntermissionInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameLinescoreIntermissionInfo`
        """
        model = GameLinescoreIntermissionInfo()
        if include_optional:
            return GameLinescoreIntermissionInfo(
                intermission_time_remaining = 0,
                intermission_time_elapsed = 0,
                in_intermission = True
            )
        else:
            return GameLinescoreIntermissionInfo(
        )
        """

    def testGameLinescoreIntermissionInfo(self):
        """Test GameLinescoreIntermissionInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()