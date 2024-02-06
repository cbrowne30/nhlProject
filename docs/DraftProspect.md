# DraftProspect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**full_name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**birth_date** | **date** |  | [optional] 
**birth_city** | **str** |  | [optional] 
**birth_country** | **str** |  | [optional] 
**nationality** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**shoots_catches** | **str** |  | [optional] 
**primary_position** | [**DraftProspectPrimaryPosition**](DraftProspectPrimaryPosition.md) |  | [optional] 
**prospect_category** | [**DraftProspectProspectCategory**](DraftProspectProspectCategory.md) |  | [optional] 
**amateur_team** | [**DraftProspectAmateurTeam**](DraftProspectAmateurTeam.md) |  | [optional] 
**amateur_league** | [**DraftProspectAmateurLeague**](DraftProspectAmateurLeague.md) |  | [optional] 
**ranks** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.draft_prospect import DraftProspect

# TODO update the JSON string below
json = "{}"
# create an instance of DraftProspect from a JSON string
draft_prospect_instance = DraftProspect.from_json(json)
# print the JSON string representation of the object
print DraftProspect.to_json()

# convert the object into a dict
draft_prospect_dict = draft_prospect_instance.to_dict()
# create an instance of DraftProspect from a dict
draft_prospect_form_dict = draft_prospect.from_dict(draft_prospect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


