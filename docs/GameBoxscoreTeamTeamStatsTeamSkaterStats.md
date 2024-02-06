# GameBoxscoreTeamTeamStatsTeamSkaterStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | **float** |  | [optional] 
**pim** | **float** |  | [optional] 
**shots** | **float** |  | [optional] 
**power_play_percentage** | **str** |  | [optional] 
**power_play_goals** | **float** |  | [optional] 
**power_play_opportunities** | **float** |  | [optional] 
**face_off_win_percentage** | **str** |  | [optional] 
**blocked** | **float** |  | [optional] 
**takeaways** | **float** |  | [optional] 
**giveaways** | **float** |  | [optional] 
**hits** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.game_boxscore_team_team_stats_team_skater_stats import GameBoxscoreTeamTeamStatsTeamSkaterStats

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxscoreTeamTeamStatsTeamSkaterStats from a JSON string
game_boxscore_team_team_stats_team_skater_stats_instance = GameBoxscoreTeamTeamStatsTeamSkaterStats.from_json(json)
# print the JSON string representation of the object
print GameBoxscoreTeamTeamStatsTeamSkaterStats.to_json()

# convert the object into a dict
game_boxscore_team_team_stats_team_skater_stats_dict = game_boxscore_team_team_stats_team_skater_stats_instance.to_dict()
# create an instance of GameBoxscoreTeamTeamStatsTeamSkaterStats from a dict
game_boxscore_team_team_stats_team_skater_stats_form_dict = game_boxscore_team_team_stats_team_skater_stats.from_dict(game_boxscore_team_team_stats_team_skater_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


