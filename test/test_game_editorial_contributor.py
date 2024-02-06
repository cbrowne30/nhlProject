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

from openapi_client.models.game_editorial_contributor import GameEditorialContributor

class TestGameEditorialContributor(unittest.TestCase):
    """GameEditorialContributor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameEditorialContributor:
        """Test GameEditorialContributor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameEditorialContributor`
        """
        model = GameEditorialContributor()
        if include_optional:
            return GameEditorialContributor(
                contributors = [
                    openapi_client.models.game_editorial_contributor_contributors_inner.GameEditorial_contributor_contributors_inner(
                        name = 'Eric Gilmore', 
                        twitter = '', )
                    ],
                source = 'NHL.com Correspondent'
            )
        else:
            return GameEditorialContributor(
        )
        """

    def testGameEditorialContributor(self):
        """Test GameEditorialContributor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
