# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class StatutoryDeductionCategory(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    ADDITIONALSTUDENTLOAN = "AdditionalStudentLoan"
    CHILDSUPPORT = "ChildSupport"
    COURTFINES = "CourtFines"
    CREDITOR = "Creditor"
    FEDERALLEVY = "FederalLevy"
    INLANDREVENUEARREARS = "InlandRevenueArrears"
    KIWISAVER = "KiwiSaver"
    MSDREPAYMENTS = "MsdRepayments"
    NONPRIORITYORDER = "NonPriorityOrder"
    PRIORITYORDER = "PriorityOrder"
    TABLEBASED = "TableBased"
    STUDENTLOAN = "StudentLoan"
    VOLUNTARYSTUDENTLOAN = "VoluntaryStudentLoan"
    USCHILDSUPPORT = "USChildSupport"