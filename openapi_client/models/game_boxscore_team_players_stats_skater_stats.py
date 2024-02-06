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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GameBoxscoreTeamPlayersStatsSkaterStats(BaseModel):
    """
    GameBoxscoreTeamPlayersStatsSkaterStats
    """ # noqa: E501
    time_on_ice: Optional[StrictStr] = Field(default=None, alias="timeOnIce")
    assists: Optional[Union[StrictFloat, StrictInt]] = None
    goals: Optional[Union[StrictFloat, StrictInt]] = None
    shots: Optional[Union[StrictFloat, StrictInt]] = None
    hits: Optional[Union[StrictFloat, StrictInt]] = None
    power_play_goals: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="powerPlayGoals")
    power_play_assists: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="powerPlayAssists")
    penalty_minutes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="penaltyMinutes")
    face_off_wins: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="faceOffWins")
    faceoff_taken: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="faceoffTaken")
    takeaways: Optional[Union[StrictFloat, StrictInt]] = None
    giveaways: Optional[Union[StrictFloat, StrictInt]] = None
    short_handed_goals: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shortHandedGoals")
    short_handed_assists: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shortHandedAssists")
    blocked: Optional[Union[StrictFloat, StrictInt]] = None
    plus_minus: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="plusMinus")
    even_time_on_ice: Optional[StrictStr] = Field(default=None, alias="evenTimeOnIce")
    power_play_time_on_ice: Optional[StrictStr] = Field(default=None, alias="powerPlayTimeOnIce")
    short_handed_time_on_ice: Optional[StrictStr] = Field(default=None, alias="shortHandedTimeOnIce")
    __properties: ClassVar[List[str]] = ["timeOnIce", "assists", "goals", "shots", "hits", "powerPlayGoals", "powerPlayAssists", "penaltyMinutes", "faceOffWins", "faceoffTaken", "takeaways", "giveaways", "shortHandedGoals", "shortHandedAssists", "blocked", "plusMinus", "evenTimeOnIce", "powerPlayTimeOnIce", "shortHandedTimeOnIce"]

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
        """Create an instance of GameBoxscoreTeamPlayersStatsSkaterStats from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GameBoxscoreTeamPlayersStatsSkaterStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timeOnIce": obj.get("timeOnIce"),
            "assists": obj.get("assists"),
            "goals": obj.get("goals"),
            "shots": obj.get("shots"),
            "hits": obj.get("hits"),
            "powerPlayGoals": obj.get("powerPlayGoals"),
            "powerPlayAssists": obj.get("powerPlayAssists"),
            "penaltyMinutes": obj.get("penaltyMinutes"),
            "faceOffWins": obj.get("faceOffWins"),
            "faceoffTaken": obj.get("faceoffTaken"),
            "takeaways": obj.get("takeaways"),
            "giveaways": obj.get("giveaways"),
            "shortHandedGoals": obj.get("shortHandedGoals"),
            "shortHandedAssists": obj.get("shortHandedAssists"),
            "blocked": obj.get("blocked"),
            "plusMinus": obj.get("plusMinus"),
            "evenTimeOnIce": obj.get("evenTimeOnIce"),
            "powerPlayTimeOnIce": obj.get("powerPlayTimeOnIce"),
            "shortHandedTimeOnIce": obj.get("shortHandedTimeOnIce")
        })
        return _obj


