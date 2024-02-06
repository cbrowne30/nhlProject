# ScheduleGameTicketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_type** | **str** |  | [optional] 
**ticket_link** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schedule_game_tickets_inner import ScheduleGameTicketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGameTicketsInner from a JSON string
schedule_game_tickets_inner_instance = ScheduleGameTicketsInner.from_json(json)
# print the JSON string representation of the object
print ScheduleGameTicketsInner.to_json()

# convert the object into a dict
schedule_game_tickets_inner_dict = schedule_game_tickets_inner_instance.to_dict()
# create an instance of ScheduleGameTicketsInner from a dict
schedule_game_tickets_inner_form_dict = schedule_game_tickets_inner.from_dict(schedule_game_tickets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


