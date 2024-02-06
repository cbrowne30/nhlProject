# openapi_client.ScheduleApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedule**](ScheduleApi.md#get_schedule) | **GET** /schedule | Get the NHL game schedule.


# **get_schedule**
> Schedule get_schedule(expand=expand, team_id=team_id, start_date=start_date, end_date=end_date)

Get the NHL game schedule.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.schedule import Schedule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://statsapi.web.nhl.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://statsapi.web.nhl.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduleApi(api_client)
    expand = 'expand_example' # str | Expand explanations:   * `schedule.brodcasts` - Shows the broadcasts of the game.   * `schedule.linescore` - Linescore for completed games.   * `schedule.ticket` - Provides the different places to buy tickets for the upcoming games.   * `team.schedule.previous` - Same as above but for the last game played.  (optional)
    team_id = '28' # str | Limit results to a specific team. Team ids can be found through the teams endpoint (optional)
    start_date = 'Sat Feb 10 19:00:00 EST 2018' # date | Start date for the search. (optional)
    end_date = 'Sat Feb 17 19:00:00 EST 2018' # date | End date for the search. (optional)

    try:
        # Get the NHL game schedule.
        api_response = api_instance.get_schedule(expand=expand, team_id=team_id, start_date=start_date, end_date=end_date)
        print("The response of ScheduleApi->get_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleApi->get_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand explanations:   * &#x60;schedule.brodcasts&#x60; - Shows the broadcasts of the game.   * &#x60;schedule.linescore&#x60; - Linescore for completed games.   * &#x60;schedule.ticket&#x60; - Provides the different places to buy tickets for the upcoming games.   * &#x60;team.schedule.previous&#x60; - Same as above but for the last game played.  | [optional] 
 **team_id** | **str**| Limit results to a specific team. Team ids can be found through the teams endpoint | [optional] 
 **start_date** | **date**| Start date for the search. | [optional] 
 **end_date** | **date**| End date for the search. | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

