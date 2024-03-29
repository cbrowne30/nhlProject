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

from openapi_client.models.schedule_game_tickets_inner import ScheduleGameTicketsInner

class TestScheduleGameTicketsInner(unittest.TestCase):
    """ScheduleGameTicketsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleGameTicketsInner:
        """Test ScheduleGameTicketsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleGameTicketsInner`
        """
        model = ScheduleGameTicketsInner()
        if include_optional:
            return ScheduleGameTicketsInner(
                ticket_type = 'buysell',
                ticket_link = 'http://www.ticketmaster.com/event/090052DD92E620B4?BRAND=ducks&extcmp=tm208344&utm_source=NHL.com&utm_medium=client&utm_campaign=NHL_LEAGUE_ANA&utm_content=SCHEDULE_PAGE&camefrom=CFC_DUCKS_1718_Web_DucksSchedule'
            )
        else:
            return ScheduleGameTicketsInner(
        )
        """

    def testScheduleGameTicketsInner(self):
        """Test ScheduleGameTicketsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
