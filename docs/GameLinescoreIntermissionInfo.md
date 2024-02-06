# GameLinescoreIntermissionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intermission_time_remaining** | **float** |  | [optional] 
**intermission_time_elapsed** | **float** |  | [optional] 
**in_intermission** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.game_linescore_intermission_info import GameLinescoreIntermissionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GameLinescoreIntermissionInfo from a JSON string
game_linescore_intermission_info_instance = GameLinescoreIntermissionInfo.from_json(json)
# print the JSON string representation of the object
print GameLinescoreIntermissionInfo.to_json()

# convert the object into a dict
game_linescore_intermission_info_dict = game_linescore_intermission_info_instance.to_dict()
# create an instance of GameLinescoreIntermissionInfo from a dict
game_linescore_intermission_info_form_dict = game_linescore_intermission_info.from_dict(game_linescore_intermission_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


