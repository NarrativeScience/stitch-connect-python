# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from stitch_connect_client.api_client import ApiClient
from stitch_connect_client.exceptions import ApiTypeError, ApiValueError


class StreamsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_stream_schema(self, source_id, stream_id, **kwargs):  # noqa: E501
        """Retrieves the schema for a source’s stream by the source and stream’s unique identifiers.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stream_schema(source_id, stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str source_id: The ID of the source (required)
        :param str stream_id: The ID of the source (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: StreamSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_stream_schema_with_http_info(
            source_id, stream_id, **kwargs
        )  # noqa: E501

    def get_stream_schema_with_http_info(
        self, source_id, stream_id, **kwargs
    ):  # noqa: E501
        """Retrieves the schema for a source’s stream by the source and stream’s unique identifiers.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stream_schema_with_http_info(source_id, stream_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str source_id: The ID of the source (required)
        :param str stream_id: The ID of the source (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(StreamSchema, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["source_id", "stream_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stream_schema" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'source_id' is set
        if self.api_client.client_side_validation and (
            "source_id" not in local_var_params
            or local_var_params["source_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `source_id` when calling `get_stream_schema`"
            )  # noqa: E501
        # verify the required parameter 'stream_id' is set
        if self.api_client.client_side_validation and (
            "stream_id" not in local_var_params
            or local_var_params["stream_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stream_id` when calling `get_stream_schema`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "source_id" in local_var_params:
            path_params["source_id"] = local_var_params["source_id"]  # noqa: E501
        if "stream_id" in local_var_params:
            path_params["stream_id"] = local_var_params["stream_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/v4/sources/{source_id}/streams/{stream_id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="StreamSchema",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_streams(self, source_id, **kwargs):  # noqa: E501
        """Lists the available streams for a source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_streams(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str source_id: The ID of the source (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Stream]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_streams_with_http_info(source_id, **kwargs)  # noqa: E501

    def get_streams_with_http_info(self, source_id, **kwargs):  # noqa: E501
        """Lists the available streams for a source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_streams_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str source_id: The ID of the source (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Stream], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["source_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_streams" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'source_id' is set
        if self.api_client.client_side_validation and (
            "source_id" not in local_var_params
            or local_var_params["source_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `source_id` when calling `get_streams`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "source_id" in local_var_params:
            path_params["source_id"] = local_var_params["source_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/v4/sources/{source_id}/streams",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[Stream]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_stream_metadata(
        self, source_id, streams_update_list, **kwargs
    ):  # noqa: E501
        """Updates the metadata for streams and fields. This endpoint is used to define the metadata properties returned in the Stream Schema object’s non-discoverable-metadata-keys property.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_stream_metadata(source_id, streams_update_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str source_id: The ID of the source (required)
        :param StreamsUpdateList streams_update_list: Array of streams to update metadata for (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.update_stream_metadata_with_http_info(
            source_id, streams_update_list, **kwargs
        )  # noqa: E501

    def update_stream_metadata_with_http_info(
        self, source_id, streams_update_list, **kwargs
    ):  # noqa: E501
        """Updates the metadata for streams and fields. This endpoint is used to define the metadata properties returned in the Stream Schema object’s non-discoverable-metadata-keys property.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_stream_metadata_with_http_info(source_id, streams_update_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str source_id: The ID of the source (required)
        :param StreamsUpdateList streams_update_list: Array of streams to update metadata for (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["source_id", "streams_update_list"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_stream_metadata" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'source_id' is set
        if self.api_client.client_side_validation and (
            "source_id" not in local_var_params
            or local_var_params["source_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `source_id` when calling `update_stream_metadata`"
            )  # noqa: E501
        # verify the required parameter 'streams_update_list' is set
        if self.api_client.client_side_validation and (
            "streams_update_list" not in local_var_params
            or local_var_params["streams_update_list"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `streams_update_list` when calling `update_stream_metadata`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "source_id" in local_var_params:
            path_params["source_id"] = local_var_params["source_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "streams_update_list" in local_var_params:
            body_params = local_var_params["streams_update_list"]
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/v4/sources/{source_id}/streams/metadata",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
