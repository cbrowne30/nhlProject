# GameBoxscore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**GameBoxscoreTeams**](GameBoxscoreTeams.md) |  | [optional] 
**officials** | [**List[GameOfficial]**](GameOfficial.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_boxscore import GameBoxscore

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxscore from a JSON string
game_boxscore_instance = GameBoxscore.from_json(json)
# print the JSON string representation of the object
print GameBoxscore.to_json()

# convert the object into a dict
game_boxscore_dict = game_boxscore_instance.to_dict()
# create an instance of GameBoxscore from a dict
game_boxscore_form_dict = game_boxscore.from_dict(game_boxscore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


