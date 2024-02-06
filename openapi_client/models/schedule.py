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
from openapi_client.models.schedule_day import ScheduleDay
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Schedule(BaseModel):
    """
    Schedule
    """ # noqa: E501
    copyright: Optional[StrictStr] = None
    total_items: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalItems")
    total_events: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalEvents")
    total_games: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalGames")
    total_matches: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalMatches")
    wait: Optional[Union[StrictFloat, StrictInt]] = None
    dates: Optional[List[ScheduleDay]] = None
    __properties: ClassVar[List[str]] = ["copyright", "totalItems", "totalEvents", "totalGames", "totalMatches", "wait", "dates"]

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
        """Create an instance of Schedule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dates (list)
        _items = []
        if self.dates:
            for _item in self.dates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Schedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "copyright": obj.get("copyright"),
            "totalItems": obj.get("totalItems"),
            "totalEvents": obj.get("totalEvents"),
            "totalGames": obj.get("totalGames"),
            "totalMatches": obj.get("totalMatches"),
            "wait": obj.get("wait"),
            "dates": [ScheduleDay.from_dict(_item) for _item in obj.get("dates")] if obj.get("dates") is not None else None
        })
        return _obj


