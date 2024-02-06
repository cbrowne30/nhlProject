# GameEditorialTokenData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_guid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**seo_name** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**href_mobile** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_editorial_token_data import GameEditorialTokenData

# TODO update the JSON string below
json = "{}"
# create an instance of GameEditorialTokenData from a JSON string
game_editorial_token_data_instance = GameEditorialTokenData.from_json(json)
# print the JSON string representation of the object
print GameEditorialTokenData.to_json()

# convert the object into a dict
game_editorial_token_data_dict = game_editorial_token_data_instance.to_dict()
# create an instance of GameEditorialTokenData from a dict
game_editorial_token_data_form_dict = game_editorial_token_data.from_dict(game_editorial_token_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


