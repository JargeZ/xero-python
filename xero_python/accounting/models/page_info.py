# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PageInfo(BaseModel):
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
        "page": "int",
        "page_size": "int",
        "total_pages": "int",
        "total_rows": "int",
    }

    attribute_map = {
        "page": "Page",
        "page_size": "PageSize",
        "total_pages": "TotalPages",
        "total_rows": "TotalRows",
    }

    def __init__(
        self, page=None, page_size=None, total_pages=None, total_rows=None
    ):  # noqa: E501
        """PageInfo - a model defined in OpenAPI"""  # noqa: E501

        self._page = None
        self._page_size = None
        self._total_pages = None
        self._total_rows = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total_pages is not None:
            self.total_pages = total_pages
        if total_rows is not None:
            self.total_rows = total_rows

    @property
    def page(self):
        """Gets the page of this PageInfo.  # noqa: E501


        :return: The page of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PageInfo.


        :param page: The page of this PageInfo.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this PageInfo.  # noqa: E501


        :return: The page_size of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PageInfo.


        :param page_size: The page_size of this PageInfo.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_pages(self):
        """Gets the total_pages of this PageInfo.  # noqa: E501


        :return: The total_pages of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PageInfo.


        :param total_pages: The total_pages of this PageInfo.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def total_rows(self):
        """Gets the total_rows of this PageInfo.  # noqa: E501


        :return: The total_rows of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this PageInfo.


        :param total_rows: The total_rows of this PageInfo.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows