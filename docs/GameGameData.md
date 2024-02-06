# GameGameData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game** | [**GameGameDataGame**](GameGameDataGame.md) |  | [optional] 
**datetime** | [**GameGameDataDatetime**](GameGameDataDatetime.md) |  | [optional] 
**status** | [**GameGameDataStatus**](GameGameDataStatus.md) |  | [optional] 
**teams** | [**GameGameDataTeams**](GameGameDataTeams.md) |  | [optional] 
**players** | [**Player**](Player.md) |  | [optional] 
**venue** | [**GameGameDataVenue**](GameGameDataVenue.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_game_data import GameGameData

# TODO update the JSON string below
json = "{}"
# create an instance of GameGameData from a JSON string
game_game_data_instance = GameGameData.from_json(json)
# print the JSON string representation of the object
print GameGameData.to_json()

# convert the object into a dict
game_game_data_dict = game_game_data_instance.to_dict()
# create an instance of GameGameData from a dict
game_game_data_form_dict = game_game_data.from_dict(game_game_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


