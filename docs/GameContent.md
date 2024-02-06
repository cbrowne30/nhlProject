# GameContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**editorial** | [**GameContentEditorial**](GameContentEditorial.md) |  | [optional] 
**media** | [**GameContentMedia**](GameContentMedia.md) |  | [optional] 
**highlights** | [**GameContentHighlights**](GameContentHighlights.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_content import GameContent

# TODO update the JSON string below
json = "{}"
# create an instance of GameContent from a JSON string
game_content_instance = GameContent.from_json(json)
# print the JSON string representation of the object
print GameContent.to_json()

# convert the object into a dict
game_content_dict = game_content_instance.to_dict()
# create an instance of GameContent from a dict
game_content_form_dict = game_content.from_dict(game_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


