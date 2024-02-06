# Conferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **str** |  | [optional] 
**teams** | [**List[Conference]**](Conference.md) |  | [optional] 

## Example

```python
from openapi_client.models.conferences import Conferences

# TODO update the JSON string below
json = "{}"
# create an instance of Conferences from a JSON string
conferences_instance = Conferences.from_json(json)
# print the JSON string representation of the object
print Conferences.to_json()

# convert the object into a dict
conferences_dict = conferences_instance.to_dict()
# create an instance of Conferences from a dict
conferences_form_dict = conferences.from_dict(conferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


