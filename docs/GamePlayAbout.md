# GamePlayAbout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_idx** | **float** |  | [optional] 
**event_id** | **float** |  | [optional] 
**period** | **float** |  | [optional] 
**period_type** | **str** |  | [optional] 
**ordinal_num** | **str** |  | [optional] 
**period_time** | **str** |  | [optional] 
**period_time_remaining** | **str** |  | [optional] 
**date_time** | **datetime** |  | [optional] 
**goals** | [**GamePlayAboutGoals**](GamePlayAboutGoals.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_play_about import GamePlayAbout

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayAbout from a JSON string
game_play_about_instance = GamePlayAbout.from_json(json)
# print the JSON string representation of the object
print GamePlayAbout.to_json()

# convert the object into a dict
game_play_about_dict = game_play_about_instance.to_dict()
# create an instance of GamePlayAbout from a dict
game_play_about_form_dict = game_play_about.from_dict(game_play_about_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


