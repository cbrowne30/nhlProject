# TeamStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**stats** | [**List[TeamStatsStatsInner]**](TeamStatsStatsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_stats import TeamStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStats from a JSON string
team_stats_instance = TeamStats.from_json(json)
# print the JSON string representation of the object
print TeamStats.to_json()

# convert the object into a dict
team_stats_dict = team_stats_instance.to_dict()
# create an instance of TeamStats from a dict
team_stats_form_dict = team_stats.from_dict(team_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


