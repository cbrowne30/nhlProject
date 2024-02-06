# GameMediaAudio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**items** | [**List[GameMediaAudioItemsInner]**](GameMediaAudioItemsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_media_audio import GameMediaAudio

# TODO update the JSON string below
json = "{}"
# create an instance of GameMediaAudio from a JSON string
game_media_audio_instance = GameMediaAudio.from_json(json)
# print the JSON string representation of the object
print GameMediaAudio.to_json()

# convert the object into a dict
game_media_audio_dict = game_media_audio_instance.to_dict()
# create an instance of GameMediaAudio from a dict
game_media_audio_form_dict = game_media_audio.from_dict(game_media_audio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


