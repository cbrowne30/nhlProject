# GameContentEditorial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | [**GameEditorials**](GameEditorials.md) |  | [optional] 
**articles** | [**GameEditorials**](GameEditorials.md) |  | [optional] 
**recap** | [**GameEditorials**](GameEditorials.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_content_editorial import GameContentEditorial

# TODO update the JSON string below
json = "{}"
# create an instance of GameContentEditorial from a JSON string
game_content_editorial_instance = GameContentEditorial.from_json(json)
# print the JSON string representation of the object
print GameContentEditorial.to_json()

# convert the object into a dict
game_content_editorial_dict = game_content_editorial_instance.to_dict()
# create an instance of GameContentEditorial from a dict
game_content_editorial_form_dict = game_content_editorial.from_dict(game_content_editorial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


