# openapi_client.StatsApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stat_types**](StatsApi.md#get_stat_types) | **GET** /statTypes | Get all available NHL statistic types.


# **get_stat_types**
> List[StatTypesInner] get_stat_types()

Get all available NHL statistic types.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.stat_types_inner import StatTypesInner
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
    api_instance = openapi_client.StatsApi(api_client)

    try:
        # Get all available NHL statistic types.
        api_response = api_instance.get_stat_types()
        print("The response of StatsApi->get_stat_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_stat_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StatTypesInner]**](StatTypesInner.md)

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

