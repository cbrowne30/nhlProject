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

from openapi_client.models.game_content_editorial import GameContentEditorial

class TestGameContentEditorial(unittest.TestCase):
    """GameContentEditorial unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameContentEditorial:
        """Test GameContentEditorial
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameContentEditorial`
        """
        model = GameContentEditorial()
        if include_optional:
            return GameContentEditorial(
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
                                        at3x = 'https://nhl.bamcontent.com/images/photos/295824704/2568x1444/cut.jpg', ), ), ), 
                            preview = '<p><b>OILERS (23-26-4) at SHARKS (28-18-8)</b></p><p><b>10 p.m. ET; NBCSCA, CITY, SN360, SN, NHL.TV</b></p><p>&nbsp;</p><h5><b>The Game</b></h5><p>Backup goaltender <span class="token token-playerCard" id="token-B36CCB71E81996298E792">Aaron Dell</span> will make his 19th start of the season when the San Jose Sharks play the Edmonton Oilers at SAP Center on Saturday in the first of back-to-back games.</p>', )
                        ], ),
                recap = openapi_client.models.game_editorials.GameEditorials(
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
                                        at3x = 'https://nhl.bamcontent.com/images/photos/295824704/2568x1444/cut.jpg', ), ), ), 
                            preview = '<p><b>OILERS (23-26-4) at SHARKS (28-18-8)</b></p><p><b>10 p.m. ET; NBCSCA, CITY, SN360, SN, NHL.TV</b></p><p>&nbsp;</p><h5><b>The Game</b></h5><p>Backup goaltender <span class="token token-playerCard" id="token-B36CCB71E81996298E792">Aaron Dell</span> will make his 19th start of the season when the San Jose Sharks play the Edmonton Oilers at SAP Center on Saturday in the first of back-to-back games.</p>', )
                        ], )
            )
        else:
            return GameContentEditorial(
        )
        """

    def testGameContentEditorial(self):
        """Test GameContentEditorial"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()