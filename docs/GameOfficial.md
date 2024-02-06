# GameOfficial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**official** | [**GameOfficialOfficial**](GameOfficialOfficial.md) |  | [optional] 
**official_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_official import GameOfficial

# TODO update the JSON string below
json = "{}"
# create an instance of GameOfficial from a JSON string
game_official_instance = GameOfficial.from_json(json)
# print the JSON string representation of the object
print GameOfficial.to_json()

# convert the object into a dict
game_official_dict = game_official_instance.to_dict()
# create an instance of GameOfficial from a dict
game_official_form_dict = game_official.from_dict(game_official_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


