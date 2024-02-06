# GamePeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_type** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**num** | **float** |  | [optional] 
**ordinal_num** | **str** |  | [optional] 
**home** | [**GamePeriodHome**](GamePeriodHome.md) |  | [optional] 
**away** | [**GamePeriodAway**](GamePeriodAway.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_period import GamePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of GamePeriod from a JSON string
game_period_instance = GamePeriod.from_json(json)
# print the JSON string representation of the object
print GamePeriod.to_json()

# convert the object into a dict
game_period_dict = game_period_instance.to_dict()
# create an instance of GamePeriod from a dict
game_period_form_dict = game_period.from_dict(game_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


