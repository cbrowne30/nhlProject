# PlayerCurrentTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.player_current_team import PlayerCurrentTeam

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerCurrentTeam from a JSON string
player_current_team_instance = PlayerCurrentTeam.from_json(json)
# print the JSON string representation of the object
print PlayerCurrentTeam.to_json()

# convert the object into a dict
player_current_team_dict = player_current_team_instance.to_dict()
# create an instance of PlayerCurrentTeam from a dict
player_current_team_form_dict = player_current_team.from_dict(player_current_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


