# GamePlayTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**tri_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_play_team import GamePlayTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GamePlayTeam from a JSON string
game_play_team_instance = GamePlayTeam.from_json(json)
# print the JSON string representation of the object
print GamePlayTeam.to_json()

# convert the object into a dict
game_play_team_dict = game_play_team_instance.to_dict()
# create an instance of GamePlayTeam from a dict
game_play_team_form_dict = game_play_team.from_dict(game_play_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


