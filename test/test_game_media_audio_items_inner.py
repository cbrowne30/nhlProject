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

from openapi_client.models.game_media_audio_items_inner import GameMediaAudioItemsInner

class TestGameMediaAudioItemsInner(unittest.TestCase):
    """GameMediaAudioItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameMediaAudioItemsInner:
        """Test GameMediaAudioItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameMediaAudioItemsInner`
        """
        model = GameMediaAudioItemsInner()
        if include_optional:
            return GameMediaAudioItemsInner(
                media_state = 'MEDIA_DONE',
                media_playback_id = '57463903',
                media_feed_type = 'HOME',
                call_letters = 'KFOX',
                event_id = '221-1007449',
                language = 'eng',
                free_game = True,
                feed_name = '',
                game_plus = True
            )
        else:
            return GameMediaAudioItemsInner(
        )
        """

    def testGameMediaAudioItemsInner(self):
        """Test GameMediaAudioItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()