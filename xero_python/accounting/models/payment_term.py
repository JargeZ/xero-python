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


class PaymentTerm(BaseModel):
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
    openapi_types = {"bills": "Bill", "sales": "Bill"}

    attribute_map = {"bills": "Bills", "sales": "Sales"}

    def __init__(self, bills=None, sales=None):  # noqa: E501
        """PaymentTerm - a model defined in OpenAPI"""  # noqa: E501

        self._bills = None
        self._sales = None
        self.discriminator = None

        if bills is not None:
            self.bills = bills
        if sales is not None:
            self.sales = sales

    @property
    def bills(self):
        """Gets the bills of this PaymentTerm.  # noqa: E501


        :return: The bills of this PaymentTerm.  # noqa: E501
        :rtype: Bill
        """
        return self._bills

    @bills.setter
    def bills(self, bills):
        """Sets the bills of this PaymentTerm.


        :param bills: The bills of this PaymentTerm.  # noqa: E501
        :type: Bill
        """

        self._bills = bills

    @property
    def sales(self):
        """Gets the sales of this PaymentTerm.  # noqa: E501


        :return: The sales of this PaymentTerm.  # noqa: E501
        :rtype: Bill
        """
        return self._sales

    @sales.setter
    def sales(self, sales):
        """Sets the sales of this PaymentTerm.


        :param sales: The sales of this PaymentTerm.  # noqa: E501
        :type: Bill
        """

        self._sales = sales
