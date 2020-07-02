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


class ReportAttribute(BaseModel):
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
    openapi_types = {"id": "str", "value": "str"}

    attribute_map = {"id": "Id", "value": "Value"}

    def __init__(self, id=None, value=None):  # noqa: E501
        """ReportAttribute - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if value is not None:
            self.value = value

    @property
    def id(self):
        """Gets the id of this ReportAttribute.  # noqa: E501


        :return: The id of this ReportAttribute.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportAttribute.


        :param id: The id of this ReportAttribute.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this ReportAttribute.  # noqa: E501


        :return: The value of this ReportAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ReportAttribute.


        :param value: The value of this ReportAttribute.  # noqa: E501
        :type: str
        """

        self._value = value
