# GameEditorial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**headline** | **str** |  | [optional] 
**subhead** | **str** |  | [optional] 
**seo_title** | **str** |  | [optional] 
**seo_description** | **str** |  | [optional] 
**seo_keywords** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**commenting** | **bool** |  | [optional] 
**tagline** | **str** |  | [optional] 
**token_data** | [**GameEditorialTokenData**](GameEditorialTokenData.md) |  | [optional] 
**contributor** | [**GameEditorialContributor**](GameEditorialContributor.md) |  | [optional] 
**keywords_display** | [**List[GameEditorialKeyword]**](GameEditorialKeyword.md) |  | [optional] 
**keywords_all** | [**List[GameEditorialKeyword]**](GameEditorialKeyword.md) |  | [optional] 
**approval** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**data_uri** | **str** |  | [optional] 
**primary_keyword** | [**GameEditorialKeyword**](GameEditorialKeyword.md) |  | [optional] 
**media** | [**GameEditorialMedia**](GameEditorialMedia.md) |  | [optional] 
**preview** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_editorial import GameEditorial

# TODO update the JSON string below
json = "{}"
# create an instance of GameEditorial from a JSON string
game_editorial_instance = GameEditorial.from_json(json)
# print the JSON string representation of the object
print GameEditorial.to_json()

# convert the object into a dict
game_editorial_dict = game_editorial_instance.to_dict()
# create an instance of GameEditorial from a dict
game_editorial_form_dict = game_editorial.from_dict(game_editorial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


