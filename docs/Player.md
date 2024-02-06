# Player


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**full_name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**primary_number** | **str** |  | [optional] 
**birth_date** | **date** |  | [optional] 
**current_age** | **float** |  | [optional] 
**birth_city** | **str** |  | [optional] 
**birth_state_province** | **str** |  | [optional] 
**birth_country** | **str** |  | [optional] 
**nationality** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**active** | **bool** |  | [optional] 
**alternate_captain** | **bool** |  | [optional] 
**captain** | **bool** |  | [optional] 
**rookie** | **bool** |  | [optional] 
**shoots_catches** | **str** |  | [optional] 
**roster_status** | **str** |  | [optional] 
**current_team** | [**PlayerCurrentTeam**](PlayerCurrentTeam.md) |  | [optional] 
**primary_position** | [**DraftProspectPrimaryPosition**](DraftProspectPrimaryPosition.md) |  | [optional] 

## Example

```python
from openapi_client.models.player import Player

# TODO update the JSON string below
json = "{}"
# create an instance of Player from a JSON string
player_instance = Player.from_json(json)
# print the JSON string representation of the object
print Player.to_json()

# convert the object into a dict
player_dict = player_instance.to_dict()
# create an instance of Player from a dict
player_form_dict = player.from_dict(player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


