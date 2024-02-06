# openapi_client.DraftApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_draft**](DraftApi.md#get_draft) | **GET** /draft | Get round-by-round data for current year&#39;s NHL Entry Draft.
[**get_draft_by_year**](DraftApi.md#get_draft_by_year) | **GET** /draft/{year} | Get round-by-round data for a specific year&#39;s NHL Entry Draft.
[**get_draft_prospect**](DraftApi.md#get_draft_prospect) | **GET** /draft/prospects/{id} | Get an NHL Entry Draft prospect.
[**get_draft_prospects**](DraftApi.md#get_draft_prospects) | **GET** /draft/prospects | Get all NHL Entry Draft prospects.


# **get_draft**
> Draft get_draft()

Get round-by-round data for current year's NHL Entry Draft.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.draft import Draft
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
    api_instance = openapi_client.DraftApi(api_client)

    try:
        # Get round-by-round data for current year's NHL Entry Draft.
        api_response = api_instance.get_draft()
        print("The response of DraftApi->get_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Draft**](Draft.md)

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

# **get_draft_by_year**
> Draft get_draft_by_year(year)

Get round-by-round data for a specific year's NHL Entry Draft.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.draft import Draft
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
    api_instance = openapi_client.DraftApi(api_client)
    year = 2018 # float | The draft year.

    try:
        # Get round-by-round data for a specific year's NHL Entry Draft.
        api_response = api_instance.get_draft_by_year(year)
        print("The response of DraftApi->get_draft_by_year:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_by_year: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**| The draft year. | 

### Return type

[**Draft**](Draft.md)

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

# **get_draft_prospect**
> DraftProspects get_draft_prospect(id)

Get an NHL Entry Draft prospect.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.draft_prospects import DraftProspects
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
    api_instance = openapi_client.DraftApi(api_client)
    id = 65242 # float | The prospect ID.

    try:
        # Get an NHL Entry Draft prospect.
        api_response = api_instance.get_draft_prospect(id)
        print("The response of DraftApi->get_draft_prospect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_prospect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The prospect ID. | 

### Return type

[**DraftProspects**](DraftProspects.md)

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

# **get_draft_prospects**
> DraftProspects get_draft_prospects()

Get all NHL Entry Draft prospects.

Be forewarned that this endpoint returns a **lot** of data and there does not appear to be a way to paginate results.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.draft_prospects import DraftProspects
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
    api_instance = openapi_client.DraftApi(api_client)

    try:
        # Get all NHL Entry Draft prospects.
        api_response = api_instance.get_draft_prospects()
        print("The response of DraftApi->get_draft_prospects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_prospects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DraftProspects**](DraftProspects.md)

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

