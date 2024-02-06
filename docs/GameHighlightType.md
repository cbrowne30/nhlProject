# GameHighlightType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**topic_list** | **str** |  | [optional] 
**items** | [**List[GameHighlight]**](GameHighlight.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_highlight_type import GameHighlightType

# TODO update the JSON string below
json = "{}"
# create an instance of GameHighlightType from a JSON string
game_highlight_type_instance = GameHighlightType.from_json(json)
# print the JSON string representation of the object
print GameHighlightType.to_json()

# convert the object into a dict
game_highlight_type_dict = game_highlight_type_instance.to_dict()
# create an instance of GameHighlightType from a dict
game_highlight_type_form_dict = game_highlight_type.from_dict(game_highlight_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


