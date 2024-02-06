# DraftDraftsInnerRoundsInnerPicksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **float** |  | [optional] 
**round** | **str** |  | [optional] 
**pick_overall** | **float** |  | [optional] 
**pick_in_round** | **float** |  | [optional] 
**team** | [**DraftDraftsInnerRoundsInnerPicksInnerTeam**](DraftDraftsInnerRoundsInnerPicksInnerTeam.md) |  | [optional] 
**prospect** | [**DraftDraftsInnerRoundsInnerPicksInnerProspect**](DraftDraftsInnerRoundsInnerPicksInnerProspect.md) |  | [optional] 

## Example

```python
from openapi_client.models.draft_drafts_inner_rounds_inner_picks_inner import DraftDraftsInnerRoundsInnerPicksInner

# TODO update the JSON string below
json = "{}"
# create an instance of DraftDraftsInnerRoundsInnerPicksInner from a JSON string
draft_drafts_inner_rounds_inner_picks_inner_instance = DraftDraftsInnerRoundsInnerPicksInner.from_json(json)
# print the JSON string representation of the object
print DraftDraftsInnerRoundsInnerPicksInner.to_json()

# convert the object into a dict
draft_drafts_inner_rounds_inner_picks_inner_dict = draft_drafts_inner_rounds_inner_picks_inner_instance.to_dict()
# create an instance of DraftDraftsInnerRoundsInnerPicksInner from a dict
draft_drafts_inner_rounds_inner_picks_inner_form_dict = draft_drafts_inner_rounds_inner_picks_inner.from_dict(draft_drafts_inner_rounds_inner_picks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


