# Conference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.conference import Conference

# TODO update the JSON string below
json = "{}"
# create an instance of Conference from a JSON string
conference_instance = Conference.from_json(json)
# print the JSON string representation of the object
print Conference.to_json()

# convert the object into a dict
conference_dict = conference_instance.to_dict()
# create an instance of Conference from a dict
conference_form_dict = conference.from_dict(conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


