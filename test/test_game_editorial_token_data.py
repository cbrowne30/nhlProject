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

from openapi_client.models.game_editorial_token_data import GameEditorialTokenData

class TestGameEditorialTokenData(unittest.TestCase):
    """GameEditorialTokenData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameEditorialTokenData:
        """Test GameEditorialTokenData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameEditorialTokenData`
        """
        model = GameEditorialTokenData()
        if include_optional:
            return GameEditorialTokenData(
                token_guid = 'token-EBDA2F0039BF4445D2C91',
                type = 'hyperLink',
                id = '8471709',
                team_id = '28',
                name = 'Marc-Edouard Vlasic',
                seo_name = 'marc-edouard-vlasic',
                href = 'https://www.nhl.com/player/keegan-lowe-8476397?season=20172018',
                href_mobile = 'https://www.nhl.com/player/keegan-lowe-8476397?season=20172018'
            )
        else:
            return GameEditorialTokenData(
        )
        """

    def testGameEditorialTokenData(self):
        """Test GameEditorialTokenData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()