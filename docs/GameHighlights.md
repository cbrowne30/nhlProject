# GameHighlights


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scoreboard** | [**GameHighlightType**](GameHighlightType.md) |  | [optional] 
**game_center** | [**GameHighlightType**](GameHighlightType.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_highlights import GameHighlights

# TODO update the JSON string below
json = "{}"
# create an instance of GameHighlights from a JSON string
game_highlights_instance = GameHighlights.from_json(json)
# print the JSON string representation of the object
print GameHighlights.to_json()

# convert the object into a dict
game_highlights_dict = game_highlights_instance.to_dict()
# create an instance of GameHighlights from a dict
game_highlights_form_dict = game_highlights.from_dict(game_highlights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


