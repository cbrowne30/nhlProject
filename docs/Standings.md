# Standings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**records** | [**List[StandingsRecordsInner]**](StandingsRecordsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.standings import Standings

# TODO update the JSON string below
json = "{}"
# create an instance of Standings from a JSON string
standings_instance = Standings.from_json(json)
# print the JSON string representation of the object
print Standings.to_json()

# convert the object into a dict
standings_dict = standings_instance.to_dict()
# create an instance of Standings from a dict
standings_form_dict = standings.from_dict(standings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


