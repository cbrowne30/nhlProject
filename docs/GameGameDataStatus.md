# GameGameDataStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abstract_game_state** | **str** |  | [optional] 
**coded_game_state** | **str** |  | [optional] 
**detailed_state** | **str** |  | [optional] 
**status_code** | **str** |  | [optional] 
**start_time_tbd** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.game_game_data_status import GameGameDataStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GameGameDataStatus from a JSON string
game_game_data_status_instance = GameGameDataStatus.from_json(json)
# print the JSON string representation of the object
print GameGameDataStatus.to_json()

# convert the object into a dict
game_game_data_status_dict = game_game_data_status_instance.to_dict()
# create an instance of GameGameDataStatus from a dict
game_game_data_status_form_dict = game_game_data_status.from_dict(game_game_data_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


