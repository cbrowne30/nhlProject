# TeamStatsStatsInnerSplitsInnerStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games_played** | **float** |  | [optional] 
**wins** | **float** |  | [optional] 
**losses** | **float** |  | [optional] 
**ot** | **float** |  | [optional] 
**pts** | **float** |  | [optional] 
**pt_pctg** | **str** |  | [optional] 
**goals_per_game** | **float** |  | [optional] 
**goals_against_per_game** | **float** |  | [optional] 
**ev_gga_ratio** | **float** |  | [optional] 
**power_play_percentage** | **str** |  | [optional] 
**power_play_goals** | **float** |  | [optional] 
**power_play_goals_against** | **float** |  | [optional] 
**power_play_opportunities** | **float** |  | [optional] 
**penalty_kill_percentage** | **str** |  | [optional] 
**shots_per_game** | **float** |  | [optional] 
**shots_allowed** | **float** |  | [optional] 
**win_score_first** | **float** |  | [optional] 
**win_opp_score_first** | **float** |  | [optional] 
**win_lead_first_per** | **float** |  | [optional] 
**win_lead_second_per** | **float** |  | [optional] 
**win_outshoot_opp** | **float** |  | [optional] 
**win_outshot_by_opp** | **float** |  | [optional] 
**face_offs_taken** | **float** |  | [optional] 
**face_offs_won** | **float** |  | [optional] 
**face_offs_lost** | **float** |  | [optional] 
**face_off_win_percentage** | **str** |  | [optional] 
**shooting_pctg** | **float** |  | [optional] 
**save_pctg** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.team_stats_stats_inner_splits_inner_stat import TeamStatsStatsInnerSplitsInnerStat

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatsStatsInnerSplitsInnerStat from a JSON string
team_stats_stats_inner_splits_inner_stat_instance = TeamStatsStatsInnerSplitsInnerStat.from_json(json)
# print the JSON string representation of the object
print TeamStatsStatsInnerSplitsInnerStat.to_json()

# convert the object into a dict
team_stats_stats_inner_splits_inner_stat_dict = team_stats_stats_inner_splits_inner_stat_instance.to_dict()
# create an instance of TeamStatsStatsInnerSplitsInnerStat from a dict
team_stats_stats_inner_splits_inner_stat_form_dict = team_stats_stats_inner_splits_inner_stat.from_dict(team_stats_stats_inner_splits_inner_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


