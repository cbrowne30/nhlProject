# ScheduleGameTeamsHomeLeagueRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wins** | **float** |  | [optional] 
**losses** | **float** |  | [optional] 
**ot** | **float** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_game_teams_home_league_record import ScheduleGameTeamsHomeLeagueRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGameTeamsHomeLeagueRecord from a JSON string
schedule_game_teams_home_league_record_instance = ScheduleGameTeamsHomeLeagueRecord.from_json(json)
# print the JSON string representation of the object
print ScheduleGameTeamsHomeLeagueRecord.to_json()

# convert the object into a dict
schedule_game_teams_home_league_record_dict = schedule_game_teams_home_league_record_instance.to_dict()
# create an instance of ScheduleGameTeamsHomeLeagueRecord from a dict
schedule_game_teams_home_league_record_form_dict = schedule_game_teams_home_league_record.from_dict(schedule_game_teams_home_league_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


