# StandingsRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standings_type** | **str** |  | [optional] 
**league** | [**StandingsRecordsInnerLeague**](StandingsRecordsInnerLeague.md) |  | [optional] 
**division** | [**StandingsRecordsInnerDivision**](StandingsRecordsInnerDivision.md) |  | [optional] 
**conference** | [**DivisionConference**](DivisionConference.md) |  | [optional] 
**team_records** | [**List[StandingsRecordsInnerTeamRecordsInner]**](StandingsRecordsInnerTeamRecordsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.standings_records_inner import StandingsRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StandingsRecordsInner from a JSON string
standings_records_inner_instance = StandingsRecordsInner.from_json(json)
# print the JSON string representation of the object
print StandingsRecordsInner.to_json()

# convert the object into a dict
standings_records_inner_dict = standings_records_inner_instance.to_dict()
# create an instance of StandingsRecordsInner from a dict
standings_records_inner_form_dict = standings_records_inner.from_dict(standings_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


