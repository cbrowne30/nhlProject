# Rosters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**teams** | [**List[Roster]**](Roster.md) |  | [optional] 

## Example

```python
from openapi_client.models.rosters import Rosters

# TODO update the JSON string below
json = "{}"
# create an instance of Rosters from a JSON string
rosters_instance = Rosters.from_json(json)
# print the JSON string representation of the object
print Rosters.to_json()

# convert the object into a dict
rosters_dict = rosters_instance.to_dict()
# create an instance of Rosters from a dict
rosters_form_dict = rosters.from_dict(rosters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


