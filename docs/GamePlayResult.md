# GamePlayResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**event_code** | **str** |  | [optional] 
**event_type_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_play_result import GamePlayResult

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayResult from a JSON string
game_play_result_instance = GamePlayResult.from_json(json)
# print the JSON string representation of the object
print GamePlayResult.to_json()

# convert the object into a dict
game_play_result_dict = game_play_result_instance.to_dict()
# create an instance of GamePlayResult from a dict
game_play_result_form_dict = game_play_result.from_dict(game_play_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


