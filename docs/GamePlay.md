# GamePlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | [**List[GamePlayPlayersInner]**](GamePlayPlayersInner.md) |  | [optional] 
**result** | [**GamePlayResult**](GamePlayResult.md) |  | [optional] 
**about** | [**GamePlayAbout**](GamePlayAbout.md) |  | [optional] 
**coordinates** | [**GamePlayCoordinates**](GamePlayCoordinates.md) |  | [optional] 
**team** | [**GamePlayTeam**](GamePlayTeam.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_play import GamePlay

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlay from a JSON string
game_play_instance = GamePlay.from_json(json)
# print the JSON string representation of the object
print GamePlay.to_json()

# convert the object into a dict
game_play_dict = game_play_instance.to_dict()
# create an instance of GamePlay from a dict
game_play_form_dict = game_play.from_dict(game_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


