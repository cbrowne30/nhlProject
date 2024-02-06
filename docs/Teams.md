# Teams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**teams** | [**List[Team]**](Team.md) |  | [optional] 

## Example

```python
from openapi_client.models.teams import Teams

# TODO update the JSON string below
json = "{}"
# create an instance of Teams from a JSON string
teams_instance = Teams.from_json(json)
# print the JSON string representation of the object
print Teams.to_json()

# convert the object into a dict
teams_dict = teams_instance.to_dict()
# create an instance of Teams from a dict
teams_form_dict = teams.from_dict(teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


