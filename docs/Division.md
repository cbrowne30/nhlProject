# Division


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**conference** | [**DivisionConference**](DivisionConference.md) |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.division import Division

# TODO update the JSON string below
json = "{}"
# create an instance of Division from a JSON string
division_instance = Division.from_json(json)
# print the JSON string representation of the object
print Division.to_json()

# convert the object into a dict
division_dict = division_instance.to_dict()
# create an instance of Division from a dict
division_form_dict = division.from_dict(division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


