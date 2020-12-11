# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EarningsOrder(BaseModel):
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
        "id": "str",
        "name": "str",
        "statutory_deduction_category": "StatutoryDeductionCategory",
        "liability_account_id": "str",
        "current_record": "bool",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "statutory_deduction_category": "statutoryDeductionCategory",
        "liability_account_id": "liabilityAccountId",
        "current_record": "currentRecord",
    }

    def __init__(
        self,
        id=None,
        name=None,
        statutory_deduction_category=None,
        liability_account_id=None,
        current_record=True,
    ):  # noqa: E501
        """EarningsOrder - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._statutory_deduction_category = None
        self._liability_account_id = None
        self._current_record = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if statutory_deduction_category is not None:
            self.statutory_deduction_category = statutory_deduction_category
        if liability_account_id is not None:
            self.liability_account_id = liability_account_id
        if current_record is not None:
            self.current_record = current_record

    @property
    def id(self):
        """Gets the id of this EarningsOrder.  # noqa: E501

        Xero unique identifier for an earning rate  # noqa: E501

        :return: The id of this EarningsOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EarningsOrder.

        Xero unique identifier for an earning rate  # noqa: E501

        :param id: The id of this EarningsOrder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EarningsOrder.  # noqa: E501

        Name of the earning order  # noqa: E501

        :return: The name of this EarningsOrder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EarningsOrder.

        Name of the earning order  # noqa: E501

        :param name: The name of this EarningsOrder.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def statutory_deduction_category(self):
        """Gets the statutory_deduction_category of this EarningsOrder.  # noqa: E501


        :return: The statutory_deduction_category of this EarningsOrder.  # noqa: E501
        :rtype: StatutoryDeductionCategory
        """
        return self._statutory_deduction_category

    @statutory_deduction_category.setter
    def statutory_deduction_category(self, statutory_deduction_category):
        """Sets the statutory_deduction_category of this EarningsOrder.


        :param statutory_deduction_category: The statutory_deduction_category of this EarningsOrder.  # noqa: E501
        :type: StatutoryDeductionCategory
        """

        self._statutory_deduction_category = statutory_deduction_category

    @property
    def liability_account_id(self):
        """Gets the liability_account_id of this EarningsOrder.  # noqa: E501

        Xero identifier for Liability Account  # noqa: E501

        :return: The liability_account_id of this EarningsOrder.  # noqa: E501
        :rtype: str
        """
        return self._liability_account_id

    @liability_account_id.setter
    def liability_account_id(self, liability_account_id):
        """Sets the liability_account_id of this EarningsOrder.

        Xero identifier for Liability Account  # noqa: E501

        :param liability_account_id: The liability_account_id of this EarningsOrder.  # noqa: E501
        :type: str
        """

        self._liability_account_id = liability_account_id

    @property
    def current_record(self):
        """Gets the current_record of this EarningsOrder.  # noqa: E501

        Identifier of a record is active or not.  # noqa: E501

        :return: The current_record of this EarningsOrder.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this EarningsOrder.

        Identifier of a record is active or not.  # noqa: E501

        :param current_record: The current_record of this EarningsOrder.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record
