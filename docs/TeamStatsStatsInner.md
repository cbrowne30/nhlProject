# TeamStatsStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TeamStatsStatsInnerType**](TeamStatsStatsInnerType.md) |  | [optional] 
**splits** | [**List[TeamStatsStatsInnerSplitsInner]**](TeamStatsStatsInnerSplitsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.team_stats_stats_inner import TeamStatsStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatsStatsInner from a JSON string
team_stats_stats_inner_instance = TeamStatsStatsInner.from_json(json)
# print the JSON string representation of the object
print TeamStatsStatsInner.to_json()

# convert the object into a dict
team_stats_stats_inner_dict = team_stats_stats_inner_instance.to_dict()
# create an instance of TeamStatsStatsInner from a dict
team_stats_stats_inner_form_dict = team_stats_stats_inner.from_dict(team_stats_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


