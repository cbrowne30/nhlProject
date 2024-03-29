# openapi_client.TeamsApi

All URIs are relative to *https://statsapi.web.nhl.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team**](TeamsApi.md#get_team) | **GET** /teams/{id} | Get an NHL team.
[**get_team_roster**](TeamsApi.md#get_team_roster) | **GET** /teams/{id}/roster | Get an NHL team&#39;s roster.
[**get_team_stats**](TeamsApi.md#get_team_stats) | **GET** /teams/{id}/stats | Get all statistics for an NHL team.
[**get_teams**](TeamsApi.md#get_teams) | **GET** /teams | Get all NHL teams.


# **get_team**
> Team get_team(id, expand=expand, season=season)

Get an NHL team.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.team import Team
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
    api_instance = openapi_client.TeamsApi(api_client)
    id = 28 # float | The ID of the team.
    expand = 'expand_example' # str | Expand your response for some additional data. (optional)
    season = 20172018 # float | Return a team's specific season. (optional)

    try:
        # Get an NHL team.
        api_response = api_instance.get_team(id, expand=expand, season=season)
        print("The response of TeamsApi->get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the team. | 
 **expand** | **str**| Expand your response for some additional data. | [optional] 
 **season** | **float**| Return a team&#39;s specific season. | [optional] 

### Return type

[**Team**](Team.md)

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

# **get_team_roster**
> Rosters get_team_roster(id, season=season)

Get an NHL team's roster.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.rosters import Rosters
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
    api_instance = openapi_client.TeamsApi(api_client)
    id = 28 # float | The ID of the team.
    season = 20172018 # float | Return a team's specific season. (optional)

    try:
        # Get an NHL team's roster.
        api_response = api_instance.get_team_roster(id, season=season)
        print("The response of TeamsApi->get_team_roster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_roster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the team. | 
 **season** | **float**| Return a team&#39;s specific season. | [optional] 

### Return type

[**Rosters**](Rosters.md)

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

# **get_team_stats**
> TeamStats get_team_stats(id)

Get all statistics for an NHL team.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.team_stats import TeamStats
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
    api_instance = openapi_client.TeamsApi(api_client)
    id = 28 # float | The ID of the team.

    try:
        # Get all statistics for an NHL team.
        api_response = api_instance.get_team_stats(id)
        print("The response of TeamsApi->get_team_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the team. | 

### Return type

[**TeamStats**](TeamStats.md)

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

# **get_teams**
> Teams get_teams(expand=expand, season=season)

Get all NHL teams.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.teams import Teams
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
    api_instance = openapi_client.TeamsApi(api_client)
    expand = 'expand_example' # str | Expand your response for some additional data. (optional)
    season = 20172018 # float | Return a team's specific season. (optional)

    try:
        # Get all NHL teams.
        api_response = api_instance.get_teams(expand=expand, season=season)
        print("The response of TeamsApi->get_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Expand your response for some additional data. | [optional] 
 **season** | **float**| Return a team&#39;s specific season. | [optional] 

### Return type

[**Teams**](Teams.md)

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

