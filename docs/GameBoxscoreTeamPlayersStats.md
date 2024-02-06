# GameBoxscoreTeamPlayersStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skater_stats** | [**GameBoxscoreTeamPlayersStatsSkaterStats**](GameBoxscoreTeamPlayersStatsSkaterStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_boxscore_team_players_stats import GameBoxscoreTeamPlayersStats

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxscoreTeamPlayersStats from a JSON string
game_boxscore_team_players_stats_instance = GameBoxscoreTeamPlayersStats.from_json(json)
# print the JSON string representation of the object
print GameBoxscoreTeamPlayersStats.to_json()

# convert the object into a dict
game_boxscore_team_players_stats_dict = game_boxscore_team_players_stats_instance.to_dict()
# create an instance of GameBoxscoreTeamPlayersStats from a dict
game_boxscore_team_players_stats_form_dict = game_boxscore_team_players_stats.from_dict(game_boxscore_team_players_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


