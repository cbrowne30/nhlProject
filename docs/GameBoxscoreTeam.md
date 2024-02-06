# GameBoxscoreTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**GameBoxscoreTeamTeam**](GameBoxscoreTeamTeam.md) |  | [optional] 
**team_stats** | [**GameBoxscoreTeamTeamStats**](GameBoxscoreTeamTeamStats.md) |  | [optional] 
**players** | [**GameBoxscoreTeamPlayers**](GameBoxscoreTeamPlayers.md) |  | [optional] 
**goalies** | **List[float]** |  | [optional] 
**skaters** | **List[float]** |  | [optional] 
**on_ice** | **List[float]** |  | [optional] 
**on_ice_plus** | [**List[GameBoxscoreTeamOnIcePlusInner]**](GameBoxscoreTeamOnIcePlusInner.md) |  | [optional] 
**scratches** | **List[float]** |  | [optional] 
**penalty_box** | **List[float]** |  | [optional] 
**coaches** | [**List[GameBoxscoreTeamCoachesInner]**](GameBoxscoreTeamCoachesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_boxscore_team import GameBoxscoreTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxscoreTeam from a JSON string
game_boxscore_team_instance = GameBoxscoreTeam.from_json(json)
# print the JSON string representation of the object
print GameBoxscoreTeam.to_json()

# convert the object into a dict
game_boxscore_team_dict = game_boxscore_team_instance.to_dict()
# create an instance of GameBoxscoreTeam from a dict
game_boxscore_team_form_dict = game_boxscore_team.from_dict(game_boxscore_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


