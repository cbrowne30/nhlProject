# GameBoxscoreTeamPlayers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person** | [**GameBoxscoreTeamPlayersPerson**](GameBoxscoreTeamPlayersPerson.md) |  | [optional] 
**jersey_number** | **str** |  | [optional] 
**position** | [**GameBoxscoreTeamPlayersPosition**](GameBoxscoreTeamPlayersPosition.md) |  | [optional] 
**stats** | [**GameBoxscoreTeamPlayersStats**](GameBoxscoreTeamPlayersStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_boxscore_team_players import GameBoxscoreTeamPlayers

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxscoreTeamPlayers from a JSON string
game_boxscore_team_players_instance = GameBoxscoreTeamPlayers.from_json(json)
# print the JSON string representation of the object
print GameBoxscoreTeamPlayers.to_json()

# convert the object into a dict
game_boxscore_team_players_dict = game_boxscore_team_players_instance.to_dict()
# create an instance of GameBoxscoreTeamPlayers from a dict
game_boxscore_team_players_form_dict = game_boxscore_team_players.from_dict(game_boxscore_team_players_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


