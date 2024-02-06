# GameLiveDataDecisions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**winner** | [**GameDecisionPlayer**](GameDecisionPlayer.md) |  | [optional] 
**loser** | [**GameDecisionPlayer**](GameDecisionPlayer.md) |  | [optional] 
**first_star** | [**GameDecisionPlayer**](GameDecisionPlayer.md) |  | [optional] 
**second_star** | [**GameDecisionPlayer**](GameDecisionPlayer.md) |  | [optional] 
**third_star** | [**GameDecisionPlayer**](GameDecisionPlayer.md) |  | [optional] 

## Example

```python
from openapi_client.models.game_live_data_decisions import GameLiveDataDecisions

# TODO update the JSON string below
json = "{}"
# create an instance of GameLiveDataDecisions from a JSON string
game_live_data_decisions_instance = GameLiveDataDecisions.from_json(json)
# print the JSON string representation of the object
print GameLiveDataDecisions.to_json()

# convert the object into a dict
game_live_data_decisions_dict = game_live_data_decisions_instance.to_dict()
# create an instance of GameLiveDataDecisions from a dict
game_live_data_decisions_form_dict = game_live_data_decisions.from_dict(game_live_data_decisions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


