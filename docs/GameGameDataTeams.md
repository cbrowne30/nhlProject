# GameGameDataTeams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**Team**](Team.md) |  | [optional] 
**home** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_game_data_teams import GameGameDataTeams

# TODO update the JSON string below
json = "{}"
# create an instance of GameGameDataTeams from a JSON string
game_game_data_teams_instance = GameGameDataTeams.from_json(json)
# print the JSON string representation of the object
print GameGameDataTeams.to_json()

# convert the object into a dict
game_game_data_teams_dict = game_game_data_teams_instance.to_dict()
# create an instance of GameGameDataTeams from a dict
game_game_data_teams_form_dict = game_game_data_teams.from_dict(game_game_data_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


