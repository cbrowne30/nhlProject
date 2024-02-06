# openapi_client.DivisionsApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_division**](DivisionsApi.md#get_division) | **GET** /divisions/{id} | Get an NHL division.
[**get_divisions**](DivisionsApi.md#get_divisions) | **GET** /divisions | Get all current NHL divisions.


# **get_division**
> Division get_division(id)

Get an NHL division.

You can use this to also retrieve inactive divisions. For example, the ID for the old Patrick division is `13`.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.division import Division
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
    api_instance = openapi_client.DivisionsApi(api_client)
    id = 15 # float | The ID of the division.

    try:
        # Get an NHL division.
        api_response = api_instance.get_division(id)
        print("The response of DivisionsApi->get_division:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DivisionsApi->get_division: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the division. | 

### Return type

[**Division**](Division.md)

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

# **get_divisions**
> Divisions get_divisions()

Get all current NHL divisions.

This only retrieves active divisions. For inactive divisions, use `/divisions/{id}`.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.divisions import Divisions
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
    api_instance = openapi_client.DivisionsApi(api_client)

    try:
        # Get all current NHL divisions.
        api_response = api_instance.get_divisions()
        print("The response of DivisionsApi->get_divisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DivisionsApi->get_divisions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Divisions**](Divisions.md)

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

