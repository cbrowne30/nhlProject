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
from openapi_client.models.draft_drafts_inner_rounds_inner import DraftDraftsInnerRoundsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DraftDraftsInner(BaseModel):
    """
    DraftDraftsInner
    """ # noqa: E501
    draft_year: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="draftYear")
    rounds: Optional[List[DraftDraftsInnerRoundsInner]] = None
    __properties: ClassVar[List[str]] = ["draftYear", "rounds"]

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
        """Create an instance of DraftDraftsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rounds (list)
        _items = []
        if self.rounds:
            for _item in self.rounds:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rounds'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DraftDraftsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "draftYear": obj.get("draftYear"),
            "rounds": [DraftDraftsInnerRoundsInner.from_dict(_item) for _item in obj.get("rounds")] if obj.get("rounds") is not None else None
        })
        return _obj

