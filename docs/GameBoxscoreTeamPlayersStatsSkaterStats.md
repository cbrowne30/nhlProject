# GameBoxscoreTeamPlayersStatsSkaterStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_on_ice** | **str** |  | [optional] 
**assists** | **float** |  | [optional] 
**goals** | **float** |  | [optional] 
**shots** | **float** |  | [optional] 
**hits** | **float** |  | [optional] 
**power_play_goals** | **float** |  | [optional] 
**power_play_assists** | **float** |  | [optional] 
**penalty_minutes** | **float** |  | [optional] 
**face_off_wins** | **float** |  | [optional] 
**faceoff_taken** | **float** |  | [optional] 
**takeaways** | **float** |  | [optional] 
**giveaways** | **float** |  | [optional] 
**short_handed_goals** | **float** |  | [optional] 
**short_handed_assists** | **float** |  | [optional] 
**blocked** | **float** |  | [optional] 
**plus_minus** | **float** |  | [optional] 
**even_time_on_ice** | **str** |  | [optional] 
**power_play_time_on_ice** | **str** |  | [optional] 
**short_handed_time_on_ice** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_boxscore_team_players_stats_skater_stats import GameBoxscoreTeamPlayersStatsSkaterStats

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxscoreTeamPlayersStatsSkaterStats from a JSON string
game_boxscore_team_players_stats_skater_stats_instance = GameBoxscoreTeamPlayersStatsSkaterStats.from_json(json)
# print the JSON string representation of the object
print GameBoxscoreTeamPlayersStatsSkaterStats.to_json()

# convert the object into a dict
game_boxscore_team_players_stats_skater_stats_dict = game_boxscore_team_players_stats_skater_stats_instance.to_dict()
# create an instance of GameBoxscoreTeamPlayersStatsSkaterStats from a dict
game_boxscore_team_players_stats_skater_stats_form_dict = game_boxscore_team_players_stats_skater_stats.from_dict(game_boxscore_team_players_stats_skater_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


