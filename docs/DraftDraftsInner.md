# DraftDraftsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_year** | **float** |  | [optional] 
**rounds** | [**List[DraftDraftsInnerRoundsInner]**](DraftDraftsInnerRoundsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.draft_drafts_inner import DraftDraftsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DraftDraftsInner from a JSON string
draft_drafts_inner_instance = DraftDraftsInner.from_json(json)
# print the JSON string representation of the object
print DraftDraftsInner.to_json()

# convert the object into a dict
draft_drafts_inner_dict = draft_drafts_inner_instance.to_dict()
# create an instance of DraftDraftsInner from a dict
draft_drafts_inner_form_dict = draft_drafts_inner.from_dict(draft_drafts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


