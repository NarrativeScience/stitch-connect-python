# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from stitch_connect_client.configuration import Configuration


class StreamUpdate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "stream_id": "int",
        "selected": "bool",
        "stream_name": "str",
        "tap_stream_id": "str",
        "metadata": "list[StreamLevelMetadata]",
    }

    attribute_map = {
        "stream_id": "stream_id",
        "selected": "selected",
        "stream_name": "stream_name",
        "tap_stream_id": "tap_stream_id",
        "metadata": "metadata",
    }

    def __init__(
        self,
        stream_id=None,
        selected=None,
        stream_name=None,
        tap_stream_id=None,
        metadata=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """StreamUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stream_id = None
        self._selected = None
        self._stream_name = None
        self._tap_stream_id = None
        self._metadata = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if selected is not None:
            self.selected = selected
        if stream_name is not None:
            self.stream_name = stream_name
        if tap_stream_id is not None:
            self.tap_stream_id = tap_stream_id
        if metadata is not None:
            self.metadata = metadata

    @property
    def stream_id(self):
        """Gets the stream_id of this StreamUpdate.  # noqa: E501

        The stream ID.  # noqa: E501

        :return: The stream_id of this StreamUpdate.  # noqa: E501
        :rtype: int
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this StreamUpdate.

        The stream ID.  # noqa: E501

        :param stream_id: The stream_id of this StreamUpdate.  # noqa: E501
        :type: int
        """

        self._stream_id = stream_id

    @property
    def selected(self):
        """Gets the selected of this StreamUpdate.  # noqa: E501

        Indicates if the stream is selected for replication. Possible values are: null - Only present if a stream has never been selected. Otherwise, this value will be true if selected, and false if de-selected. true - The stream is selected and data will be replicated for all selected fields false - The stream is not selected and data for this stream will not be replicated   # noqa: E501

        :return: The selected of this StreamUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this StreamUpdate.

        Indicates if the stream is selected for replication. Possible values are: null - Only present if a stream has never been selected. Otherwise, this value will be true if selected, and false if de-selected. true - The stream is selected and data will be replicated for all selected fields false - The stream is not selected and data for this stream will not be replicated   # noqa: E501

        :param selected: The selected of this StreamUpdate.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def stream_name(self):
        """Gets the stream_name of this StreamUpdate.  # noqa: E501

        The name of the stream. This value may not be unique. For example: A database with multiple schemas can have the same stream name in multiple schemas.   # noqa: E501

        :return: The stream_name of this StreamUpdate.  # noqa: E501
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this StreamUpdate.

        The name of the stream. This value may not be unique. For example: A database with multiple schemas can have the same stream name in multiple schemas.   # noqa: E501

        :param stream_name: The stream_name of this StreamUpdate.  # noqa: E501
        :type: str
        """

        self._stream_name = stream_name

    @property
    def tap_stream_id(self):
        """Gets the tap_stream_id of this StreamUpdate.  # noqa: E501

        The unique version of the stream name. For database sources, this value will be the database name, schema name, and table name, combined.   # noqa: E501

        :return: The tap_stream_id of this StreamUpdate.  # noqa: E501
        :rtype: str
        """
        return self._tap_stream_id

    @tap_stream_id.setter
    def tap_stream_id(self, tap_stream_id):
        """Sets the tap_stream_id of this StreamUpdate.

        The unique version of the stream name. For database sources, this value will be the database name, schema name, and table name, combined.   # noqa: E501

        :param tap_stream_id: The tap_stream_id of this StreamUpdate.  # noqa: E501
        :type: str
        """

        self._tap_stream_id = tap_stream_id

    @property
    def metadata(self):
        """Gets the metadata of this StreamUpdate.  # noqa: E501


        :return: The metadata of this StreamUpdate.  # noqa: E501
        :rtype: list[StreamLevelMetadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this StreamUpdate.


        :param metadata: The metadata of this StreamUpdate.  # noqa: E501
        :type: list[StreamLevelMetadata]
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StreamUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StreamUpdate):
            return True

        return self.to_dict() != other.to_dict()
