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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from openapi_client.models.game_highlights import GameHighlights
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GameContentHighlights(BaseModel):
    """
    GameContentHighlights
    """ # noqa: E501
    scoreboard: Optional[GameHighlights] = None
    game_center: Optional[GameHighlights] = Field(default=None, alias="gameCenter")
    __properties: ClassVar[List[str]] = ["scoreboard", "gameCenter"]

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
        """Create an instance of GameContentHighlights from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scoreboard
        if self.scoreboard:
            _dict['scoreboard'] = self.scoreboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of game_center
        if self.game_center:
            _dict['gameCenter'] = self.game_center.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GameContentHighlights from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scoreboard": GameHighlights.from_dict(obj.get("scoreboard")) if obj.get("scoreboard") is not None else None,
            "gameCenter": GameHighlights.from_dict(obj.get("gameCenter")) if obj.get("gameCenter") is not None else None
        })
        return _obj


