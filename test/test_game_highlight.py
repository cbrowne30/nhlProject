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

from openapi_client.models.game_highlight import GameHighlight

class TestGameHighlight(unittest.TestCase):
    """GameHighlight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameHighlight:
        """Test GameHighlight
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameHighlight`
        """
        model = GameHighlight()
        if include_optional:
            return GameHighlight(
                type = 'video',
                id = '57602103',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                title = 'Goodrow buries Hansen's pass',
                blurb = 'EDM@SJS: Goodrow snaps Hansen's pass by Montoya',
                description = 'Barclay Goodrow takes a drop pass from Jannik Hansen and whips a quick wrist shot past Al Montoya to give the Sharks a 3-0 lead in the 2nd',
                duration = '00:51',
                auth_flow = True,
                media_playback_id = '57602103',
                media_state = 'MEDIA_ARCHIVE',
                keywords = [
                    openapi_client.models.game_editorial_keyword.GameEditorialKeyword(
                        type = 'bodyParagraphCount', 
                        value = 'en', 
                        display_name = 'English', )
                    ],
                image = openapi_client.models.photo.Photo(
                    title = '', 
                    alt_text = '', 
                    cuts = openapi_client.models.photo_cuts.Photo_cuts(
                        aspect_ratio = '16:9', 
                        width = 2568, 
                        height = 1444, 
                        src = 'https://nhl.bamcontent.com/images/photos/295824704/2568x1444/cut.jpg', 
                        at2x = 'https://nhl.bamcontent.com/images/photos/295824704/2568x1444/cut.jpg', 
                        at3x = 'https://nhl.bamcontent.com/images/photos/295824704/2568x1444/cut.jpg', ), ),
                playbacks = [
                    openapi_client.models.game_highlight_playbacks_inner.GameHighlight_playbacks_inner(
                        name = 'FLASH_192K_320X180', 
                        width = '960', 
                        height = '540', 
                        url = 'http://md-akc.med.nhl.com/mp4/nhl/2018/02/11/ddec1fcc-3772-4769-a547-314de76c6c11/1518322152840/asset_1800k.mp4', )
                    ]
            )
        else:
            return GameHighlight(
        )
        """

    def testGameHighlight(self):
        """Test GameHighlight"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
