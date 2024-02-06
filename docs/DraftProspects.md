# DraftProspects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**prospects** | [**List[DraftProspect]**](DraftProspect.md) |  | [optional] 

## Example

```python
from openapi_client.models.draft_prospects import DraftProspects

# TODO update the JSON string below
json = "{}"
# create an instance of DraftProspects from a JSON string
draft_prospects_instance = DraftProspects.from_json(json)
# print the JSON string representation of the object
print DraftProspects.to_json()

# convert the object into a dict
draft_prospects_dict = draft_prospects_instance.to_dict()
# create an instance of DraftProspects from a dict
draft_prospects_form_dict = draft_prospects.from_dict(draft_prospects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


