# Divisions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**teams** | [**List[Division]**](Division.md) |  | [optional] 

## Example

```python
from openapi_client.models.divisions import Divisions

# TODO update the JSON string below
json = "{}"
# create an instance of Divisions from a JSON string
divisions_instance = Divisions.from_json(json)
# print the JSON string representation of the object
print Divisions.to_json()

# convert the object into a dict
divisions_dict = divisions_instance.to_dict()
# create an instance of Divisions from a dict
divisions_form_dict = divisions.from_dict(divisions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


