# GameContentMediaMilestonesItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**time_absolute** | **datetime** |  | [optional] 
**time_offset** | **str** |  | [optional] 
**period** | **str** |  | [optional] 
**stats_event_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**player_id** | **str** |  | [optional] 
**period_time** | **str** |  | [optional] 
**ordinal_num** | **str** |  | [optional] 
**highlight** | [**GameHighlight**](GameHighlight.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_content_media_milestones_items_inner import GameContentMediaMilestonesItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GameContentMediaMilestonesItemsInner from a JSON string
game_content_media_milestones_items_inner_instance = GameContentMediaMilestonesItemsInner.from_json(json)
# print the JSON string representation of the object
print GameContentMediaMilestonesItemsInner.to_json()

# convert the object into a dict
game_content_media_milestones_items_inner_dict = game_content_media_milestones_items_inner_instance.to_dict()
# create an instance of GameContentMediaMilestonesItemsInner from a dict
game_content_media_milestones_items_inner_form_dict = game_content_media_milestones_items_inner.from_dict(game_content_media_milestones_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


