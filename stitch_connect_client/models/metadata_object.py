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


class MetadataObject(object):
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
        "tap_google_analytics_all_cubes": "list[str]",
        "inclusion": "str",
        "selected_by_default": "bool",
        "sql_datatype": "str",
        "field_exclusions": "object",
        "unsupported_description": "str",
        "tap_google_analytics_cubes": "list[str]",
        "tap_google_analytics_group": "str",
        "behavior": "str",
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
        "tap_google_analytics_all_cubes": "tap_google_analytics.all_cubes",
        "inclusion": "inclusion",
        "selected_by_default": "selected-by-default",
        "sql_datatype": "sql-datatype",
        "field_exclusions": "fieldExclusions",
        "unsupported_description": "unsupported-description",
        "tap_google_analytics_cubes": "tap_google_analytics.cubes",
        "tap_google_analytics_group": "tap_google_analytics.group",
        "behavior": "behavior",
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
        tap_google_analytics_all_cubes=None,
        inclusion=None,
        selected_by_default=None,
        sql_datatype=None,
        field_exclusions=None,
        unsupported_description=None,
        tap_google_analytics_cubes=None,
        tap_google_analytics_group=None,
        behavior=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """MetadataObject - a model defined in OpenAPI"""  # noqa: E501
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
        self._tap_google_analytics_all_cubes = None
        self._inclusion = None
        self._selected_by_default = None
        self._sql_datatype = None
        self._field_exclusions = None
        self._unsupported_description = None
        self._tap_google_analytics_cubes = None
        self._tap_google_analytics_group = None
        self._behavior = None
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
        if tap_google_analytics_all_cubes is not None:
            self.tap_google_analytics_all_cubes = tap_google_analytics_all_cubes
        if inclusion is not None:
            self.inclusion = inclusion
        if selected_by_default is not None:
            self.selected_by_default = selected_by_default
        if sql_datatype is not None:
            self.sql_datatype = sql_datatype
        if field_exclusions is not None:
            self.field_exclusions = field_exclusions
        if unsupported_description is not None:
            self.unsupported_description = unsupported_description
        if tap_google_analytics_cubes is not None:
            self.tap_google_analytics_cubes = tap_google_analytics_cubes
        if tap_google_analytics_group is not None:
            self.tap_google_analytics_group = tap_google_analytics_group
        if behavior is not None:
            self.behavior = behavior

    @property
    def database_name(self):
        """Gets the database_name of this MetadataObject.  # noqa: E501

        For database sources only. The name of the database containing the stream.   # noqa: E501

        :return: The database_name of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this MetadataObject.

        For database sources only. The name of the database containing the stream.   # noqa: E501

        :param database_name: The database_name of this MetadataObject.  # noqa: E501
        :type: str
        """

        self._database_name = database_name

    @property
    def forced_replication_method(self):
        """Gets the forced_replication_method of this MetadataObject.  # noqa: E501


        :return: The forced_replication_method of this MetadataObject.  # noqa: E501
        :rtype: ForcedReplicationMethod
        """
        return self._forced_replication_method

    @forced_replication_method.setter
    def forced_replication_method(self, forced_replication_method):
        """Sets the forced_replication_method of this MetadataObject.


        :param forced_replication_method: The forced_replication_method of this MetadataObject.  # noqa: E501
        :type: ForcedReplicationMethod
        """

        self._forced_replication_method = forced_replication_method

    @property
    def is_view(self):
        """Gets the is_view of this MetadataObject.  # noqa: E501

        For database sources only. Indicates if the stream is a database view.   # noqa: E501

        :return: The is_view of this MetadataObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        """Sets the is_view of this MetadataObject.

        For database sources only. Indicates if the stream is a database view.   # noqa: E501

        :param is_view: The is_view of this MetadataObject.  # noqa: E501
        :type: bool
        """

        self._is_view = is_view

    @property
    def replication_key(self):
        """Gets the replication_key of this MetadataObject.  # noqa: E501

        Indicates the field being used as the stream’s Replication Key.   # noqa: E501

        :return: The replication_key of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._replication_key

    @replication_key.setter
    def replication_key(self, replication_key):
        """Sets the replication_key of this MetadataObject.

        Indicates the field being used as the stream’s Replication Key.   # noqa: E501

        :param replication_key: The replication_key of this MetadataObject.  # noqa: E501
        :type: str
        """

        self._replication_key = replication_key

    @property
    def replication_method(self):
        """Gets the replication_method of this MetadataObject.  # noqa: E501

        The Replication Method the stream uses to replicate data. Accepted values are: FULL_TABLE - The stream is using Full Table Replication INCREMENTAL - The stream is using Key-based Incremental Replication LOG_BASED - The stream is using Log-based Incremental Replication. Note: This method is only available for certain database sources, and requires additional setup to use.   # noqa: E501

        :return: The replication_method of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._replication_method

    @replication_method.setter
    def replication_method(self, replication_method):
        """Sets the replication_method of this MetadataObject.

        The Replication Method the stream uses to replicate data. Accepted values are: FULL_TABLE - The stream is using Full Table Replication INCREMENTAL - The stream is using Key-based Incremental Replication LOG_BASED - The stream is using Log-based Incremental Replication. Note: This method is only available for certain database sources, and requires additional setup to use.   # noqa: E501

        :param replication_method: The replication_method of this MetadataObject.  # noqa: E501
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
        """Gets the row_count of this MetadataObject.  # noqa: E501

        For database sources only. The number of rows (records) in the stream.   # noqa: E501

        :return: The row_count of this MetadataObject.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this MetadataObject.

        For database sources only. The number of rows (records) in the stream.   # noqa: E501

        :param row_count: The row_count of this MetadataObject.  # noqa: E501
        :type: int
        """

        self._row_count = row_count

    @property
    def schema_name(self):
        """Gets the schema_name of this MetadataObject.  # noqa: E501

        For database sources only. The name of the schema containing the stream.   # noqa: E501

        :return: The schema_name of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this MetadataObject.

        For database sources only. The name of the schema containing the stream.   # noqa: E501

        :param schema_name: The schema_name of this MetadataObject.  # noqa: E501
        :type: str
        """

        self._schema_name = schema_name

    @property
    def selected(self):
        """Gets the selected of this MetadataObject.  # noqa: E501

        Indicates whether a field should be included in a stream’s field selection list. This value will be present only if the stream containing the field is selected (selected: true). null - The value has not been set true - The field is selected false - The field is not selected   # noqa: E501

        :return: The selected of this MetadataObject.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this MetadataObject.

        Indicates whether a field should be included in a stream’s field selection list. This value will be present only if the stream containing the field is selected (selected: true). null - The value has not been set true - The field is selected false - The field is not selected   # noqa: E501

        :param selected: The selected of this MetadataObject.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def table_key_properties(self):
        """Gets the table_key_properties of this MetadataObject.  # noqa: E501

        An array of strings listing the fields that make up the key properties of the table. These are the table’s defined Primary Keys.   # noqa: E501

        :return: The table_key_properties of this MetadataObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._table_key_properties

    @table_key_properties.setter
    def table_key_properties(self, table_key_properties):
        """Sets the table_key_properties of this MetadataObject.

        An array of strings listing the fields that make up the key properties of the table. These are the table’s defined Primary Keys.   # noqa: E501

        :param table_key_properties: The table_key_properties of this MetadataObject.  # noqa: E501
        :type: list[str]
        """

        self._table_key_properties = table_key_properties

    @property
    def valid_replication_keys(self):
        """Gets the valid_replication_keys of this MetadataObject.  # noqa: E501

        An array of strings indicating the fields valid for use as Replication Keys in Key-based Incremental Replication (replication-method: INCREMENTAL). Note: For SaaS sources, the fields listed in this array are pre-defined by Stitch and will be used as the Replication Keys for the stream. They cannot be modified.   # noqa: E501

        :return: The valid_replication_keys of this MetadataObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._valid_replication_keys

    @valid_replication_keys.setter
    def valid_replication_keys(self, valid_replication_keys):
        """Sets the valid_replication_keys of this MetadataObject.

        An array of strings indicating the fields valid for use as Replication Keys in Key-based Incremental Replication (replication-method: INCREMENTAL). Note: For SaaS sources, the fields listed in this array are pre-defined by Stitch and will be used as the Replication Keys for the stream. They cannot be modified.   # noqa: E501

        :param valid_replication_keys: The valid_replication_keys of this MetadataObject.  # noqa: E501
        :type: list[str]
        """

        self._valid_replication_keys = valid_replication_keys

    @property
    def view_key_properties(self):
        """Gets the view_key_properties of this MetadataObject.  # noqa: E501

        For database sources only. An array of strings listing the fields that make up the key properties of the view.   # noqa: E501

        :return: The view_key_properties of this MetadataObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._view_key_properties

    @view_key_properties.setter
    def view_key_properties(self, view_key_properties):
        """Sets the view_key_properties of this MetadataObject.

        For database sources only. An array of strings listing the fields that make up the key properties of the view.   # noqa: E501

        :param view_key_properties: The view_key_properties of this MetadataObject.  # noqa: E501
        :type: list[str]
        """

        self._view_key_properties = view_key_properties

    @property
    def tap_google_analytics_all_cubes(self):
        """Gets the tap_google_analytics_all_cubes of this MetadataObject.  # noqa: E501

        For Google Analytics sources only. An array of strings listing all the ‘cubes’ available in the Google Analytics source. A cube is a group of metrics and dimensions that are compatible together.   # noqa: E501

        :return: The tap_google_analytics_all_cubes of this MetadataObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._tap_google_analytics_all_cubes

    @tap_google_analytics_all_cubes.setter
    def tap_google_analytics_all_cubes(self, tap_google_analytics_all_cubes):
        """Sets the tap_google_analytics_all_cubes of this MetadataObject.

        For Google Analytics sources only. An array of strings listing all the ‘cubes’ available in the Google Analytics source. A cube is a group of metrics and dimensions that are compatible together.   # noqa: E501

        :param tap_google_analytics_all_cubes: The tap_google_analytics_all_cubes of this MetadataObject.  # noqa: E501
        :type: list[str]
        """

        self._tap_google_analytics_all_cubes = tap_google_analytics_all_cubes

    @property
    def inclusion(self):
        """Gets the inclusion of this MetadataObject.  # noqa: E501

        Indicates when a field will be included. Possible values are: automatic - The field is included all the time, regardless of selected-by-default and selected values available - The field is available for selection. The field will be included if selected-by-default or selected is true. unsupported - The field is unsupported and will not be included, regardless of selected-by-default and selected values If a field is unsupported, the `unsupported-description` attribute may provide additonal information.   # noqa: E501

        :return: The inclusion of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._inclusion

    @inclusion.setter
    def inclusion(self, inclusion):
        """Sets the inclusion of this MetadataObject.

        Indicates when a field will be included. Possible values are: automatic - The field is included all the time, regardless of selected-by-default and selected values available - The field is available for selection. The field will be included if selected-by-default or selected is true. unsupported - The field is unsupported and will not be included, regardless of selected-by-default and selected values If a field is unsupported, the `unsupported-description` attribute may provide additonal information.   # noqa: E501

        :param inclusion: The inclusion of this MetadataObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["automatic", "available", "unsupported"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and inclusion not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `inclusion` ({0}), must be one of {1}".format(  # noqa: E501
                    inclusion, allowed_values
                )
            )

        self._inclusion = inclusion

    @property
    def selected_by_default(self):
        """Gets the selected_by_default of this MetadataObject.  # noqa: E501

        Indicates if a field will be selected by default. Possible values are: null - The value has not been set true - The field is selected by default and is included regardless of the `selected` value false - The field is not selected by default. The field will be included if the `selected value` is true.   # noqa: E501

        :return: The selected_by_default of this MetadataObject.  # noqa: E501
        :rtype: bool
        """
        return self._selected_by_default

    @selected_by_default.setter
    def selected_by_default(self, selected_by_default):
        """Sets the selected_by_default of this MetadataObject.

        Indicates if a field will be selected by default. Possible values are: null - The value has not been set true - The field is selected by default and is included regardless of the `selected` value false - The field is not selected by default. The field will be included if the `selected value` is true.   # noqa: E501

        :param selected_by_default: The selected_by_default of this MetadataObject.  # noqa: E501
        :type: bool
        """

        self._selected_by_default = selected_by_default

    @property
    def sql_datatype(self):
        """Gets the sql_datatype of this MetadataObject.  # noqa: E501

        For database sources only. The data type of a column from a database.   # noqa: E501

        :return: The sql_datatype of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._sql_datatype

    @sql_datatype.setter
    def sql_datatype(self, sql_datatype):
        """Sets the sql_datatype of this MetadataObject.

        For database sources only. The data type of a column from a database.   # noqa: E501

        :param sql_datatype: The sql_datatype of this MetadataObject.  # noqa: E501
        :type: str
        """

        self._sql_datatype = sql_datatype

    @property
    def field_exclusions(self):
        """Gets the field_exclusions of this MetadataObject.  # noqa: E501

        A list of arrays, each array containing an array of strings that correspond to fields that are incompatible when the current field is selected. For example: If the metadata for a DeviceOS field contains a fieldExclusion of [\"properties\":\"ImpressionLostToBidPercent\"], then the DeviceOS and ImpressionLostToBidPercent fields cannot be selected together in the stream.   # noqa: E501

        :return: The field_exclusions of this MetadataObject.  # noqa: E501
        :rtype: object
        """
        return self._field_exclusions

    @field_exclusions.setter
    def field_exclusions(self, field_exclusions):
        """Sets the field_exclusions of this MetadataObject.

        A list of arrays, each array containing an array of strings that correspond to fields that are incompatible when the current field is selected. For example: If the metadata for a DeviceOS field contains a fieldExclusion of [\"properties\":\"ImpressionLostToBidPercent\"], then the DeviceOS and ImpressionLostToBidPercent fields cannot be selected together in the stream.   # noqa: E501

        :param field_exclusions: The field_exclusions of this MetadataObject.  # noqa: E501
        :type: object
        """

        self._field_exclusions = field_exclusions

    @property
    def unsupported_description(self):
        """Gets the unsupported_description of this MetadataObject.  # noqa: E501

        The reason a field is unsupported (`inclusion`: unsupported). Note: This is not available for all sources.   # noqa: E501

        :return: The unsupported_description of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._unsupported_description

    @unsupported_description.setter
    def unsupported_description(self, unsupported_description):
        """Sets the unsupported_description of this MetadataObject.

        The reason a field is unsupported (`inclusion`: unsupported). Note: This is not available for all sources.   # noqa: E501

        :param unsupported_description: The unsupported_description of this MetadataObject.  # noqa: E501
        :type: str
        """

        self._unsupported_description = unsupported_description

    @property
    def tap_google_analytics_cubes(self):
        """Gets the tap_google_analytics_cubes of this MetadataObject.  # noqa: E501

        For Google Analytics sources only. An array of strings containing the ‘cubes’ the field is a part of. A cube is a group of metrics and dimensions that are compatible together.   # noqa: E501

        :return: The tap_google_analytics_cubes of this MetadataObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._tap_google_analytics_cubes

    @tap_google_analytics_cubes.setter
    def tap_google_analytics_cubes(self, tap_google_analytics_cubes):
        """Sets the tap_google_analytics_cubes of this MetadataObject.

        For Google Analytics sources only. An array of strings containing the ‘cubes’ the field is a part of. A cube is a group of metrics and dimensions that are compatible together.   # noqa: E501

        :param tap_google_analytics_cubes: The tap_google_analytics_cubes of this MetadataObject.  # noqa: E501
        :type: list[str]
        """

        self._tap_google_analytics_cubes = tap_google_analytics_cubes

    @property
    def tap_google_analytics_group(self):
        """Gets the tap_google_analytics_group of this MetadataObject.  # noqa: E501

        For Google Analytics sources only. The group the field belongs to. Possible values are: - Ad Exchange - Adsense - Adwords - App Tracking - Audience - Channel Grouping - Content Experiments - Content Grouping - Custom Variables or Columns - DoubleClick Bid Manager - DoubleClick Campaign Manager - DoubleClick Search - DoubleClick for Publishers - DoubleClick for Publishers Backfill - Ecommerce - Event Tracking - Exceptions - Geo Network - Goal Conversions - Internal Search - Lifetime Value and Cohorts - Page Tracking - Platform or Device - Publisher - Report Fields - Session - Site Speed - Social Activities - Social Interactions - System - Time - Traffic Sources - User - User Timings   # noqa: E501

        :return: The tap_google_analytics_group of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._tap_google_analytics_group

    @tap_google_analytics_group.setter
    def tap_google_analytics_group(self, tap_google_analytics_group):
        """Sets the tap_google_analytics_group of this MetadataObject.

        For Google Analytics sources only. The group the field belongs to. Possible values are: - Ad Exchange - Adsense - Adwords - App Tracking - Audience - Channel Grouping - Content Experiments - Content Grouping - Custom Variables or Columns - DoubleClick Bid Manager - DoubleClick Campaign Manager - DoubleClick Search - DoubleClick for Publishers - DoubleClick for Publishers Backfill - Ecommerce - Event Tracking - Exceptions - Geo Network - Goal Conversions - Internal Search - Lifetime Value and Cohorts - Page Tracking - Platform or Device - Publisher - Report Fields - Session - Site Speed - Social Activities - Social Interactions - System - Time - Traffic Sources - User - User Timings   # noqa: E501

        :param tap_google_analytics_group: The tap_google_analytics_group of this MetadataObject.  # noqa: E501
        :type: str
        """

        self._tap_google_analytics_group = tap_google_analytics_group

    @property
    def behavior(self):
        """Gets the behavior of this MetadataObject.  # noqa: E501

        For Google Analytics and Google Ads sources only. The type of field. Possible values are: - ATTRIBUTE - Goolgle Ads sources only - METRIC - DIMENSION - Google Analytics sources only - SEGMENT - Goolgle Ads sources only Note: This property won’t be present for Google Analytics fields where tap_google_analytics.group: Report Fields.   # noqa: E501

        :return: The behavior of this MetadataObject.  # noqa: E501
        :rtype: str
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """Sets the behavior of this MetadataObject.

        For Google Analytics and Google Ads sources only. The type of field. Possible values are: - ATTRIBUTE - Goolgle Ads sources only - METRIC - DIMENSION - Google Analytics sources only - SEGMENT - Goolgle Ads sources only Note: This property won’t be present for Google Analytics fields where tap_google_analytics.group: Report Fields.   # noqa: E501

        :param behavior: The behavior of this MetadataObject.  # noqa: E501
        :type: str
        """

        self._behavior = behavior

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
        if not isinstance(other, MetadataObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetadataObject):
            return True

        return self.to_dict() != other.to_dict()
