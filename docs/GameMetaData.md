# GameMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wait** | **float** |  | [optional] 
**time_stamp** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_meta_data import GameMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of GameMetaData from a JSON string
game_meta_data_instance = GameMetaData.from_json(json)
# print the JSON string representation of the object
print GameMetaData.to_json()

# convert the object into a dict
game_meta_data_dict = game_meta_data_instance.to_dict()
# create an instance of GameMetaData from a dict
game_meta_data_form_dict = game_meta_data.from_dict(game_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


