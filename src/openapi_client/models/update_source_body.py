# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class UpdateSourceBody(object):
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
        'display_name': 'str',
        'paused_at': 'str',
        'properties': 'SourceFormProperties'
    }

    attribute_map = {
        'display_name': 'display_name',
        'paused_at': 'paused_at',
        'properties': 'properties'
    }

    def __init__(self, display_name=None, paused_at=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """UpdateSourceBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._paused_at = None
        self._properties = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if paused_at is not None:
            self.paused_at = paused_at
        if properties is not None:
            self.properties = properties

    @property
    def display_name(self):
        """Gets the display_name of this UpdateSourceBody.  # noqa: E501

        A descriptive name for the source. This will be used to dynamically generate the name corresponding to the schema name or dataset name that the data from this source will be loaded into.   # noqa: E501

        :return: The display_name of this UpdateSourceBody.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateSourceBody.

        A descriptive name for the source. This will be used to dynamically generate the name corresponding to the schema name or dataset name that the data from this source will be loaded into.   # noqa: E501

        :param display_name: The display_name of this UpdateSourceBody.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def paused_at(self):
        """Gets the paused_at of this UpdateSourceBody.  # noqa: E501

        The time the source was paused. This field must contain an ISO 8601-compliant date. Note: Providing any value - past, present, or future - for this property will pause the source immediately if the request is successful.   # noqa: E501

        :return: The paused_at of this UpdateSourceBody.  # noqa: E501
        :rtype: str
        """
        return self._paused_at

    @paused_at.setter
    def paused_at(self, paused_at):
        """Sets the paused_at of this UpdateSourceBody.

        The time the source was paused. This field must contain an ISO 8601-compliant date. Note: Providing any value - past, present, or future - for this property will pause the source immediately if the request is successful.   # noqa: E501

        :param paused_at: The paused_at of this UpdateSourceBody.  # noqa: E501
        :type: str
        """

        self._paused_at = paused_at

    @property
    def properties(self):
        """Gets the properties of this UpdateSourceBody.  # noqa: E501


        :return: The properties of this UpdateSourceBody.  # noqa: E501
        :rtype: SourceFormProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdateSourceBody.


        :param properties: The properties of this UpdateSourceBody.  # noqa: E501
        :type: SourceFormProperties
        """

        self._properties = properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, UpdateSourceBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSourceBody):
            return True

        return self.to_dict() != other.to_dict()
