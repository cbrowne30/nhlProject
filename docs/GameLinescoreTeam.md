# GameLinescoreTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**GameBoxscoreTeamTeam**](GameBoxscoreTeamTeam.md) |  | [optional] 
**goals** | **float** |  | [optional] 
**shots_on_goal** | **float** |  | [optional] 
**goalie_pulled** | **bool** |  | [optional] 
**num_skaters** | **float** |  | [optional] 
**power_play** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.game_linescore_team import GameLinescoreTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GameLinescoreTeam from a JSON string
game_linescore_team_instance = GameLinescoreTeam.from_json(json)
# print the JSON string representation of the object
print GameLinescoreTeam.to_json()

# convert the object into a dict
game_linescore_team_dict = game_linescore_team_instance.to_dict()
# create an instance of GameLinescoreTeam from a dict
game_linescore_team_form_dict = game_linescore_team.from_dict(game_linescore_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


