# GameLinescore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_period** | **float** |  | [optional] 
**current_period_ordinal** | **str** |  | [optional] 
**current_period_time_remaining** | **str** |  | [optional] 
**periods** | [**List[GamePeriod]**](GamePeriod.md) |  | [optional] 
**shootout_info** | [**GameLinescoreShootoutInfo**](GameLinescoreShootoutInfo.md) |  | [optional] 
**teams** | [**GameLinescoreTeams**](GameLinescoreTeams.md) |  | [optional] 
**power_play_strength** | **str** |  | [optional] 
**has_shootout** | **bool** |  | [optional] 
**intermission_info** | [**GameLinescoreIntermissionInfo**](GameLinescoreIntermissionInfo.md) |  | [optional] 
**power_play_info** | [**GameLinescorePowerPlayInfo**](GameLinescorePowerPlayInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_linescore import GameLinescore

# TODO update the JSON string below
json = "{}"
# create an instance of GameLinescore from a JSON string
game_linescore_instance = GameLinescore.from_json(json)
# print the JSON string representation of the object
print GameLinescore.to_json()

# convert the object into a dict
game_linescore_dict = game_linescore_instance.to_dict()
# create an instance of GameLinescore from a dict
game_linescore_form_dict = game_linescore.from_dict(game_linescore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


