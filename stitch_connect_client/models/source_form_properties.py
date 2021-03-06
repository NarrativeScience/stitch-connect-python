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


class SourceFormProperties(object):
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
        "anchor_time": "str",
        "api_type": "str",
        "client_id": "str",
        "client_secret": "str",
        "cron_expression": "str",
        "frequency_in_minutes": "str",
        "instance_url": "str",
        "is_sandbox": "str",
        "quota_percent_per_run": "str",
        "quota_percent_total": "str",
        "refresh_token": "str",
        "select_fields_by_default": "str",
        "start_date": "str",
        "quota_user": "str",
        "report_definitions": "list[GoogleAnalyticsSourceFormPropertiesReportDefinitions]",
        "api_secret": "str",
        "attribution_window": "str",
        "date_window_size": "str",
        "project_timezone": "str",
        "select_properties_by_default": "str",
    }

    attribute_map = {
        "anchor_time": "anchor_time",
        "api_type": "api_type",
        "client_id": "client_id",
        "client_secret": "client_secret",
        "cron_expression": "cron_expression",
        "frequency_in_minutes": "frequency_in_minutes",
        "instance_url": "instance_url",
        "is_sandbox": "is_sandbox",
        "quota_percent_per_run": "quota_percent_per_run",
        "quota_percent_total": "quota_percent_total",
        "refresh_token": "refresh_token",
        "select_fields_by_default": "select_fields_by_default",
        "start_date": "start_date",
        "quota_user": "quota_user",
        "report_definitions": "report_definitions",
        "api_secret": "api_secret",
        "attribution_window": "attribution_window",
        "date_window_size": "date_window_size",
        "project_timezone": "project_timezone",
        "select_properties_by_default": "select_properties_by_default",
    }

    def __init__(
        self,
        anchor_time=None,
        api_type=None,
        client_id=None,
        client_secret=None,
        cron_expression=None,
        frequency_in_minutes=None,
        instance_url=None,
        is_sandbox=None,
        quota_percent_per_run=None,
        quota_percent_total=None,
        refresh_token=None,
        select_fields_by_default=None,
        start_date=None,
        quota_user=None,
        report_definitions=None,
        api_secret=None,
        attribution_window=None,
        date_window_size=None,
        project_timezone=None,
        select_properties_by_default=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SourceFormProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._anchor_time = None
        self._api_type = None
        self._client_id = None
        self._client_secret = None
        self._cron_expression = None
        self._frequency_in_minutes = None
        self._instance_url = None
        self._is_sandbox = None
        self._quota_percent_per_run = None
        self._quota_percent_total = None
        self._refresh_token = None
        self._select_fields_by_default = None
        self._start_date = None
        self._quota_user = None
        self._report_definitions = None
        self._api_secret = None
        self._attribution_window = None
        self._date_window_size = None
        self._project_timezone = None
        self._select_properties_by_default = None
        self.discriminator = None

        if anchor_time is not None:
            self.anchor_time = anchor_time
        if api_type is not None:
            self.api_type = api_type
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if cron_expression is not None:
            self.cron_expression = cron_expression
        if frequency_in_minutes is not None:
            self.frequency_in_minutes = frequency_in_minutes
        if instance_url is not None:
            self.instance_url = instance_url
        if is_sandbox is not None:
            self.is_sandbox = is_sandbox
        if quota_percent_per_run is not None:
            self.quota_percent_per_run = quota_percent_per_run
        if quota_percent_total is not None:
            self.quota_percent_total = quota_percent_total
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if select_fields_by_default is not None:
            self.select_fields_by_default = select_fields_by_default
        if start_date is not None:
            self.start_date = start_date
        if quota_user is not None:
            self.quota_user = quota_user
        if report_definitions is not None:
            self.report_definitions = report_definitions
        if api_secret is not None:
            self.api_secret = api_secret
        if attribution_window is not None:
            self.attribution_window = attribution_window
        if date_window_size is not None:
            self.date_window_size = date_window_size
        if project_timezone is not None:
            self.project_timezone = project_timezone
        if select_properties_by_default is not None:
            self.select_properties_by_default = select_properties_by_default

    @property
    def anchor_time(self):
        """Gets the anchor_time of this SourceFormProperties.  # noqa: E501

        Defines the time that frequency_in_minutes is \"anchored\" to, which Stitch will use to create the integration's replication schedule. In Stitch, this is referred to as Anchor Scheduling. This field must contain an ISO 8601-compliant date. Note: When Stitch stores this value, it will be in UTC. You should provide this value in UTC to ensure the desired anchor time is retained. For example: You want to create a schedule that is anchored to 1:00PM EST and runs every 6 hours (360 minutes). To do this, you can set anchor_time to something like 2018-04-30T17:00:00Z and frequency_in_minutes to 360. This means jobs would run at 23:00:00, 05:00:00, 11:00:00, and so on.   # noqa: E501

        :return: The anchor_time of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._anchor_time

    @anchor_time.setter
    def anchor_time(self, anchor_time):
        """Sets the anchor_time of this SourceFormProperties.

        Defines the time that frequency_in_minutes is \"anchored\" to, which Stitch will use to create the integration's replication schedule. In Stitch, this is referred to as Anchor Scheduling. This field must contain an ISO 8601-compliant date. Note: When Stitch stores this value, it will be in UTC. You should provide this value in UTC to ensure the desired anchor time is retained. For example: You want to create a schedule that is anchored to 1:00PM EST and runs every 6 hours (360 minutes). To do this, you can set anchor_time to something like 2018-04-30T17:00:00Z and frequency_in_minutes to 360. This means jobs would run at 23:00:00, 05:00:00, 11:00:00, and so on.   # noqa: E501

        :param anchor_time: The anchor_time of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._anchor_time = anchor_time

    @property
    def api_type(self):
        """Gets the api_type of this SourceFormProperties.  # noqa: E501

        The Salesforce API Stitch should use to extract data. Possible values are REST or BULK.   # noqa: E501

        :return: The api_type of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this SourceFormProperties.

        The Salesforce API Stitch should use to extract data. Possible values are REST or BULK.   # noqa: E501

        :param api_type: The api_type of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._api_type = api_type

    @property
    def client_id(self):
        """Gets the client_id of this SourceFormProperties.  # noqa: E501

        The secure OAuth 2.0 identifier for the client application.   # noqa: E501

        :return: The client_id of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SourceFormProperties.

        The secure OAuth 2.0 identifier for the client application.   # noqa: E501

        :param client_id: The client_id of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this SourceFormProperties.  # noqa: E501

        The secure OAuth 2.0 secret key for the client application.   # noqa: E501

        :return: The client_secret of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this SourceFormProperties.

        The secure OAuth 2.0 secret key for the client application.   # noqa: E501

        :param client_secret: The client_secret of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def cron_expression(self):
        """Gets the cron_expression of this SourceFormProperties.  # noqa: E501

        Note: Advanced Scheduling using Cron is not yet supported for this source. A value may be submitted for this property if the account is on an Enterprise plan, but Stitch will not use the expression submitted. A valid Quartz cron expression representing the replication schedule for the integration. Refer to the Advanced Scheduling documentation for more info. Note: If neither a cron_expression or frequency_in_minutes property is provided, Stitch will use the source's default frequency_in_minutes value (60).   # noqa: E501

        :return: The cron_expression of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this SourceFormProperties.

        Note: Advanced Scheduling using Cron is not yet supported for this source. A value may be submitted for this property if the account is on an Enterprise plan, but Stitch will not use the expression submitted. A valid Quartz cron expression representing the replication schedule for the integration. Refer to the Advanced Scheduling documentation for more info. Note: If neither a cron_expression or frequency_in_minutes property is provided, Stitch will use the source's default frequency_in_minutes value (60).   # noqa: E501

        :param cron_expression: The cron_expression of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._cron_expression = cron_expression

    @property
    def frequency_in_minutes(self):
        """Gets the frequency_in_minutes of this SourceFormProperties.  # noqa: E501

        Defines how often, in minutes, Stitch should attempt to replicate data from Google Analytics. Accepted values are: - 30 - 60 - 360 - 720 - 1440   # noqa: E501

        :return: The frequency_in_minutes of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._frequency_in_minutes

    @frequency_in_minutes.setter
    def frequency_in_minutes(self, frequency_in_minutes):
        """Sets the frequency_in_minutes of this SourceFormProperties.

        Defines how often, in minutes, Stitch should attempt to replicate data from Google Analytics. Accepted values are: - 30 - 60 - 360 - 720 - 1440   # noqa: E501

        :param frequency_in_minutes: The frequency_in_minutes of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._frequency_in_minutes = frequency_in_minutes

    @property
    def instance_url(self):
        """Gets the instance_url of this SourceFormProperties.  # noqa: E501

        The url of the instance to connect to.  # noqa: E501

        :return: The instance_url of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        """Sets the instance_url of this SourceFormProperties.

        The url of the instance to connect to.  # noqa: E501

        :param instance_url: The instance_url of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._instance_url = instance_url

    @property
    def is_sandbox(self):
        """Gets the is_sandbox of this SourceFormProperties.  # noqa: E501

        If `true`, the Salesforce account being connected is a sandbox.  # noqa: E501

        :return: The is_sandbox of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._is_sandbox

    @is_sandbox.setter
    def is_sandbox(self, is_sandbox):
        """Sets the is_sandbox of this SourceFormProperties.

        If `true`, the Salesforce account being connected is a sandbox.  # noqa: E501

        :param is_sandbox: The is_sandbox of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._is_sandbox = is_sandbox

    @property
    def quota_percent_per_run(self):
        """Gets the quota_percent_per_run of this SourceFormProperties.  # noqa: E501

        The maximum percentage of Salesforce API quota allowed per replication job.   # noqa: E501

        :return: The quota_percent_per_run of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._quota_percent_per_run

    @quota_percent_per_run.setter
    def quota_percent_per_run(self, quota_percent_per_run):
        """Sets the quota_percent_per_run of this SourceFormProperties.

        The maximum percentage of Salesforce API quota allowed per replication job.   # noqa: E501

        :param quota_percent_per_run: The quota_percent_per_run of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._quota_percent_per_run = quota_percent_per_run

    @property
    def quota_percent_total(self):
        """Gets the quota_percent_total of this SourceFormProperties.  # noqa: E501

        The maximum percentage of Salesforce API quota allowed per day.   # noqa: E501

        :return: The quota_percent_total of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._quota_percent_total

    @quota_percent_total.setter
    def quota_percent_total(self, quota_percent_total):
        """Sets the quota_percent_total of this SourceFormProperties.

        The maximum percentage of Salesforce API quota allowed per day.   # noqa: E501

        :param quota_percent_total: The quota_percent_total of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._quota_percent_total = quota_percent_total

    @property
    def refresh_token(self):
        """Gets the refresh_token of this SourceFormProperties.  # noqa: E501

        The OAuth 2.0 refresh token used to access the Google API.  # noqa: E501

        :return: The refresh_token of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this SourceFormProperties.

        The OAuth 2.0 refresh token used to access the Google API.  # noqa: E501

        :param refresh_token: The refresh_token of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def select_fields_by_default(self):
        """Gets the select_fields_by_default of this SourceFormProperties.  # noqa: E501

        If `true`, Stitch will automatically set new fields added in Salesforce to replicate.   # noqa: E501

        :return: The select_fields_by_default of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._select_fields_by_default

    @select_fields_by_default.setter
    def select_fields_by_default(self, select_fields_by_default):
        """Sets the select_fields_by_default of this SourceFormProperties.

        If `true`, Stitch will automatically set new fields added in Salesforce to replicate.   # noqa: E501

        :param select_fields_by_default: The select_fields_by_default of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._select_fields_by_default = select_fields_by_default

    @property
    def start_date(self):
        """Gets the start_date of this SourceFormProperties.  # noqa: E501

        The date from which Stitch should begin replicating data from Salesforce. Data from this date forward will be replicated. This field must contain an ISO 8601-compliant date, and the timestamp must be midnight. For example: 2018-01-01T00:00:00Z   # noqa: E501

        :return: The start_date of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SourceFormProperties.

        The date from which Stitch should begin replicating data from Salesforce. Data from this date forward will be replicated. This field must contain an ISO 8601-compliant date, and the timestamp must be midnight. For example: 2018-01-01T00:00:00Z   # noqa: E501

        :param start_date: The start_date of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def quota_user(self):
        """Gets the quota_user of this SourceFormProperties.  # noqa: E501

        Note: This is a read-only property and will be returned when the Google Analytics object is successfully created. Including it in POST or PUT requests will result in InvalidProperties errors.   # noqa: E501

        :return: The quota_user of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._quota_user

    @quota_user.setter
    def quota_user(self, quota_user):
        """Sets the quota_user of this SourceFormProperties.

        Note: This is a read-only property and will be returned when the Google Analytics object is successfully created. Including it in POST or PUT requests will result in InvalidProperties errors.   # noqa: E501

        :param quota_user: The quota_user of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._quota_user = quota_user

    @property
    def report_definitions(self):
        """Gets the report_definitions of this SourceFormProperties.  # noqa: E501

        An array of objects, each object pertaining to a custom report you want to create. Note: Metrics and dimensions for each report can be selected when the source proceeds to the field_selection step.   # noqa: E501

        :return: The report_definitions of this SourceFormProperties.  # noqa: E501
        :rtype: list[GoogleAnalyticsSourceFormPropertiesReportDefinitions]
        """
        return self._report_definitions

    @report_definitions.setter
    def report_definitions(self, report_definitions):
        """Sets the report_definitions of this SourceFormProperties.

        An array of objects, each object pertaining to a custom report you want to create. Note: Metrics and dimensions for each report can be selected when the source proceeds to the field_selection step.   # noqa: E501

        :param report_definitions: The report_definitions of this SourceFormProperties.  # noqa: E501
        :type: list[GoogleAnalyticsSourceFormPropertiesReportDefinitions]
        """

        self._report_definitions = report_definitions

    @property
    def api_secret(self):
        """Gets the api_secret of this SourceFormProperties.  # noqa: E501

        The API secret of your project in your Mixpanel account. Refer to the Mixpanel documentation for instructions on obtaining this information.   # noqa: E501

        :return: The api_secret of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this SourceFormProperties.

        The API secret of your project in your Mixpanel account. Refer to the Mixpanel documentation for instructions on obtaining this information.   # noqa: E501

        :param api_secret: The api_secret of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._api_secret = api_secret

    @property
    def attribution_window(self):
        """Gets the attribution_window of this SourceFormProperties.  # noqa: E501

        Defines the number, in days, Stitch should use as an attribution window. To ensure your Mixpanel and Stitch settings align, we recommend using the same attribution window in Stitch that you use in Mixpanel. Mixpanel's default attribution window is five days (5). Refer to the Mixpanel documentation for more information about attribution windows for this integration.   # noqa: E501

        :return: The attribution_window of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._attribution_window

    @attribution_window.setter
    def attribution_window(self, attribution_window):
        """Sets the attribution_window of this SourceFormProperties.

        Defines the number, in days, Stitch should use as an attribution window. To ensure your Mixpanel and Stitch settings align, we recommend using the same attribution window in Stitch that you use in Mixpanel. Mixpanel's default attribution window is five days (5). Refer to the Mixpanel documentation for more information about attribution windows for this integration.   # noqa: E501

        :param attribution_window: The attribution_window of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._attribution_window = attribution_window

    @property
    def date_window_size(self):
        """Gets the date_window_size of this SourceFormProperties.  # noqa: E501

        Defines the number, in days, for a date looping window for the export, funnel, and revenue tables. Date looping will return records whose from_date and to_date fall between the number of days in the defined window size. Note: If your project has large volumes of events, you may want to set the number of days to 14, 7, or even to 1 or 2 days.   # noqa: E501

        :return: The date_window_size of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._date_window_size

    @date_window_size.setter
    def date_window_size(self, date_window_size):
        """Sets the date_window_size of this SourceFormProperties.

        Defines the number, in days, for a date looping window for the export, funnel, and revenue tables. Date looping will return records whose from_date and to_date fall between the number of days in the defined window size. Note: If your project has large volumes of events, you may want to set the number of days to 14, 7, or even to 1 or 2 days.   # noqa: E501

        :param date_window_size: The date_window_size of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._date_window_size = date_window_size

    @property
    def project_timezone(self):
        """Gets the project_timezone of this SourceFormProperties.  # noqa: E501

        The timezone in which your date-time fields are stored for your project. You can find your project timezone in the project settings in the Mixpanel console   # noqa: E501

        :return: The project_timezone of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._project_timezone

    @project_timezone.setter
    def project_timezone(self, project_timezone):
        """Sets the project_timezone of this SourceFormProperties.

        The timezone in which your date-time fields are stored for your project. You can find your project timezone in the project settings in the Mixpanel console   # noqa: E501

        :param project_timezone: The project_timezone of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._project_timezone = project_timezone

    @property
    def select_properties_by_default(self):
        """Gets the select_properties_by_default of this SourceFormProperties.  # noqa: E501

        A configuration parameter - the only accepted values are true and false. When set to true, this parameter captures new properties in the events and engage tables' records. If set to false, new properties will be ignored.   # noqa: E501

        :return: The select_properties_by_default of this SourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._select_properties_by_default

    @select_properties_by_default.setter
    def select_properties_by_default(self, select_properties_by_default):
        """Sets the select_properties_by_default of this SourceFormProperties.

        A configuration parameter - the only accepted values are true and false. When set to true, this parameter captures new properties in the events and engage tables' records. If set to false, new properties will be ignored.   # noqa: E501

        :param select_properties_by_default: The select_properties_by_default of this SourceFormProperties.  # noqa: E501
        :type: str
        """

        self._select_properties_by_default = select_properties_by_default

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
        if not isinstance(other, SourceFormProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceFormProperties):
            return True

        return self.to_dict() != other.to_dict()
