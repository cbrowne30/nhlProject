# Team


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**venue** | [**Venue**](Venue.md) |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**tri_code** | **str** |  | [optional] 
**team_name** | **str** |  | [optional] 
**location_name** | **str** |  | [optional] 
**first_year_of_play** | **float** |  | [optional] 
**division** | [**StandingsRecordsInnerDivision**](StandingsRecordsInnerDivision.md) |  | [optional] 
**conference** | [**DivisionConference**](DivisionConference.md) |  | [optional] 
**franchise** | [**Franchise**](Franchise.md) |  | [optional] 
**roster** | [**TeamRoster**](TeamRoster.md) |  | [optional] 
**next_game_schedule** | [**TeamNextGameSchedule**](TeamNextGameSchedule.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**official_site_url** | **str** |  | [optional] 
**franchise_id** | **float** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print Team.to_json()

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_form_dict = team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


