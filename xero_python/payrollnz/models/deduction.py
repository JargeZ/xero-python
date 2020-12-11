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


class Deduction(BaseModel):
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
        "deduction_id": "str",
        "deduction_name": "str",
        "deduction_category": "str",
        "liability_account_id": "str",
        "current_record": "bool",
        "standard_amount": "float",
    }

    attribute_map = {
        "deduction_id": "deductionId",
        "deduction_name": "deductionName",
        "deduction_category": "deductionCategory",
        "liability_account_id": "liabilityAccountId",
        "current_record": "currentRecord",
        "standard_amount": "standardAmount",
    }

    def __init__(
        self,
        deduction_id=None,
        deduction_name=None,
        deduction_category=None,
        liability_account_id=None,
        current_record=None,
        standard_amount=None,
    ):  # noqa: E501
        """Deduction - a model defined in OpenAPI"""  # noqa: E501

        self._deduction_id = None
        self._deduction_name = None
        self._deduction_category = None
        self._liability_account_id = None
        self._current_record = None
        self._standard_amount = None
        self.discriminator = None

        if deduction_id is not None:
            self.deduction_id = deduction_id
        self.deduction_name = deduction_name
        self.deduction_category = deduction_category
        self.liability_account_id = liability_account_id
        if current_record is not None:
            self.current_record = current_record
        if standard_amount is not None:
            self.standard_amount = standard_amount

    @property
    def deduction_id(self):
        """Gets the deduction_id of this Deduction.  # noqa: E501

        The Xero identifier for Deduction  # noqa: E501

        :return: The deduction_id of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._deduction_id

    @deduction_id.setter
    def deduction_id(self, deduction_id):
        """Sets the deduction_id of this Deduction.

        The Xero identifier for Deduction  # noqa: E501

        :param deduction_id: The deduction_id of this Deduction.  # noqa: E501
        :type: str
        """

        self._deduction_id = deduction_id

    @property
    def deduction_name(self):
        """Gets the deduction_name of this Deduction.  # noqa: E501

        Name of the deduction  # noqa: E501

        :return: The deduction_name of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._deduction_name

    @deduction_name.setter
    def deduction_name(self, deduction_name):
        """Sets the deduction_name of this Deduction.

        Name of the deduction  # noqa: E501

        :param deduction_name: The deduction_name of this Deduction.  # noqa: E501
        :type: str
        """
        if deduction_name is None:
            raise ValueError(
                "Invalid value for `deduction_name`, must not be `None`"
            )  # noqa: E501

        self._deduction_name = deduction_name

    @property
    def deduction_category(self):
        """Gets the deduction_category of this Deduction.  # noqa: E501

        Deduction Category type  # noqa: E501

        :return: The deduction_category of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._deduction_category

    @deduction_category.setter
    def deduction_category(self, deduction_category):
        """Sets the deduction_category of this Deduction.

        Deduction Category type  # noqa: E501

        :param deduction_category: The deduction_category of this Deduction.  # noqa: E501
        :type: str
        """
        if deduction_category is None:
            raise ValueError(
                "Invalid value for `deduction_category`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "PayrollGiving",
            "KiwiSaverVoluntaryContributions",
            "Superannuation",
            "NzOther",
            "None",
        ]  # noqa: E501
        if deduction_category not in allowed_values:
            raise ValueError(
                "Invalid value for `deduction_category` ({0}), must be one of {1}".format(  # noqa: E501
                    deduction_category, allowed_values
                )
            )

        self._deduction_category = deduction_category

    @property
    def liability_account_id(self):
        """Gets the liability_account_id of this Deduction.  # noqa: E501

        Xero identifier for Liability Account  # noqa: E501

        :return: The liability_account_id of this Deduction.  # noqa: E501
        :rtype: str
        """
        return self._liability_account_id

    @liability_account_id.setter
    def liability_account_id(self, liability_account_id):
        """Sets the liability_account_id of this Deduction.

        Xero identifier for Liability Account  # noqa: E501

        :param liability_account_id: The liability_account_id of this Deduction.  # noqa: E501
        :type: str
        """
        if liability_account_id is None:
            raise ValueError(
                "Invalid value for `liability_account_id`, must not be `None`"
            )  # noqa: E501

        self._liability_account_id = liability_account_id

    @property
    def current_record(self):
        """Gets the current_record of this Deduction.  # noqa: E501

        Identifier of a record is active or not.  # noqa: E501

        :return: The current_record of this Deduction.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this Deduction.

        Identifier of a record is active or not.  # noqa: E501

        :param current_record: The current_record of this Deduction.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record

    @property
    def standard_amount(self):
        """Gets the standard_amount of this Deduction.  # noqa: E501

        Standard amount of the deduction.  # noqa: E501

        :return: The standard_amount of this Deduction.  # noqa: E501
        :rtype: float
        """
        return self._standard_amount

    @standard_amount.setter
    def standard_amount(self, standard_amount):
        """Sets the standard_amount of this Deduction.

        Standard amount of the deduction.  # noqa: E501

        :param standard_amount: The standard_amount of this Deduction.  # noqa: E501
        :type: float
        """

        self._standard_amount = standard_amount
