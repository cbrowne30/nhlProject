# GameLiveData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plays** | [**GameLiveDataPlays**](GameLiveDataPlays.md) |  | [optional] 
**linescore** | [**GameLinescore**](GameLinescore.md) |  | [optional] 
**boxscore** | [**GameBoxscore**](GameBoxscore.md) |  | [optional] 
**decisions** | [**GameLiveDataDecisions**](GameLiveDataDecisions.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_live_data import GameLiveData

# TODO update the JSON string below
json = "{}"
# create an instance of GameLiveData from a JSON string
game_live_data_instance = GameLiveData.from_json(json)
# print the JSON string representation of the object
print GameLiveData.to_json()

# convert the object into a dict
game_live_data_dict = game_live_data_instance.to_dict()
# create an instance of GameLiveData from a dict
game_live_data_form_dict = game_live_data.from_dict(game_live_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


