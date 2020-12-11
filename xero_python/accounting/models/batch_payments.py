# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BatchPayments(BaseModel):
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
    openapi_types = {"batch_payments": "list[BatchPayment]"}

    attribute_map = {"batch_payments": "BatchPayments"}

    def __init__(self, batch_payments=None):  # noqa: E501
        """BatchPayments - a model defined in OpenAPI"""  # noqa: E501

        self._batch_payments = None
        self.discriminator = None

        if batch_payments is not None:
            self.batch_payments = batch_payments

    @property
    def batch_payments(self):
        """Gets the batch_payments of this BatchPayments.  # noqa: E501


        :return: The batch_payments of this BatchPayments.  # noqa: E501
        :rtype: list[BatchPayment]
        """
        return self._batch_payments

    @batch_payments.setter
    def batch_payments(self, batch_payments):
        """Sets the batch_payments of this BatchPayments.


        :param batch_payments: The batch_payments of this BatchPayments.  # noqa: E501
        :type: list[BatchPayment]
        """

        self._batch_payments = batch_payments
