# GameContentMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epg** | [**List[GameContentMediaEpgInner]**](GameContentMediaEpgInner.md) |  | [optional] 
**milestones** | [**GameContentMediaMilestones**](GameContentMediaMilestones.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_content_media import GameContentMedia

# TODO update the JSON string below
json = "{}"
# create an instance of GameContentMedia from a JSON string
game_content_media_instance = GameContentMedia.from_json(json)
# print the JSON string representation of the object
print GameContentMedia.to_json()

# convert the object into a dict
game_content_media_dict = game_content_media_instance.to_dict()
# create an instance of GameContentMedia from a dict
game_content_media_form_dict = game_content_media.from_dict(game_content_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


