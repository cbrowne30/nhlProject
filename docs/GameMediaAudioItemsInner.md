# GameMediaAudioItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_state** | **str** |  | [optional] 
**media_playback_id** | **str** |  | [optional] 
**media_feed_type** | **str** |  | [optional] 
**call_letters** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**free_game** | **bool** |  | [optional] 
**feed_name** | **str** |  | [optional] 
**game_plus** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.game_media_audio_items_inner import GameMediaAudioItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GameMediaAudioItemsInner from a JSON string
game_media_audio_items_inner_instance = GameMediaAudioItemsInner.from_json(json)
# print the JSON string representation of the object
print GameMediaAudioItemsInner.to_json()

# convert the object into a dict
game_media_audio_items_inner_dict = game_media_audio_items_inner_instance.to_dict()
# create an instance of GameMediaAudioItemsInner from a dict
game_media_audio_items_inner_form_dict = game_media_audio_items_inner.from_dict(game_media_audio_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


