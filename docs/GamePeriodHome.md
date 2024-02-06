# GamePeriodHome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | **float** |  | [optional] 
**shots_on_goal** | **float** |  | [optional] 
**rink_side** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_period_home import GamePeriodHome

# TODO update the JSON string below
json = "{}"
# create an instance of GamePeriodHome from a JSON string
game_period_home_instance = GamePeriodHome.from_json(json)
# print the JSON string representation of the object
print GamePeriodHome.to_json()

# convert the object into a dict
game_period_home_dict = game_period_home_instance.to_dict()
# create an instance of GamePeriodHome from a dict
game_period_home_form_dict = game_period_home.from_dict(game_period_home_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


