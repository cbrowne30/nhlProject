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

from openapi_client.models.game_content import GameContent

class TestGameContent(unittest.TestCase):
    """GameContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameContent:
        """Test GameContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameContent`
        """
        model = GameContent()
        if include_optional:
            return GameContent(
                copyright = '',
                link = '/api/v1/game/2017020851/content',
                editorial = openapi_client.models.game_content_editorial.GameContent_editorial(
                    preview = openapi_client.models.game_editorials.GameEditorials(
                        title = 'Preview', 
                        topic_list = '', 
                        items = [
                            openapi_client.models.game_editorial.GameEditorial(
                                type = 'article', 
                                state = 'A', 
                                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                id = '295823824', 
                                headline = 'Oilers at Sharks preview', 
                                subhead = 'Backups Montoya, Dell to start for Edmonton, San Jose', 
                                seo_title = 'Edmonton Oilers San Jose Sharks game preview', 
                                seo_description = 'Backup goaltender Aaron Dell will make his 19th start of the season when the San Jose Sharks play the Edmonton Oilers at SAP Center on Saturday in the first of back-to-back games.', 
                                seo_keywords = 'Game preview, Edmonton Oilers, San Jose Sharks, Aaron Dell, Al Montoya, Feb 10', 
                                slug = 'edmonton-oilers-san-jose-sharks-game-preview', 
                                commenting = True, 
                                tagline = '', 
                                token_data = openapi_client.models.game_editorial_token_data.GameEditorial_tokenData(
                                    token_guid = 'token-EBDA2F0039BF4445D2C91', 
                                    type = 'hyperLink', 
                                    id = '8471709', 
                                    team_id = '28', 
                                    name = 'Marc-Edouard Vlasic', 
                                    seo_name = 'marc-edouard-vlasic', 
                                    href = 'https://www.nhl.com/player/keegan-lowe-8476397?season=20172018', 
                                    href_mobile = 'https://www.nhl.com/player/keegan-lowe-8476397?season=20172018', ), 
                                contributor = openapi_client.models.game_editorial_contributor.GameEditorial_contributor(
                                    contributors = [
                                        openapi_client.models.game_editorial_contributor_contributors_inner.GameEditorial_contributor_contributors_inner(
                                            name = 'Eric Gilmore', 
                                            twitter = '', )
                                        ], 
                                    source = 'NHL.com Correspondent', ), 
                                keywords_display = [
                                    openapi_client.models.game_editorial_keyword.GameEditorialKeyword(
                                        type = 'bodyParagraphCount', 
                                        value = 'en', 
                                        display_name = 'English', )
                                    ], 
                                keywords_all = [
                                    openapi_client.models.game_editorial_keyword.GameEditorialKeyword(
                                        type = 'bodyParagraphCount', 
                                        value = 'en', 
                                        display_name = 'English', )
                                    ], 
                                approval = '', 
                                url = '/news/edmonton-oilers-san-jose-sharks-game-preview/c-295823824?game_pk=2017020851', 
                                data_uri = '/nhl/id/v1/295823824/details/web-v1.json', 
                                primary_keyword = , 
                                media = openapi_client.models.game_editorial_media.GameEditorial_media(
                                    type = 'photo', 
                                    image = openapi_client.models.photo.Photo(
                                        title = '', 
                                        alt_text = '', 
                                        cuts = openapi_client.models.photo_cuts.Photo_cuts(
                                            aspect_ratio = '16:9', 
                                            width = 2568, 
                                            height = 1444, 
                                            src = 'https://nhl.bamcontent.com/images/photos/295824704/2568x1444/cut.jpg', 
                                            at2x = 'https://nhl.bamcontent.com/images/photos/295824704/2568x1444/cut.jpg', 
                                            at3x = 'https://nhl.bamcontent.com/images/photos/295824704/2568x1444/cut.jpg', ), ), ), )
                            ], ), 
                    articles = openapi_client.models.game_editorials.GameEditorials(
                        title = 'Preview', 
                        topic_list = '', ), 
                    recap = , ),
                media = openapi_client.models.game_content_media.GameContent_media(
                    epg = [
                        openapi_client.models.game_content_media_epg_inner.GameContent_media_epg_inner()
                        ], 
                    milestones = openapi_client.models.game_content_media_milestones.GameContent_media_milestones(
                        title = 'Milestones', 
                        stream_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        items = [
                            openapi_client.models.game_content_media_milestones_items_inner.GameContent_media_milestones_items_inner(
                                title = 'Broadcast Start', 
                                description = 'Broadcast Start', 
                                type = 'BROADCAST_START', 
                                time_absolute = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                time_offset = '4', 
                                period = '1', 
                                stats_event_id = '10', 
                                team_id = '28', 
                                player_id = '8477046', 
                                period_time = '01:15', 
                                ordinal_num = '1st', 
                                highlight = openapi_client.models.game_highlight.GameHighlight(
                                    type = 'video', 
                                    id = '57602103', 
                                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
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
                                        ], ), )
                            ], ), ),
                highlights = openapi_client.models.game_content_highlights.GameContent_highlights(
                    scoreboard = openapi_client.models.game_highlights.GameHighlights(
                        game_center = openapi_client.models.game_highlight_type.GameHighlightType(
                            title = 'Highlights', 
                            topic_list = '293642378', 
                            items = [
                                openapi_client.models.game_highlight.GameHighlight(
                                    type = 'video', 
                                    id = '57602103', 
                                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
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
                                        ], )
                                ], ), ), 
                    game_center = openapi_client.models.game_highlights.GameHighlights(), )
            )
        else:
            return GameContent(
        )
        """

    def testGameContent(self):
        """Test GameContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
