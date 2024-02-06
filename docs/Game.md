# Game


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**game_pk** | **float** |  | [optional] 
**link** | **str** |  | [optional] 
**meta_data** | [**GameMetaData**](GameMetaData.md) |  | [optional] 
**game_data** | [**GameGameData**](GameGameData.md) |  | [optional] 
**live_data** | [**GameLiveData**](GameLiveData.md) |  | [optional] 

## Example

```python
from openapi_client.models.game import Game

# TODO update the JSON string below
json = "{}"
# create an instance of Game from a JSON string
game_instance = Game.from_json(json)
# print the JSON string representation of the object
print Game.to_json()

# convert the object into a dict
game_dict = game_instance.to_dict()
# create an instance of Game from a dict
game_form_dict = game.from_dict(game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


