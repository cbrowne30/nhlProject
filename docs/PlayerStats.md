# PlayerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**stats** | [**List[PlayerStatsStatsInner]**](PlayerStatsStatsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_stats import PlayerStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStats from a JSON string
player_stats_instance = PlayerStats.from_json(json)
# print the JSON string representation of the object
print PlayerStats.to_json()

# convert the object into a dict
player_stats_dict = player_stats_instance.to_dict()
# create an instance of PlayerStats from a dict
player_stats_form_dict = player_stats.from_dict(player_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


