# Schedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**total_items** | **float** |  | [optional] 
**total_events** | **float** |  | [optional] 
**total_games** | **float** |  | [optional] 
**total_matches** | **float** |  | [optional] 
**wait** | **float** |  | [optional] 
**dates** | [**List[ScheduleDay]**](ScheduleDay.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print Schedule.to_json()

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_form_dict = schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


