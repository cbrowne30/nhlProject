# GameLiveDataPlays


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_plays** | [**List[GamePlay]**](GamePlay.md) |  | [optional] 
**scoring_plays** | **List[float]** |  | [optional] 
**penalty_plays** | **List[float]** |  | [optional] 
**plays_by_period** | [**List[GameLiveDataPlaysPlaysByPeriodInner]**](GameLiveDataPlaysPlaysByPeriodInner.md) |  | [optional] 
**current_play** | [**GamePlay**](GamePlay.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_live_data_plays import GameLiveDataPlays

# TODO update the JSON string below
json = "{}"
# create an instance of GameLiveDataPlays from a JSON string
game_live_data_plays_instance = GameLiveDataPlays.from_json(json)
# print the JSON string representation of the object
print GameLiveDataPlays.to_json()

# convert the object into a dict
game_live_data_plays_dict = game_live_data_plays_instance.to_dict()
# create an instance of GameLiveDataPlays from a dict
game_live_data_plays_form_dict = game_live_data_plays.from_dict(game_live_data_plays_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


