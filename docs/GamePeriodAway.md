# GamePeriodAway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | **float** |  | [optional] 
**shots_on_goal** | **float** |  | [optional] 
**rink_side** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_period_away import GamePeriodAway

# TODO update the JSON string below
json = "{}"
# create an instance of GamePeriodAway from a JSON string
game_period_away_instance = GamePeriodAway.from_json(json)
# print the JSON string representation of the object
print GamePeriodAway.to_json()

# convert the object into a dict
game_period_away_dict = game_period_away_instance.to_dict()
# create an instance of GamePeriodAway from a dict
game_period_away_form_dict = game_period_away.from_dict(game_period_away_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


