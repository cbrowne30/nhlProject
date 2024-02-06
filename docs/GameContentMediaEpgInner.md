# GameContentMediaEpgInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**items** | [**List[GameHighlight]**](GameHighlight.md) |  | [optional] 
**topic_list** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_content_media_epg_inner import GameContentMediaEpgInner

# TODO update the JSON string below
json = "{}"
# create an instance of GameContentMediaEpgInner from a JSON string
game_content_media_epg_inner_instance = GameContentMediaEpgInner.from_json(json)
# print the JSON string representation of the object
print GameContentMediaEpgInner.to_json()

# convert the object into a dict
game_content_media_epg_inner_dict = game_content_media_epg_inner_instance.to_dict()
# create an instance of GameContentMediaEpgInner from a dict
game_content_media_epg_inner_form_dict = game_content_media_epg_inner.from_dict(game_content_media_epg_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


