# StandingsRecordsInnerTeamRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**PlayerCurrentTeam**](PlayerCurrentTeam.md) |  | [optional] 
**league_record** | [**ScheduleGameTeamsHomeLeagueRecord**](ScheduleGameTeamsHomeLeagueRecord.md) |  | [optional] 
**goals_against** | **float** |  | [optional] 
**goals_scored** | **float** |  | [optional] 
**points** | **float** |  | [optional] 
**division_rank** | **str** |  | [optional] 
**conference_rank** | **str** |  | [optional] 
**league_rank** | **str** |  | [optional] 
**wild_card_rank** | **str** |  | [optional] 
**row** | **float** |  | [optional] 
**games_played** | **float** |  | [optional] 
**streak** | [**StandingsRecordsInnerTeamRecordsInnerStreak**](StandingsRecordsInnerTeamRecordsInnerStreak.md) |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.standings_records_inner_team_records_inner import StandingsRecordsInnerTeamRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StandingsRecordsInnerTeamRecordsInner from a JSON string
standings_records_inner_team_records_inner_instance = StandingsRecordsInnerTeamRecordsInner.from_json(json)
# print the JSON string representation of the object
print StandingsRecordsInnerTeamRecordsInner.to_json()

# convert the object into a dict
standings_records_inner_team_records_inner_dict = standings_records_inner_team_records_inner_instance.to_dict()
# create an instance of StandingsRecordsInnerTeamRecordsInner from a dict
standings_records_inner_team_records_inner_form_dict = standings_records_inner_team_records_inner.from_dict(standings_records_inner_team_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


