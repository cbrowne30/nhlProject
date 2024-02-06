# PlayerStatsStatsInnerSplitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **str** |  | [optional] 
**stat** | [**PlayerStatsStatsInnerSplitsInnerStat**](PlayerStatsStatsInnerSplitsInnerStat.md) |  | [optional] 
**is_home** | **bool** |  | [optional] 
**is_win** | **bool** |  | [optional] 
**is_ot** | **bool** |  | [optional] 
**month** | **float** |  | [optional] 
**day_of_week** | **float** |  | [optional] 
**opponent** | [**DraftDraftsInnerRoundsInnerPicksInnerTeam**](DraftDraftsInnerRoundsInnerPicksInnerTeam.md) |  | [optional] 
**opponent_division** | [**PlayerStatsStatsInnerSplitsInnerOpponentDivision**](PlayerStatsStatsInnerSplitsInnerOpponentDivision.md) |  | [optional] 
**opponent_conference** | [**DivisionConference**](DivisionConference.md) |  | [optional] 

## Example

```python
from openapi_client.models.player_stats_stats_inner_splits_inner import PlayerStatsStatsInnerSplitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatsStatsInnerSplitsInner from a JSON string
player_stats_stats_inner_splits_inner_instance = PlayerStatsStatsInnerSplitsInner.from_json(json)
# print the JSON string representation of the object
print PlayerStatsStatsInnerSplitsInner.to_json()

# convert the object into a dict
player_stats_stats_inner_splits_inner_dict = player_stats_stats_inner_splits_inner_instance.to_dict()
# create an instance of PlayerStatsStatsInnerSplitsInner from a dict
player_stats_stats_inner_splits_inner_form_dict = player_stats_stats_inner_splits_inner.from_dict(player_stats_stats_inner_splits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


