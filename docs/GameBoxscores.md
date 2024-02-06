# GameBoxscores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**GameBoxscoreTeams**](GameBoxscoreTeams.md) |  | [optional] 
**officials** | [**List[GameOfficial]**](GameOfficial.md) |  | [optional] 
**copyright** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_boxscores import GameBoxscores

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxscores from a JSON string
game_boxscores_instance = GameBoxscores.from_json(json)
# print the JSON string representation of the object
print GameBoxscores.to_json()

# convert the object into a dict
game_boxscores_dict = game_boxscores_instance.to_dict()
# create an instance of GameBoxscores from a dict
game_boxscores_form_dict = game_boxscores.from_dict(game_boxscores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


