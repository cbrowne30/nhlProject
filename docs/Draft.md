# Draft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**drafts** | [**List[DraftDraftsInner]**](DraftDraftsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.draft import Draft

# TODO update the JSON string below
json = "{}"
# create an instance of Draft from a JSON string
draft_instance = Draft.from_json(json)
# print the JSON string representation of the object
print Draft.to_json()

# convert the object into a dict
draft_dict = draft_instance.to_dict()
# create an instance of Draft from a dict
draft_form_dict = draft.from_dict(draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


