# GameEditorialContributor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributors** | [**List[GameEditorialContributorContributorsInner]**](GameEditorialContributorContributorsInner.md) |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.game_editorial_contributor import GameEditorialContributor

# TODO update the JSON string below
json = "{}"
# create an instance of GameEditorialContributor from a JSON string
game_editorial_contributor_instance = GameEditorialContributor.from_json(json)
# print the JSON string representation of the object
print GameEditorialContributor.to_json()

# convert the object into a dict
game_editorial_contributor_dict = game_editorial_contributor_instance.to_dict()
# create an instance of GameEditorialContributor from a dict
game_editorial_contributor_form_dict = game_editorial_contributor.from_dict(game_editorial_contributor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


