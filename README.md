# stitch_connect_client

[![](https://img.shields.io/pypi/v/stitch_connect_client.svg)](https://pypi.org/pypi/stitch_connect_client/) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

https://www.stitchdata.com/docs/developers/stitch-connect/api

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.3
- Package version: 0.2.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

Table of Contents:

- [Installation](#installation)
- [Guide](#guide)
- [Documentation for API Endpoints](#documentation-for-api-endpoints)
- [Documentation for Models](#documentation-for-models)
- [Documentation for Authorization](#documentation-for-authorization)
- [Development](#development)

## Installation

This package requires Python 3.6 or above.

```bash
pip install stitch_connect_client
```

## Guide

```python
import stitch_connect_client
from stitch_connect_client.rest import ApiException


configuration = stitch_connect_client.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.stitchdata.com
configuration.host = "https://api.stitchdata.com"
# Create an instance of the API class
api_instance = stitch_connect_client.DestinationsApi(stitch_connect_client.ApiClient(configuration))
create_destination_body = stitch_connect_client.CreateDestinationBody() # CreateDestinationBody | Object containing type and properties of a destination

try:
    # Creates a new destination. Only a single destination is supported per Stitch client account.
    api_response = api_instance.create_destination(create_destination_body)
    print(api_response)
except ApiException as e:
    print(f"Exception when calling DestinationsApi->create_destination: {e}")

```

## Documentation for API Endpoints

All URIs are relative to *https://api.stitchdata.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DestinationsApi* | [**create_destination**](docs/DestinationsApi.md#create_destination) | **POST** /v4/destinations | Creates a new destination. Only a single destination is supported per Stitch client account.
*DestinationsApi* | [**delete_destination**](docs/DestinationsApi.md#delete_destination) | **DELETE** /v4/destinations/{destination_id} | Deletes an existing destination. Note: Stitch requires a destination to replicate data. Replication will be paused until a new destination is created and has a successful connection.
*DestinationsApi* | [**get_destination_types**](docs/DestinationsApi.md#get_destination_types) | **GET** /v4/destination-types | Retrieves general information about the configuration required for all supported destination types.
*DestinationsApi* | [**get_destinations**](docs/DestinationsApi.md#get_destinations) | **GET** /v4/destinations | Lists the destination currently in use for a Stitch account. Only a single data warehouse is supported per Stitch client account.
*DestinationsApi* | [**update_destination**](docs/DestinationsApi.md#update_destination) | **PUT** /v4/destinations/{destination_id} | Updates an existing destination. Modifications to the type attribute are not supported.
*SourcesApi* | [**create_source**](docs/SourcesApi.md#create_source) | **POST** /v4/sources | Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed.
*SourcesApi* | [**delete_source**](docs/SourcesApi.md#delete_source) | **DELETE** /v4/sources/{source_id} | Deletes an existing data source.
*SourcesApi* | [**get_last_connection_check**](docs/SourcesApi.md#get_last_connection_check) | **GET** /v4/sources/{source_id}/last-connection-check | Retrieves the last connection check for a source by the source’s unique identifier.
*SourcesApi* | [**get_source**](docs/SourcesApi.md#get_source) | **GET** /v4/sources/{source_id} | Retrieves a previously created data source by its unique identifier. This endpoint can be used to retrieve an active, paused, or deleted source.
*SourcesApi* | [**get_sources**](docs/SourcesApi.md#get_sources) | **GET** /v4/sources | Lists the sources for an account, including active, paused, and deleted sources.
*SourcesApi* | [**start_replication**](docs/SourcesApi.md#start_replication) | **POST** /v4/sources/{source_id}/sync | Manually starts a replication job for a source using the source’s unique identifier.
*SourcesApi* | [**update_source**](docs/SourcesApi.md#update_source) | **PUT** /v4/sources/{source_id} | Updates an existing data source.
*StreamsApi* | [**get_stream_schema**](docs/StreamsApi.md#get_stream_schema) | **GET** /v4/sources/{source_id}/streams/{stream_id} | Retrieves the schema for a source’s stream by the source and stream’s unique identifiers.
*StreamsApi* | [**get_streams**](docs/StreamsApi.md#get_streams) | **GET** /v4/sources/{source_id}/streams | Lists the available streams for a source.
*StreamsApi* | [**update_stream_metadata**](docs/StreamsApi.md#update_stream_metadata) | **PUT** /v4/sources/{source_id}/streams/metadata | Updates the metadata for streams and fields. This endpoint is used to define the metadata properties returned in the Stream Schema object’s non-discoverable-metadata-keys property.


## Documentation for Models

- [AzureDestinationFormProperties](docs/AzureDestinationFormProperties.md)
- [ConnectionCheck](docs/ConnectionCheck.md)
- [ConnectionDetails](docs/ConnectionDetails.md)
- [ConnectionStep](docs/ConnectionStep.md)
- [ConnectionStepProps](docs/ConnectionStepProps.md)
- [ConnectionStepPropsAnyOf](docs/ConnectionStepPropsAnyOf.md)
- [ConnectionStepPropsJsonSchema](docs/ConnectionStepPropsJsonSchema.md)
- [CreateDestinationBody](docs/CreateDestinationBody.md)
- [CreateSourceBody](docs/CreateSourceBody.md)
- [Destination](docs/Destination.md)
- [DestinationFormProperties](docs/DestinationFormProperties.md)
- [DestinationReportCard](docs/DestinationReportCard.md)
- [ErrorObject](docs/ErrorObject.md)
- [ErrorObjectError](docs/ErrorObjectError.md)
- [FieldLevelMetadata](docs/FieldLevelMetadata.md)
- [ForcedReplicationMethod](docs/ForcedReplicationMethod.md)
- [ForcedReplicationMethodObject](docs/ForcedReplicationMethodObject.md)
- [HookNotification](docs/HookNotification.md)
- [HookNotificationConfig](docs/HookNotificationConfig.md)
- [Metadata](docs/Metadata.md)
- [MetadataObject](docs/MetadataObject.md)
- [ReplicationJob](docs/ReplicationJob.md)
- [S3DestinationFormProperties](docs/S3DestinationFormProperties.md)
- [SalesforceSourceFormProperties](docs/SalesforceSourceFormProperties.md)
- [Source](docs/Source.md)
- [SourceFormProperties](docs/SourceFormProperties.md)
- [SourceReportCard](docs/SourceReportCard.md)
- [Stream](docs/Stream.md)
- [StreamLevelMetadata](docs/StreamLevelMetadata.md)
- [StreamSchema](docs/StreamSchema.md)
- [StreamUpdate](docs/StreamUpdate.md)
- [StreamsUpdateList](docs/StreamsUpdateList.md)
- [UpdateSourceBody](docs/UpdateSourceBody.md)


## Documentation for Authorization


#### bearerAuth

- **Type**: Bearer authentication


## Development

To develop `stitch_connect_client`, install dependencies and enable the pre-commit hook:

```bash
pip install pre-commit tox
pre-commit install
```

To run tests:

```bash
tox
```

To regenerate the client, run:

```bash
npx openapi-generator generate \
    -i https://raw.githubusercontent.com/NarrativeScience/stitch-connect-openapi/master/openapi.yml \
    -g python \
    -o . \
    --library asyncio \
    --package-name stitch_connect_client \
    --git-user-id NarrativeScience \
    --git-repo-id stitch-connect-python \
    -p packageVersion=0.2.1 \
    -t templates
```
