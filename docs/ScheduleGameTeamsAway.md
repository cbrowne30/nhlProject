# ScheduleGameTeamsAway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_record** | [**ScheduleGameTeamsAwayLeagueRecord**](ScheduleGameTeamsAwayLeagueRecord.md) |  | [optional] 
**score** | **float** |  | [optional] 
**team** | [**ScheduleGameTeamsAwayTeam**](ScheduleGameTeamsAwayTeam.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_game_teams_away import ScheduleGameTeamsAway

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGameTeamsAway from a JSON string
schedule_game_teams_away_instance = ScheduleGameTeamsAway.from_json(json)
# print the JSON string representation of the object
print ScheduleGameTeamsAway.to_json()

# convert the object into a dict
schedule_game_teams_away_dict = schedule_game_teams_away_instance.to_dict()
# create an instance of ScheduleGameTeamsAway from a dict
schedule_game_teams_away_form_dict = schedule_game_teams_away.from_dict(schedule_game_teams_away_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


