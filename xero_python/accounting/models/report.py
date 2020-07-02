# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.5
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Report(BaseModel):
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
        "report_id": "str",
        "report_name": "str",
        "report_type": "str",
        "report_title": "str",
        "report_date": "str",
        "updated_date_utc": "datetime[ms-format]",
        "contacts": "list[TenNinteyNineContact]",
    }

    attribute_map = {
        "report_id": "ReportID",
        "report_name": "ReportName",
        "report_type": "ReportType",
        "report_title": "ReportTitle",
        "report_date": "ReportDate",
        "updated_date_utc": "UpdatedDateUTC",
        "contacts": "Contacts",
    }

    def __init__(
        self,
        report_id=None,
        report_name=None,
        report_type=None,
        report_title=None,
        report_date=None,
        updated_date_utc=None,
        contacts=None,
    ):  # noqa: E501
        """Report - a model defined in OpenAPI"""  # noqa: E501

        self._report_id = None
        self._report_name = None
        self._report_type = None
        self._report_title = None
        self._report_date = None
        self._updated_date_utc = None
        self._contacts = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if report_name is not None:
            self.report_name = report_name
        if report_type is not None:
            self.report_type = report_type
        if report_title is not None:
            self.report_title = report_title
        if report_date is not None:
            self.report_date = report_date
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if contacts is not None:
            self.contacts = contacts

    @property
    def report_id(self):
        """Gets the report_id of this Report.  # noqa: E501

        See Prepayment Types  # noqa: E501

        :return: The report_id of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this Report.

        See Prepayment Types  # noqa: E501

        :param report_id: The report_id of this Report.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def report_name(self):
        """Gets the report_name of this Report.  # noqa: E501

        See Prepayment Types  # noqa: E501

        :return: The report_name of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this Report.

        See Prepayment Types  # noqa: E501

        :param report_name: The report_name of this Report.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def report_type(self):
        """Gets the report_type of this Report.  # noqa: E501

        See Prepayment Types  # noqa: E501

        :return: The report_type of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this Report.

        See Prepayment Types  # noqa: E501

        :param report_type: The report_type of this Report.  # noqa: E501
        :type: str
        """
        allowed_values = ["AgedPayablesByContact"]  # noqa: E501
        if report_type not in allowed_values:
            raise ValueError(
                "Invalid value for `report_type` ({0}), must be one of {1}".format(  # noqa: E501
                    report_type, allowed_values
                )
            )

        self._report_type = report_type

    @property
    def report_title(self):
        """Gets the report_title of this Report.  # noqa: E501

        See Prepayment Types  # noqa: E501

        :return: The report_title of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_title

    @report_title.setter
    def report_title(self, report_title):
        """Sets the report_title of this Report.

        See Prepayment Types  # noqa: E501

        :param report_title: The report_title of this Report.  # noqa: E501
        :type: str
        """

        self._report_title = report_title

    @property
    def report_date(self):
        """Gets the report_date of this Report.  # noqa: E501

        Date of report  # noqa: E501

        :return: The report_date of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_date

    @report_date.setter
    def report_date(self, report_date):
        """Sets the report_date of this Report.

        Date of report  # noqa: E501

        :param report_date: The report_date of this Report.  # noqa: E501
        :type: str
        """

        self._report_date = report_date

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Report.  # noqa: E501

        Updated Date  # noqa: E501

        :return: The updated_date_utc of this Report.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Report.

        Updated Date  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Report.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def contacts(self):
        """Gets the contacts of this Report.  # noqa: E501


        :return: The contacts of this Report.  # noqa: E501
        :rtype: list[TenNinteyNineContact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this Report.


        :param contacts: The contacts of this Report.  # noqa: E501
        :type: list[TenNinteyNineContact]
        """

        self._contacts = contacts
