# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from stitch_connect_client.configuration import Configuration


class StreamLevelMetadata(object):
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
        "database_name": "str",
        "forced_replication_method": "ForcedReplicationMethod",
        "is_view": "bool",
        "replication_key": "str",
        "replication_method": "str",
        "row_count": "int",
        "schema_name": "str",
        "selected": "bool",
        "table_key_properties": "list[str]",
        "valid_replication_keys": "list[str]",
        "view_key_properties": "list[str]",
    }

    attribute_map = {
        "database_name": "database-name",
        "forced_replication_method": "forced-replication-method",
        "is_view": "is-view",
        "replication_key": "replication-key",
        "replication_method": "replication-method",
        "row_count": "row-count",
        "schema_name": "schema-name",
        "selected": "selected",
        "table_key_properties": "table-key-properties",
        "valid_replication_keys": "valid-replication-keys",
        "view_key_properties": "view-key-properties",
    }

    def __init__(
        self,
        database_name=None,
        forced_replication_method=None,
        is_view=None,
        replication_key=None,
        replication_method=None,
        row_count=None,
        schema_name=None,
        selected=None,
        table_key_properties=None,
        valid_replication_keys=None,
        view_key_properties=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """StreamLevelMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._database_name = None
        self._forced_replication_method = None
        self._is_view = None
        self._replication_key = None
        self._replication_method = None
        self._row_count = None
        self._schema_name = None
        self._selected = None
        self._table_key_properties = None
        self._valid_replication_keys = None
        self._view_key_properties = None
        self.discriminator = None

        if database_name is not None:
            self.database_name = database_name
        if forced_replication_method is not None:
            self.forced_replication_method = forced_replication_method
        if is_view is not None:
            self.is_view = is_view
        if replication_key is not None:
            self.replication_key = replication_key
        if replication_method is not None:
            self.replication_method = replication_method
        if row_count is not None:
            self.row_count = row_count
        if schema_name is not None:
            self.schema_name = schema_name
        if selected is not None:
            self.selected = selected
        if table_key_properties is not None:
            self.table_key_properties = table_key_properties
        if valid_replication_keys is not None:
            self.valid_replication_keys = valid_replication_keys
        if view_key_properties is not None:
            self.view_key_properties = view_key_properties

    @property
    def database_name(self):
        """Gets the database_name of this StreamLevelMetadata.  # noqa: E501

        For database sources only. The name of the database containing the stream.   # noqa: E501

        :return: The database_name of this StreamLevelMetadata.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this StreamLevelMetadata.

        For database sources only. The name of the database containing the stream.   # noqa: E501

        :param database_name: The database_name of this StreamLevelMetadata.  # noqa: E501
        :type: str
        """

        self._database_name = database_name

    @property
    def forced_replication_method(self):
        """Gets the forced_replication_method of this StreamLevelMetadata.  # noqa: E501


        :return: The forced_replication_method of this StreamLevelMetadata.  # noqa: E501
        :rtype: ForcedReplicationMethod
        """
        return self._forced_replication_method

    @forced_replication_method.setter
    def forced_replication_method(self, forced_replication_method):
        """Sets the forced_replication_method of this StreamLevelMetadata.


        :param forced_replication_method: The forced_replication_method of this StreamLevelMetadata.  # noqa: E501
        :type: ForcedReplicationMethod
        """

        self._forced_replication_method = forced_replication_method

    @property
    def is_view(self):
        """Gets the is_view of this StreamLevelMetadata.  # noqa: E501

        For database sources only. Indicates if the stream is a database view.   # noqa: E501

        :return: The is_view of this StreamLevelMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        """Sets the is_view of this StreamLevelMetadata.

        For database sources only. Indicates if the stream is a database view.   # noqa: E501

        :param is_view: The is_view of this StreamLevelMetadata.  # noqa: E501
        :type: bool
        """

        self._is_view = is_view

    @property
    def replication_key(self):
        """Gets the replication_key of this StreamLevelMetadata.  # noqa: E501

        Indicates the field being used as the stream’s Replication Key.   # noqa: E501

        :return: The replication_key of this StreamLevelMetadata.  # noqa: E501
        :rtype: str
        """
        return self._replication_key

    @replication_key.setter
    def replication_key(self, replication_key):
        """Sets the replication_key of this StreamLevelMetadata.

        Indicates the field being used as the stream’s Replication Key.   # noqa: E501

        :param replication_key: The replication_key of this StreamLevelMetadata.  # noqa: E501
        :type: str
        """

        self._replication_key = replication_key

    @property
    def replication_method(self):
        """Gets the replication_method of this StreamLevelMetadata.  # noqa: E501

        The Replication Method the stream uses to replicate data. Accepted values are: FULL_TABLE - The stream is using Full Table Replication INCREMENTAL - The stream is using Key-based Incremental Replication LOG_BASED - The stream is using Log-based Incremental Replication. Note: This method is only available for certain database sources, and requires additional setup to use.   # noqa: E501

        :return: The replication_method of this StreamLevelMetadata.  # noqa: E501
        :rtype: str
        """
        return self._replication_method

    @replication_method.setter
    def replication_method(self, replication_method):
        """Sets the replication_method of this StreamLevelMetadata.

        The Replication Method the stream uses to replicate data. Accepted values are: FULL_TABLE - The stream is using Full Table Replication INCREMENTAL - The stream is using Key-based Incremental Replication LOG_BASED - The stream is using Log-based Incremental Replication. Note: This method is only available for certain database sources, and requires additional setup to use.   # noqa: E501

        :param replication_method: The replication_method of this StreamLevelMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["FULL_TABLE", "INCREMENTAL", "LOG_BASED"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and replication_method not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `replication_method` ({0}), must be one of {1}".format(  # noqa: E501
                    replication_method, allowed_values
                )
            )

        self._replication_method = replication_method

    @property
    def row_count(self):
        """Gets the row_count of this StreamLevelMetadata.  # noqa: E501

        For database sources only. The number of rows (records) in the stream.   # noqa: E501

        :return: The row_count of this StreamLevelMetadata.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this StreamLevelMetadata.

        For database sources only. The number of rows (records) in the stream.   # noqa: E501

        :param row_count: The row_count of this StreamLevelMetadata.  # noqa: E501
        :type: int
        """

        self._row_count = row_count

    @property
    def schema_name(self):
        """Gets the schema_name of this StreamLevelMetadata.  # noqa: E501

        For database sources only. The name of the schema containing the stream.   # noqa: E501

        :return: The schema_name of this StreamLevelMetadata.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this StreamLevelMetadata.

        For database sources only. The name of the schema containing the stream.   # noqa: E501

        :param schema_name: The schema_name of this StreamLevelMetadata.  # noqa: E501
        :type: str
        """

        self._schema_name = schema_name

    @property
    def selected(self):
        """Gets the selected of this StreamLevelMetadata.  # noqa: E501

        Indicates whether a stream should be set to replicate. Accepted values are: true - The stream is selected and data for selected fields will be replicated false - The stream is not selected and no data will be replicated   # noqa: E501

        :return: The selected of this StreamLevelMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this StreamLevelMetadata.

        Indicates whether a stream should be set to replicate. Accepted values are: true - The stream is selected and data for selected fields will be replicated false - The stream is not selected and no data will be replicated   # noqa: E501

        :param selected: The selected of this StreamLevelMetadata.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def table_key_properties(self):
        """Gets the table_key_properties of this StreamLevelMetadata.  # noqa: E501

        An array of strings listing the fields that make up the key properties of the table. These are the table’s defined Primary Keys.   # noqa: E501

        :return: The table_key_properties of this StreamLevelMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._table_key_properties

    @table_key_properties.setter
    def table_key_properties(self, table_key_properties):
        """Sets the table_key_properties of this StreamLevelMetadata.

        An array of strings listing the fields that make up the key properties of the table. These are the table’s defined Primary Keys.   # noqa: E501

        :param table_key_properties: The table_key_properties of this StreamLevelMetadata.  # noqa: E501
        :type: list[str]
        """

        self._table_key_properties = table_key_properties

    @property
    def valid_replication_keys(self):
        """Gets the valid_replication_keys of this StreamLevelMetadata.  # noqa: E501

        An array of strings indicating the fields valid for use as Replication Keys in Key-based Incremental Replication (replication-method: INCREMENTAL). Note: For SaaS sources, the fields listed in this array are pre-defined by Stitch and will be used as the Replication Keys for the stream. They cannot be modified.   # noqa: E501

        :return: The valid_replication_keys of this StreamLevelMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._valid_replication_keys

    @valid_replication_keys.setter
    def valid_replication_keys(self, valid_replication_keys):
        """Sets the valid_replication_keys of this StreamLevelMetadata.

        An array of strings indicating the fields valid for use as Replication Keys in Key-based Incremental Replication (replication-method: INCREMENTAL). Note: For SaaS sources, the fields listed in this array are pre-defined by Stitch and will be used as the Replication Keys for the stream. They cannot be modified.   # noqa: E501

        :param valid_replication_keys: The valid_replication_keys of this StreamLevelMetadata.  # noqa: E501
        :type: list[str]
        """

        self._valid_replication_keys = valid_replication_keys

    @property
    def view_key_properties(self):
        """Gets the view_key_properties of this StreamLevelMetadata.  # noqa: E501

        For database sources only. An array of strings listing the fields that make up the key properties of the view.   # noqa: E501

        :return: The view_key_properties of this StreamLevelMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._view_key_properties

    @view_key_properties.setter
    def view_key_properties(self, view_key_properties):
        """Sets the view_key_properties of this StreamLevelMetadata.

        For database sources only. An array of strings listing the fields that make up the key properties of the view.   # noqa: E501

        :param view_key_properties: The view_key_properties of this StreamLevelMetadata.  # noqa: E501
        :type: list[str]
        """

        self._view_key_properties = view_key_properties

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
        if not isinstance(other, StreamLevelMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StreamLevelMetadata):
            return True

        return self.to_dict() != other.to_dict()
