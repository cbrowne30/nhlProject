# GameEditorials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**topic_list** | **str** |  | [optional] 
**items** | [**List[GameEditorial]**](GameEditorial.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_editorials import GameEditorials

# TODO update the JSON string below
json = "{}"
# create an instance of GameEditorials from a JSON string
game_editorials_instance = GameEditorials.from_json(json)
# print the JSON string representation of the object
print GameEditorials.to_json()

# convert the object into a dict
game_editorials_dict = game_editorials_instance.to_dict()
# create an instance of GameEditorials from a dict
game_editorials_form_dict = game_editorials.from_dict(game_editorials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


