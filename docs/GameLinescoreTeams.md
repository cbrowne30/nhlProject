# GameLinescoreTeams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home** | [**GameLinescoreTeam**](GameLinescoreTeam.md) |  | [optional] 
**away** | [**GameLinescoreTeam**](GameLinescoreTeam.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_linescore_teams import GameLinescoreTeams

# TODO update the JSON string below
json = "{}"
# create an instance of GameLinescoreTeams from a JSON string
game_linescore_teams_instance = GameLinescoreTeams.from_json(json)
# print the JSON string representation of the object
print GameLinescoreTeams.to_json()

# convert the object into a dict
game_linescore_teams_dict = game_linescore_teams_instance.to_dict()
# create an instance of GameLinescoreTeams from a dict
game_linescore_teams_form_dict = game_linescore_teams.from_dict(game_linescore_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


