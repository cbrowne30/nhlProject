# openapi_client.StandingsApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_standing_types**](StandingsApi.md#get_standing_types) | **GET** /standingsTypes | Get all available NHL standing types.
[**get_standings**](StandingsApi.md#get_standings) | **GET** /standings | Get NHL division standings.
[**get_standings_by_type**](StandingsApi.md#get_standings_by_type) | **GET** /standings/{type} | Get NHL standings for a specific standing type.


# **get_standing_types**
> List[StandingTypesInner] get_standing_types()

Get all available NHL standing types.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.standing_types_inner import StandingTypesInner
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
    api_instance = openapi_client.StandingsApi(api_client)

    try:
        # Get all available NHL standing types.
        api_response = api_instance.get_standing_types()
        print("The response of StandingsApi->get_standing_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingsApi->get_standing_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StandingTypesInner]**](StandingTypesInner.md)

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

# **get_standings**
> Standings get_standings(season=season, var_date=var_date)

Get NHL division standings.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.standings import Standings
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
    api_instance = openapi_client.StandingsApi(api_client)
    season = '2013-10-20' # date | Standings for a specified season. (optional)
    var_date = 'Mon Jan 08 19:00:00 EST 2018' # date | Standings on a specified date. (optional)

    try:
        # Get NHL division standings.
        api_response = api_instance.get_standings(season=season, var_date=var_date)
        print("The response of StandingsApi->get_standings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingsApi->get_standings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **date**| Standings for a specified season. | [optional] 
 **var_date** | **date**| Standings on a specified date. | [optional] 

### Return type

[**Standings**](Standings.md)

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

# **get_standings_by_type**
> Standings get_standings_by_type(type)

Get NHL standings for a specific standing type.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.standings import Standings
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
    api_instance = openapi_client.StandingsApi(api_client)
    type = 'type_example' # str | Standing types:   * `byConference` - Standings by Conference   * `byDivision` - Standings by Division   * `byLeague` - Standings by League   * `divisionLeaders` - Division Leader standings   * `postseason` - Postseason Standings   * `preseason` - Preseason Standings   * `regularSeason` - Regular Season Standings   * `wildCard` - Wild card standings   * `wildCardWithLeaders` - Wild card standings with Division Leaders 

    try:
        # Get NHL standings for a specific standing type.
        api_response = api_instance.get_standings_by_type(type)
        print("The response of StandingsApi->get_standings_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StandingsApi->get_standings_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Standing types:   * &#x60;byConference&#x60; - Standings by Conference   * &#x60;byDivision&#x60; - Standings by Division   * &#x60;byLeague&#x60; - Standings by League   * &#x60;divisionLeaders&#x60; - Division Leader standings   * &#x60;postseason&#x60; - Postseason Standings   * &#x60;preseason&#x60; - Preseason Standings   * &#x60;regularSeason&#x60; - Regular Season Standings   * &#x60;wildCard&#x60; - Wild card standings   * &#x60;wildCardWithLeaders&#x60; - Wild card standings with Division Leaders  | 

### Return type

[**Standings**](Standings.md)

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

