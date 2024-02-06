# GameMediaNHLTV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**items** | [**List[GameMediaNHLTVItemsInner]**](GameMediaNHLTVItemsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_media_nhltv import GameMediaNHLTV

# TODO update the JSON string below
json = "{}"
# create an instance of GameMediaNHLTV from a JSON string
game_media_nhltv_instance = GameMediaNHLTV.from_json(json)
# print the JSON string representation of the object
print GameMediaNHLTV.to_json()

# convert the object into a dict
game_media_nhltv_dict = game_media_nhltv_instance.to_dict()
# create an instance of GameMediaNHLTV from a dict
game_media_nhltv_form_dict = game_media_nhltv.from_dict(game_media_nhltv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


