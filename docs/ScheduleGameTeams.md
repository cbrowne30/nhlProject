# ScheduleGameTeams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**ScheduleGameTeamsAway**](ScheduleGameTeamsAway.md) |  | [optional] 
**home** | [**ScheduleGameTeamsHome**](ScheduleGameTeamsHome.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_game_teams import ScheduleGameTeams

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGameTeams from a JSON string
schedule_game_teams_instance = ScheduleGameTeams.from_json(json)
# print the JSON string representation of the object
print ScheduleGameTeams.to_json()

# convert the object into a dict
schedule_game_teams_dict = schedule_game_teams_instance.to_dict()
# create an instance of ScheduleGameTeams from a dict
schedule_game_teams_form_dict = schedule_game_teams.from_dict(schedule_game_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


