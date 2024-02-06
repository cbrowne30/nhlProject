# GameHighlight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**blurb** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duration** | **str** |  | [optional] 
**auth_flow** | **bool** |  | [optional] 
**media_playback_id** | **str** |  | [optional] 
**media_state** | **str** |  | [optional] 
**keywords** | [**List[GameEditorialKeyword]**](GameEditorialKeyword.md) |  | [optional] 
**image** | [**Photo**](Photo.md) |  | [optional] 
**playbacks** | [**List[GameHighlightPlaybacksInner]**](GameHighlightPlaybacksInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_highlight import GameHighlight

# TODO update the JSON string below
json = "{}"
# create an instance of GameHighlight from a JSON string
game_highlight_instance = GameHighlight.from_json(json)
# print the JSON string representation of the object
print GameHighlight.to_json()

# convert the object into a dict
game_highlight_dict = game_highlight_instance.to_dict()
# create an instance of GameHighlight from a dict
game_highlight_form_dict = game_highlight.from_dict(game_highlight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


