# VenueTimeZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**offset** | **float** |  | [optional] 
**tz** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.venue_time_zone import VenueTimeZone

# TODO update the JSON string below
json = "{}"
# create an instance of VenueTimeZone from a JSON string
venue_time_zone_instance = VenueTimeZone.from_json(json)
# print the JSON string representation of the object
print VenueTimeZone.to_json()

# convert the object into a dict
venue_time_zone_dict = venue_time_zone_instance.to_dict()
# create an instance of VenueTimeZone from a dict
venue_time_zone_form_dict = venue_time_zone.from_dict(venue_time_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


