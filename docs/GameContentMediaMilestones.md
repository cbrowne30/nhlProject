# GameContentMediaMilestones


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**stream_start** | **datetime** |  | [optional] 
**items** | [**List[GameContentMediaMilestonesItemsInner]**](GameContentMediaMilestonesItemsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_content_media_milestones import GameContentMediaMilestones

# TODO update the JSON string below
json = "{}"
# create an instance of GameContentMediaMilestones from a JSON string
game_content_media_milestones_instance = GameContentMediaMilestones.from_json(json)
# print the JSON string representation of the object
print GameContentMediaMilestones.to_json()

# convert the object into a dict
game_content_media_milestones_dict = game_content_media_milestones_instance.to_dict()
# create an instance of GameContentMediaMilestones from a dict
game_content_media_milestones_form_dict = game_content_media_milestones.from_dict(game_content_media_milestones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


