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

class TeamStatsStatsInnerSplitsInnerStat(BaseModel):
    """
    TeamStatsStatsInnerSplitsInnerStat
    """ # noqa: E501
    games_played: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gamesPlayed")
    wins: Optional[Union[StrictFloat, StrictInt]] = None
    losses: Optional[Union[StrictFloat, StrictInt]] = None
    ot: Optional[Union[StrictFloat, StrictInt]] = None
    pts: Optional[Union[StrictFloat, StrictInt]] = None
    pt_pctg: Optional[StrictStr] = Field(default=None, alias="ptPctg")
    goals_per_game: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="goalsPerGame")
    goals_against_per_game: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="goalsAgainstPerGame")
    ev_gga_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="evGGARatio")
    power_play_percentage: Optional[StrictStr] = Field(default=None, alias="powerPlayPercentage")
    power_play_goals: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="powerPlayGoals")
    power_play_goals_against: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="powerPlayGoalsAgainst")
    power_play_opportunities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="powerPlayOpportunities")
    penalty_kill_percentage: Optional[StrictStr] = Field(default=None, alias="penaltyKillPercentage")
    shots_per_game: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shotsPerGame")
    shots_allowed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shotsAllowed")
    win_score_first: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="winScoreFirst")
    win_opp_score_first: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="winOppScoreFirst")
    win_lead_first_per: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="winLeadFirstPer")
    win_lead_second_per: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="winLeadSecondPer")
    win_outshoot_opp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="winOutshootOpp")
    win_outshot_by_opp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="winOutshotByOpp")
    face_offs_taken: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="faceOffsTaken")
    face_offs_won: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="faceOffsWon")
    face_offs_lost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="faceOffsLost")
    face_off_win_percentage: Optional[StrictStr] = Field(default=None, alias="faceOffWinPercentage")
    shooting_pctg: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shootingPctg")
    save_pctg: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="savePctg")
    __properties: ClassVar[List[str]] = ["gamesPlayed", "wins", "losses", "ot", "pts", "ptPctg", "goalsPerGame", "goalsAgainstPerGame", "evGGARatio", "powerPlayPercentage", "powerPlayGoals", "powerPlayGoalsAgainst", "powerPlayOpportunities", "penaltyKillPercentage", "shotsPerGame", "shotsAllowed", "winScoreFirst", "winOppScoreFirst", "winLeadFirstPer", "winLeadSecondPer", "winOutshootOpp", "winOutshotByOpp", "faceOffsTaken", "faceOffsWon", "faceOffsLost", "faceOffWinPercentage", "shootingPctg", "savePctg"]

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
        """Create an instance of TeamStatsStatsInnerSplitsInnerStat from a JSON string"""
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
        """Create an instance of TeamStatsStatsInnerSplitsInnerStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gamesPlayed": obj.get("gamesPlayed"),
            "wins": obj.get("wins"),
            "losses": obj.get("losses"),
            "ot": obj.get("ot"),
            "pts": obj.get("pts"),
            "ptPctg": obj.get("ptPctg"),
            "goalsPerGame": obj.get("goalsPerGame"),
            "goalsAgainstPerGame": obj.get("goalsAgainstPerGame"),
            "evGGARatio": obj.get("evGGARatio"),
            "powerPlayPercentage": obj.get("powerPlayPercentage"),
            "powerPlayGoals": obj.get("powerPlayGoals"),
            "powerPlayGoalsAgainst": obj.get("powerPlayGoalsAgainst"),
            "powerPlayOpportunities": obj.get("powerPlayOpportunities"),
            "penaltyKillPercentage": obj.get("penaltyKillPercentage"),
            "shotsPerGame": obj.get("shotsPerGame"),
            "shotsAllowed": obj.get("shotsAllowed"),
            "winScoreFirst": obj.get("winScoreFirst"),
            "winOppScoreFirst": obj.get("winOppScoreFirst"),
            "winLeadFirstPer": obj.get("winLeadFirstPer"),
            "winLeadSecondPer": obj.get("winLeadSecondPer"),
            "winOutshootOpp": obj.get("winOutshootOpp"),
            "winOutshotByOpp": obj.get("winOutshotByOpp"),
            "faceOffsTaken": obj.get("faceOffsTaken"),
            "faceOffsWon": obj.get("faceOffsWon"),
            "faceOffsLost": obj.get("faceOffsLost"),
            "faceOffWinPercentage": obj.get("faceOffWinPercentage"),
            "shootingPctg": obj.get("shootingPctg"),
            "savePctg": obj.get("savePctg")
        })
        return _obj


