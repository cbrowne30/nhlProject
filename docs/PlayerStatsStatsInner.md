# PlayerStatsStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlayerStatsStatsInnerType**](PlayerStatsStatsInnerType.md) |  | [optional] 
**splits** | [**List[PlayerStatsStatsInnerSplitsInner]**](PlayerStatsStatsInnerSplitsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_stats_stats_inner import PlayerStatsStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatsStatsInner from a JSON string
player_stats_stats_inner_instance = PlayerStatsStatsInner.from_json(json)
# print the JSON string representation of the object
print PlayerStatsStatsInner.to_json()

# convert the object into a dict
player_stats_stats_inner_dict = player_stats_stats_inner_instance.to_dict()
# create an instance of PlayerStatsStatsInner from a dict
player_stats_stats_inner_form_dict = player_stats_stats_inner.from_dict(player_stats_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


