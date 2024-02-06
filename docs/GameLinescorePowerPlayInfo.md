# GameLinescorePowerPlayInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**situation_time_remaining** | **float** |  | [optional] 
**situation_time_elapsed** | **float** |  | [optional] 
**in_situation** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.game_linescore_power_play_info import GameLinescorePowerPlayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GameLinescorePowerPlayInfo from a JSON string
game_linescore_power_play_info_instance = GameLinescorePowerPlayInfo.from_json(json)
# print the JSON string representation of the object
print GameLinescorePowerPlayInfo.to_json()

# convert the object into a dict
game_linescore_power_play_info_dict = game_linescore_power_play_info_instance.to_dict()
# create an instance of GameLinescorePowerPlayInfo from a dict
game_linescore_power_play_info_form_dict = game_linescore_power_play_info.from_dict(game_linescore_power_play_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


