# TeamNextGameSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **float** |  | [optional] 
**total_events** | **float** |  | [optional] 
**total_games** | **float** |  | [optional] 
**total_matches** | **float** |  | [optional] 
**dates** | [**List[TeamNextGameScheduleDatesInner]**](TeamNextGameScheduleDatesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_next_game_schedule import TeamNextGameSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TeamNextGameSchedule from a JSON string
team_next_game_schedule_instance = TeamNextGameSchedule.from_json(json)
# print the JSON string representation of the object
print TeamNextGameSchedule.to_json()

# convert the object into a dict
team_next_game_schedule_dict = team_next_game_schedule_instance.to_dict()
# create an instance of TeamNextGameSchedule from a dict
team_next_game_schedule_form_dict = team_next_game_schedule.from_dict(team_next_game_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


