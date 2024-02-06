# GameLinescoreShootoutInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**GameLinescoreShootoutInfoAway**](GameLinescoreShootoutInfoAway.md) |  | [optional] 
**home** | [**GameLinescoreShootoutInfoAway**](GameLinescoreShootoutInfoAway.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_linescore_shootout_info import GameLinescoreShootoutInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GameLinescoreShootoutInfo from a JSON string
game_linescore_shootout_info_instance = GameLinescoreShootoutInfo.from_json(json)
# print the JSON string representation of the object
print GameLinescoreShootoutInfo.to_json()

# convert the object into a dict
game_linescore_shootout_info_dict = game_linescore_shootout_info_instance.to_dict()
# create an instance of GameLinescoreShootoutInfo from a dict
game_linescore_shootout_info_form_dict = game_linescore_shootout_info.from_dict(game_linescore_shootout_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


