# ScheduleGameTeamsHome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_record** | [**ScheduleGameTeamsHomeLeagueRecord**](ScheduleGameTeamsHomeLeagueRecord.md) |  | [optional] 
**score** | **float** |  | [optional] 
**team** | [**PlayerCurrentTeam**](PlayerCurrentTeam.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_game_teams_home import ScheduleGameTeamsHome

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGameTeamsHome from a JSON string
schedule_game_teams_home_instance = ScheduleGameTeamsHome.from_json(json)
# print the JSON string representation of the object
print ScheduleGameTeamsHome.to_json()

# convert the object into a dict
schedule_game_teams_home_dict = schedule_game_teams_home_instance.to_dict()
# create an instance of ScheduleGameTeamsHome from a dict
schedule_game_teams_home_form_dict = schedule_game_teams_home.from_dict(schedule_game_teams_home_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


