# TeamNextGameScheduleDatesInnerGamesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_pk** | **float** |  | [optional] 
**link** | **str** |  | [optional] 
**game_type** | **str** |  | [optional] 
**season** | **str** |  | [optional] 
**game_date** | **datetime** |  | [optional] 
**status** | [**TeamNextGameScheduleDatesInnerGamesInnerStatus**](TeamNextGameScheduleDatesInnerGamesInnerStatus.md) |  | [optional] 
**teams** | [**TeamNextGameScheduleDatesInnerGamesInnerTeams**](TeamNextGameScheduleDatesInnerGamesInnerTeams.md) |  | [optional] 
**venue** | [**GameGameDataVenue**](GameGameDataVenue.md) |  | [optional] 
**content** | [**ScheduleGameContent**](ScheduleGameContent.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_next_game_schedule_dates_inner_games_inner import TeamNextGameScheduleDatesInnerGamesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamNextGameScheduleDatesInnerGamesInner from a JSON string
team_next_game_schedule_dates_inner_games_inner_instance = TeamNextGameScheduleDatesInnerGamesInner.from_json(json)
# print the JSON string representation of the object
print TeamNextGameScheduleDatesInnerGamesInner.to_json()

# convert the object into a dict
team_next_game_schedule_dates_inner_games_inner_dict = team_next_game_schedule_dates_inner_games_inner_instance.to_dict()
# create an instance of TeamNextGameScheduleDatesInnerGamesInner from a dict
team_next_game_schedule_dates_inner_games_inner_form_dict = team_next_game_schedule_dates_inner_games_inner.from_dict(team_next_game_schedule_dates_inner_games_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


