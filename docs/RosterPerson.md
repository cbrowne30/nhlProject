# RosterPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**full_name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.roster_person import RosterPerson

# TODO update the JSON string below
json = "{}"
# create an instance of RosterPerson from a JSON string
roster_person_instance = RosterPerson.from_json(json)
# print the JSON string representation of the object
print RosterPerson.to_json()

# convert the object into a dict
roster_person_dict = roster_person_instance.to_dict()
# create an instance of RosterPerson from a dict
roster_person_form_dict = roster_person.from_dict(roster_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


