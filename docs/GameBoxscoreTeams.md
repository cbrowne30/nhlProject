# GameBoxscoreTeams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**GameBoxscoreTeam**](GameBoxscoreTeam.md) |  | [optional] 
**home** | [**GameBoxscoreTeam**](GameBoxscoreTeam.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_boxscore_teams import GameBoxscoreTeams

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxscoreTeams from a JSON string
game_boxscore_teams_instance = GameBoxscoreTeams.from_json(json)
# print the JSON string representation of the object
print GameBoxscoreTeams.to_json()

# convert the object into a dict
game_boxscore_teams_dict = game_boxscore_teams_instance.to_dict()
# create an instance of GameBoxscoreTeams from a dict
game_boxscore_teams_form_dict = game_boxscore_teams.from_dict(game_boxscore_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


