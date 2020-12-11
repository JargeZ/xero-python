# coding: utf-8

"""
    Xero Assets API

    This is the Xero Assets API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BookDepreciationSetting(BaseModel):
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
        "depreciation_method": "str",
        "averaging_method": "str",
        "depreciation_rate": "float",
        "effective_life_years": "int",
        "depreciation_calculation_method": "str",
        "depreciable_object_id": "str",
        "depreciable_object_type": "str",
        "book_effective_date_of_change_id": "str",
    }

    attribute_map = {
        "depreciation_method": "depreciationMethod",
        "averaging_method": "averagingMethod",
        "depreciation_rate": "depreciationRate",
        "effective_life_years": "effectiveLifeYears",
        "depreciation_calculation_method": "depreciationCalculationMethod",
        "depreciable_object_id": "depreciableObjectId",
        "depreciable_object_type": "depreciableObjectType",
        "book_effective_date_of_change_id": "bookEffectiveDateOfChangeId",
    }

    def __init__(
        self,
        depreciation_method=None,
        averaging_method=None,
        depreciation_rate=None,
        effective_life_years=None,
        depreciation_calculation_method=None,
        depreciable_object_id=None,
        depreciable_object_type=None,
        book_effective_date_of_change_id=None,
    ):  # noqa: E501
        """BookDepreciationSetting - a model defined in OpenAPI"""  # noqa: E501

        self._depreciation_method = None
        self._averaging_method = None
        self._depreciation_rate = None
        self._effective_life_years = None
        self._depreciation_calculation_method = None
        self._depreciable_object_id = None
        self._depreciable_object_type = None
        self._book_effective_date_of_change_id = None
        self.discriminator = None

        if depreciation_method is not None:
            self.depreciation_method = depreciation_method
        if averaging_method is not None:
            self.averaging_method = averaging_method
        if depreciation_rate is not None:
            self.depreciation_rate = depreciation_rate
        if effective_life_years is not None:
            self.effective_life_years = effective_life_years
        if depreciation_calculation_method is not None:
            self.depreciation_calculation_method = depreciation_calculation_method
        if depreciable_object_id is not None:
            self.depreciable_object_id = depreciable_object_id
        if depreciable_object_type is not None:
            self.depreciable_object_type = depreciable_object_type
        if book_effective_date_of_change_id is not None:
            self.book_effective_date_of_change_id = book_effective_date_of_change_id

    @property
    def depreciation_method(self):
        """Gets the depreciation_method of this BookDepreciationSetting.  # noqa: E501

        The method of depreciation applied to this asset. See Depreciation Methods  # noqa: E501

        :return: The depreciation_method of this BookDepreciationSetting.  # noqa: E501
        :rtype: str
        """
        return self._depreciation_method

    @depreciation_method.setter
    def depreciation_method(self, depreciation_method):
        """Sets the depreciation_method of this BookDepreciationSetting.

        The method of depreciation applied to this asset. See Depreciation Methods  # noqa: E501

        :param depreciation_method: The depreciation_method of this BookDepreciationSetting.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "NoDepreciation",
            "StraightLine",
            "DiminishingValue100",
            "DiminishingValue150",
            "DiminishingValue200",
            "FullDepreciation",
            "None",
        ]  # noqa: E501
        if depreciation_method not in allowed_values:
            raise ValueError(
                "Invalid value for `depreciation_method` ({0}), must be one of {1}".format(  # noqa: E501
                    depreciation_method, allowed_values
                )
            )

        self._depreciation_method = depreciation_method

    @property
    def averaging_method(self):
        """Gets the averaging_method of this BookDepreciationSetting.  # noqa: E501

        The method of averaging applied to this asset. See Averaging Methods  # noqa: E501

        :return: The averaging_method of this BookDepreciationSetting.  # noqa: E501
        :rtype: str
        """
        return self._averaging_method

    @averaging_method.setter
    def averaging_method(self, averaging_method):
        """Sets the averaging_method of this BookDepreciationSetting.

        The method of averaging applied to this asset. See Averaging Methods  # noqa: E501

        :param averaging_method: The averaging_method of this BookDepreciationSetting.  # noqa: E501
        :type: str
        """
        allowed_values = ["FullMonth", "ActualDays", "None"]  # noqa: E501
        if averaging_method not in allowed_values:
            raise ValueError(
                "Invalid value for `averaging_method` ({0}), must be one of {1}".format(  # noqa: E501
                    averaging_method, allowed_values
                )
            )

        self._averaging_method = averaging_method

    @property
    def depreciation_rate(self):
        """Gets the depreciation_rate of this BookDepreciationSetting.  # noqa: E501

        The rate of depreciation (e.g. 0.05)  # noqa: E501

        :return: The depreciation_rate of this BookDepreciationSetting.  # noqa: E501
        :rtype: float
        """
        return self._depreciation_rate

    @depreciation_rate.setter
    def depreciation_rate(self, depreciation_rate):
        """Sets the depreciation_rate of this BookDepreciationSetting.

        The rate of depreciation (e.g. 0.05)  # noqa: E501

        :param depreciation_rate: The depreciation_rate of this BookDepreciationSetting.  # noqa: E501
        :type: float
        """

        self._depreciation_rate = depreciation_rate

    @property
    def effective_life_years(self):
        """Gets the effective_life_years of this BookDepreciationSetting.  # noqa: E501

        Effective life of the asset in years (e.g. 5)  # noqa: E501

        :return: The effective_life_years of this BookDepreciationSetting.  # noqa: E501
        :rtype: int
        """
        return self._effective_life_years

    @effective_life_years.setter
    def effective_life_years(self, effective_life_years):
        """Sets the effective_life_years of this BookDepreciationSetting.

        Effective life of the asset in years (e.g. 5)  # noqa: E501

        :param effective_life_years: The effective_life_years of this BookDepreciationSetting.  # noqa: E501
        :type: int
        """

        self._effective_life_years = effective_life_years

    @property
    def depreciation_calculation_method(self):
        """Gets the depreciation_calculation_method of this BookDepreciationSetting.  # noqa: E501

        See Depreciation Calculation Methods  # noqa: E501

        :return: The depreciation_calculation_method of this BookDepreciationSetting.  # noqa: E501
        :rtype: str
        """
        return self._depreciation_calculation_method

    @depreciation_calculation_method.setter
    def depreciation_calculation_method(self, depreciation_calculation_method):
        """Sets the depreciation_calculation_method of this BookDepreciationSetting.

        See Depreciation Calculation Methods  # noqa: E501

        :param depreciation_calculation_method: The depreciation_calculation_method of this BookDepreciationSetting.  # noqa: E501
        :type: str
        """
        allowed_values = ["Rate", "Life", "None", "None"]  # noqa: E501
        if depreciation_calculation_method not in allowed_values:
            raise ValueError(
                "Invalid value for `depreciation_calculation_method` ({0}), must be one of {1}".format(  # noqa: E501
                    depreciation_calculation_method, allowed_values
                )
            )

        self._depreciation_calculation_method = depreciation_calculation_method

    @property
    def depreciable_object_id(self):
        """Gets the depreciable_object_id of this BookDepreciationSetting.  # noqa: E501

        Unique Xero identifier for the depreciable object  # noqa: E501

        :return: The depreciable_object_id of this BookDepreciationSetting.  # noqa: E501
        :rtype: str
        """
        return self._depreciable_object_id

    @depreciable_object_id.setter
    def depreciable_object_id(self, depreciable_object_id):
        """Sets the depreciable_object_id of this BookDepreciationSetting.

        Unique Xero identifier for the depreciable object  # noqa: E501

        :param depreciable_object_id: The depreciable_object_id of this BookDepreciationSetting.  # noqa: E501
        :type: str
        """

        self._depreciable_object_id = depreciable_object_id

    @property
    def depreciable_object_type(self):
        """Gets the depreciable_object_type of this BookDepreciationSetting.  # noqa: E501

        The type of asset object  # noqa: E501

        :return: The depreciable_object_type of this BookDepreciationSetting.  # noqa: E501
        :rtype: str
        """
        return self._depreciable_object_type

    @depreciable_object_type.setter
    def depreciable_object_type(self, depreciable_object_type):
        """Sets the depreciable_object_type of this BookDepreciationSetting.

        The type of asset object  # noqa: E501

        :param depreciable_object_type: The depreciable_object_type of this BookDepreciationSetting.  # noqa: E501
        :type: str
        """

        self._depreciable_object_type = depreciable_object_type

    @property
    def book_effective_date_of_change_id(self):
        """Gets the book_effective_date_of_change_id of this BookDepreciationSetting.  # noqa: E501

        Unique Xero identifier for the effective date change  # noqa: E501

        :return: The book_effective_date_of_change_id of this BookDepreciationSetting.  # noqa: E501
        :rtype: str
        """
        return self._book_effective_date_of_change_id

    @book_effective_date_of_change_id.setter
    def book_effective_date_of_change_id(self, book_effective_date_of_change_id):
        """Sets the book_effective_date_of_change_id of this BookDepreciationSetting.

        Unique Xero identifier for the effective date change  # noqa: E501

        :param book_effective_date_of_change_id: The book_effective_date_of_change_id of this BookDepreciationSetting.  # noqa: E501
        :type: str
        """

        self._book_effective_date_of_change_id = book_effective_date_of_change_id
