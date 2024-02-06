# TeamNextGameScheduleDatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**total_items** | **float** |  | [optional] 
**total_events** | **float** |  | [optional] 
**total_games** | **float** |  | [optional] 
**total_matches** | **float** |  | [optional] 
**games** | [**List[TeamNextGameScheduleDatesInnerGamesInner]**](TeamNextGameScheduleDatesInnerGamesInner.md) |  | [optional] 
**events** | **List[object]** |  | [optional] 
**matches** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.team_next_game_schedule_dates_inner import TeamNextGameScheduleDatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamNextGameScheduleDatesInner from a JSON string
team_next_game_schedule_dates_inner_instance = TeamNextGameScheduleDatesInner.from_json(json)
# print the JSON string representation of the object
print TeamNextGameScheduleDatesInner.to_json()

# convert the object into a dict
team_next_game_schedule_dates_inner_dict = team_next_game_schedule_dates_inner_instance.to_dict()
# create an instance of TeamNextGameScheduleDatesInner from a dict
team_next_game_schedule_dates_inner_form_dict = team_next_game_schedule_dates_inner.from_dict(team_next_game_schedule_dates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


