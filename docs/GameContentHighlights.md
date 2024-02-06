# GameContentHighlights


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scoreboard** | [**GameHighlights**](GameHighlights.md) |  | [optional] 
**game_center** | [**GameHighlights**](GameHighlights.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_content_highlights import GameContentHighlights

# TODO update the JSON string below
json = "{}"
# create an instance of GameContentHighlights from a JSON string
game_content_highlights_instance = GameContentHighlights.from_json(json)
# print the JSON string representation of the object
print GameContentHighlights.to_json()

# convert the object into a dict
game_content_highlights_dict = game_content_highlights_instance.to_dict()
# create an instance of GameContentHighlights from a dict
game_content_highlights_form_dict = game_content_highlights.from_dict(game_content_highlights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


