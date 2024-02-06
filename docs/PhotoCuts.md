# PhotoCuts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **str** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**src** | **str** |  | [optional] 
**at2x** | **str** |  | [optional] 
**at3x** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.photo_cuts import PhotoCuts

# TODO update the JSON string below
json = "{}"
# create an instance of PhotoCuts from a JSON string
photo_cuts_instance = PhotoCuts.from_json(json)
# print the JSON string representation of the object
print PhotoCuts.to_json()

# convert the object into a dict
photo_cuts_dict = photo_cuts_instance.to_dict()
# create an instance of PhotoCuts from a dict
photo_cuts_form_dict = photo_cuts.from_dict(photo_cuts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


