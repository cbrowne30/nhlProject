# ScheduleDay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**total_items** | **float** |  | [optional] 
**total_events** | **float** |  | [optional] 
**total_games** | **float** |  | [optional] 
**total_matches** | **float** |  | [optional] 
**games** | [**List[ScheduleGame]**](ScheduleGame.md) |  | [optional] 
**events** | **List[object]** |  | [optional] 
**matches** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_day import ScheduleDay

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDay from a JSON string
schedule_day_instance = ScheduleDay.from_json(json)
# print the JSON string representation of the object
print ScheduleDay.to_json()

# convert the object into a dict
schedule_day_dict = schedule_day_instance.to_dict()
# create an instance of ScheduleDay from a dict
schedule_day_form_dict = schedule_day.from_dict(schedule_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


