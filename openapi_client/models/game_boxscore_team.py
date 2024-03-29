# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from pydantic import Field
from openapi_client.models.game_boxscore_team_coaches_inner import GameBoxscoreTeamCoachesInner
from openapi_client.models.game_boxscore_team_on_ice_plus_inner import GameBoxscoreTeamOnIcePlusInner
from openapi_client.models.game_boxscore_team_players import GameBoxscoreTeamPlayers
from openapi_client.models.game_boxscore_team_team import GameBoxscoreTeamTeam
from openapi_client.models.game_boxscore_team_team_stats import GameBoxscoreTeamTeamStats
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GameBoxscoreTeam(BaseModel):
    """
    GameBoxscoreTeam
    """ # noqa: E501
    team: Optional[GameBoxscoreTeamTeam] = None
    team_stats: Optional[GameBoxscoreTeamTeamStats] = Field(default=None, alias="teamStats")
    players: Optional[GameBoxscoreTeamPlayers] = None
    goalies: Optional[List[Union[StrictFloat, StrictInt]]] = None
    skaters: Optional[List[Union[StrictFloat, StrictInt]]] = None
    on_ice: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="onIce")
    on_ice_plus: Optional[List[GameBoxscoreTeamOnIcePlusInner]] = Field(default=None, alias="onIcePlus")
    scratches: Optional[List[Union[StrictFloat, StrictInt]]] = None
    penalty_box: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="penaltyBox")
    coaches: Optional[List[GameBoxscoreTeamCoachesInner]] = None
    __properties: ClassVar[List[str]] = ["team", "teamStats", "players", "goalies", "skaters", "onIce", "onIcePlus", "scratches", "penaltyBox", "coaches"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GameBoxscoreTeam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team_stats
        if self.team_stats:
            _dict['teamStats'] = self.team_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of players
        if self.players:
            _dict['players'] = self.players.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in on_ice_plus (list)
        _items = []
        if self.on_ice_plus:
            for _item in self.on_ice_plus:
                if _item:
                    _items.append(_item.to_dict())
            _dict['onIcePlus'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in coaches (list)
        _items = []
        if self.coaches:
            for _item in self.coaches:
                if _item:
                    _items.append(_item.to_dict())
            _dict['coaches'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GameBoxscoreTeam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "team": GameBoxscoreTeamTeam.from_dict(obj.get("team")) if obj.get("team") is not None else None,
            "teamStats": GameBoxscoreTeamTeamStats.from_dict(obj.get("teamStats")) if obj.get("teamStats") is not None else None,
            "players": GameBoxscoreTeamPlayers.from_dict(obj.get("players")) if obj.get("players") is not None else None,
            "goalies": obj.get("goalies"),
            "skaters": obj.get("skaters"),
            "onIce": obj.get("onIce"),
            "onIcePlus": [GameBoxscoreTeamOnIcePlusInner.from_dict(_item) for _item in obj.get("onIcePlus")] if obj.get("onIcePlus") is not None else None,
            "scratches": obj.get("scratches"),
            "penaltyBox": obj.get("penaltyBox"),
            "coaches": [GameBoxscoreTeamCoachesInner.from_dict(_item) for _item in obj.get("coaches")] if obj.get("coaches") is not None else None
        })
        return _obj


