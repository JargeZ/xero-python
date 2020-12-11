# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class ManualTaxType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    PAYGMANUAL = "PAYGMANUAL"
    ETPOMANUAL = "ETPOMANUAL"
    ETPRMANUAL = "ETPRMANUAL"
    SCHEDULE5MANUAL = "SCHEDULE5MANUAL"
    SCHEDULE5STSLMANUAL = "SCHEDULE5STSLMANUAL"
