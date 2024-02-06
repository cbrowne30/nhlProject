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

from openapi_client.models.venue import Venue

class TestVenue(unittest.TestCase):
    """Venue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Venue:
        """Test Venue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Venue`
        """
        model = Venue()
        if include_optional:
            return Venue(
                name = 'SAP Center at San Jose',
                link = '/api/v1/venues/null',
                city = 'San Jose',
                time_zone = openapi_client.models.venue_time_zone.Venue_timeZone(
                    id = 'America/Los_Angeles', 
                    offset = -8, 
                    tz = 'PST', )
            )
        else:
            return Venue(
        )
        """

    def testVenue(self):
        """Test Venue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
