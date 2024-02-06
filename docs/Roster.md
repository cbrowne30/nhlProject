# Roster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person** | [**RosterPerson**](RosterPerson.md) |  | [optional] 
**jersey_number** | **float** |  | [optional] 
**position** | [**DraftProspectPrimaryPosition**](DraftProspectPrimaryPosition.md) |  | [optional] 

## Example

```python
from openapi_client.models.roster import Roster

# TODO update the JSON string below
json = "{}"
# create an instance of Roster from a JSON string
roster_instance = Roster.from_json(json)
# print the JSON string representation of the object
print Roster.to_json()

# convert the object into a dict
roster_dict = roster_instance.to_dict()
# create an instance of Roster from a dict
roster_form_dict = roster.from_dict(roster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


