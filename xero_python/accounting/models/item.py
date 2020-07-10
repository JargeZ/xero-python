# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.7
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Item(BaseModel):
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
        "code": "str",
        "inventory_asset_account_code": "str",
        "name": "str",
        "is_sold": "bool",
        "is_purchased": "bool",
        "description": "str",
        "purchase_description": "str",
        "purchase_details": "Purchase",
        "sales_details": "Purchase",
        "is_tracked_as_inventory": "bool",
        "total_cost_pool": "float",
        "quantity_on_hand": "float",
        "updated_date_utc": "datetime[ms-format]",
        "item_id": "str",
        "status_attribute_string": "str",
        "validation_errors": "list[ValidationError]",
    }

    attribute_map = {
        "code": "Code",
        "inventory_asset_account_code": "InventoryAssetAccountCode",
        "name": "Name",
        "is_sold": "IsSold",
        "is_purchased": "IsPurchased",
        "description": "Description",
        "purchase_description": "PurchaseDescription",
        "purchase_details": "PurchaseDetails",
        "sales_details": "SalesDetails",
        "is_tracked_as_inventory": "IsTrackedAsInventory",
        "total_cost_pool": "TotalCostPool",
        "quantity_on_hand": "QuantityOnHand",
        "updated_date_utc": "UpdatedDateUTC",
        "item_id": "ItemID",
        "status_attribute_string": "StatusAttributeString",
        "validation_errors": "ValidationErrors",
    }

    def __init__(
        self,
        code=None,
        inventory_asset_account_code=None,
        name=None,
        is_sold=None,
        is_purchased=None,
        description=None,
        purchase_description=None,
        purchase_details=None,
        sales_details=None,
        is_tracked_as_inventory=None,
        total_cost_pool=None,
        quantity_on_hand=None,
        updated_date_utc=None,
        item_id=None,
        status_attribute_string=None,
        validation_errors=None,
    ):  # noqa: E501
        """Item - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._inventory_asset_account_code = None
        self._name = None
        self._is_sold = None
        self._is_purchased = None
        self._description = None
        self._purchase_description = None
        self._purchase_details = None
        self._sales_details = None
        self._is_tracked_as_inventory = None
        self._total_cost_pool = None
        self._quantity_on_hand = None
        self._updated_date_utc = None
        self._item_id = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None

        self.code = code
        if inventory_asset_account_code is not None:
            self.inventory_asset_account_code = inventory_asset_account_code
        if name is not None:
            self.name = name
        if is_sold is not None:
            self.is_sold = is_sold
        if is_purchased is not None:
            self.is_purchased = is_purchased
        if description is not None:
            self.description = description
        if purchase_description is not None:
            self.purchase_description = purchase_description
        if purchase_details is not None:
            self.purchase_details = purchase_details
        if sales_details is not None:
            self.sales_details = sales_details
        if is_tracked_as_inventory is not None:
            self.is_tracked_as_inventory = is_tracked_as_inventory
        if total_cost_pool is not None:
            self.total_cost_pool = total_cost_pool
        if quantity_on_hand is not None:
            self.quantity_on_hand = quantity_on_hand
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if item_id is not None:
            self.item_id = item_id
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def code(self):
        """Gets the code of this Item.  # noqa: E501

        User defined item code (max length = 30)  # noqa: E501

        :return: The code of this Item.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Item.

        User defined item code (max length = 30)  # noqa: E501

        :param code: The code of this Item.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError(
                "Invalid value for `code`, must not be `None`"
            )  # noqa: E501
        if code is not None and len(code) > 30:
            raise ValueError(
                "Invalid value for `code`, " "length must be less than or equal to `30`"
            )  # noqa: E501

        self._code = code

    @property
    def inventory_asset_account_code(self):
        """Gets the inventory_asset_account_code of this Item.  # noqa: E501

        The inventory asset account for the item. The account must be of type INVENTORY. The  COGSAccountCode in PurchaseDetails is also required to create a tracked item  # noqa: E501

        :return: The inventory_asset_account_code of this Item.  # noqa: E501
        :rtype: str
        """
        return self._inventory_asset_account_code

    @inventory_asset_account_code.setter
    def inventory_asset_account_code(self, inventory_asset_account_code):
        """Sets the inventory_asset_account_code of this Item.

        The inventory asset account for the item. The account must be of type INVENTORY. The  COGSAccountCode in PurchaseDetails is also required to create a tracked item  # noqa: E501

        :param inventory_asset_account_code: The inventory_asset_account_code of this Item.  # noqa: E501
        :type: str
        """

        self._inventory_asset_account_code = inventory_asset_account_code

    @property
    def name(self):
        """Gets the name of this Item.  # noqa: E501

        The name of the item (max length = 50)  # noqa: E501

        :return: The name of this Item.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Item.

        The name of the item (max length = 50)  # noqa: E501

        :param name: The name of this Item.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError(
                "Invalid value for `name`, " "length must be less than or equal to `50`"
            )  # noqa: E501

        self._name = name

    @property
    def is_sold(self):
        """Gets the is_sold of this Item.  # noqa: E501

        Boolean value, defaults to true. When IsSold is true the item will be available on sales transactions in the Xero UI. If IsSold is updated to false then Description and SalesDetails values will be nulled.  # noqa: E501

        :return: The is_sold of this Item.  # noqa: E501
        :rtype: bool
        """
        return self._is_sold

    @is_sold.setter
    def is_sold(self, is_sold):
        """Sets the is_sold of this Item.

        Boolean value, defaults to true. When IsSold is true the item will be available on sales transactions in the Xero UI. If IsSold is updated to false then Description and SalesDetails values will be nulled.  # noqa: E501

        :param is_sold: The is_sold of this Item.  # noqa: E501
        :type: bool
        """

        self._is_sold = is_sold

    @property
    def is_purchased(self):
        """Gets the is_purchased of this Item.  # noqa: E501

        Boolean value, defaults to true. When IsPurchased is true the item is available for purchase transactions in the Xero UI. If IsPurchased is updated to false then PurchaseDescription and PurchaseDetails values will be nulled.  # noqa: E501

        :return: The is_purchased of this Item.  # noqa: E501
        :rtype: bool
        """
        return self._is_purchased

    @is_purchased.setter
    def is_purchased(self, is_purchased):
        """Sets the is_purchased of this Item.

        Boolean value, defaults to true. When IsPurchased is true the item is available for purchase transactions in the Xero UI. If IsPurchased is updated to false then PurchaseDescription and PurchaseDetails values will be nulled.  # noqa: E501

        :param is_purchased: The is_purchased of this Item.  # noqa: E501
        :type: bool
        """

        self._is_purchased = is_purchased

    @property
    def description(self):
        """Gets the description of this Item.  # noqa: E501

        The sales description of the item (max length = 4000)  # noqa: E501

        :return: The description of this Item.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Item.

        The sales description of the item (max length = 4000)  # noqa: E501

        :param description: The description of this Item.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 4000:
            raise ValueError(
                "Invalid value for `description`, "
                "length must be less than or equal to `4000`"
            )  # noqa: E501

        self._description = description

    @property
    def purchase_description(self):
        """Gets the purchase_description of this Item.  # noqa: E501

        The purchase description of the item (max length = 4000)  # noqa: E501

        :return: The purchase_description of this Item.  # noqa: E501
        :rtype: str
        """
        return self._purchase_description

    @purchase_description.setter
    def purchase_description(self, purchase_description):
        """Sets the purchase_description of this Item.

        The purchase description of the item (max length = 4000)  # noqa: E501

        :param purchase_description: The purchase_description of this Item.  # noqa: E501
        :type: str
        """
        if purchase_description is not None and len(purchase_description) > 4000:
            raise ValueError(
                "Invalid value for `purchase_description`, "
                "length must be less than or equal to `4000`"
            )  # noqa: E501

        self._purchase_description = purchase_description

    @property
    def purchase_details(self):
        """Gets the purchase_details of this Item.  # noqa: E501


        :return: The purchase_details of this Item.  # noqa: E501
        :rtype: Purchase
        """
        return self._purchase_details

    @purchase_details.setter
    def purchase_details(self, purchase_details):
        """Sets the purchase_details of this Item.


        :param purchase_details: The purchase_details of this Item.  # noqa: E501
        :type: Purchase
        """

        self._purchase_details = purchase_details

    @property
    def sales_details(self):
        """Gets the sales_details of this Item.  # noqa: E501


        :return: The sales_details of this Item.  # noqa: E501
        :rtype: Purchase
        """
        return self._sales_details

    @sales_details.setter
    def sales_details(self, sales_details):
        """Sets the sales_details of this Item.


        :param sales_details: The sales_details of this Item.  # noqa: E501
        :type: Purchase
        """

        self._sales_details = sales_details

    @property
    def is_tracked_as_inventory(self):
        """Gets the is_tracked_as_inventory of this Item.  # noqa: E501

        True for items that are tracked as inventory. An item will be tracked as inventory if the InventoryAssetAccountCode and COGSAccountCode are set.  # noqa: E501

        :return: The is_tracked_as_inventory of this Item.  # noqa: E501
        :rtype: bool
        """
        return self._is_tracked_as_inventory

    @is_tracked_as_inventory.setter
    def is_tracked_as_inventory(self, is_tracked_as_inventory):
        """Sets the is_tracked_as_inventory of this Item.

        True for items that are tracked as inventory. An item will be tracked as inventory if the InventoryAssetAccountCode and COGSAccountCode are set.  # noqa: E501

        :param is_tracked_as_inventory: The is_tracked_as_inventory of this Item.  # noqa: E501
        :type: bool
        """

        self._is_tracked_as_inventory = is_tracked_as_inventory

    @property
    def total_cost_pool(self):
        """Gets the total_cost_pool of this Item.  # noqa: E501

        The value of the item on hand. Calculated using average cost accounting.  # noqa: E501

        :return: The total_cost_pool of this Item.  # noqa: E501
        :rtype: float
        """
        return self._total_cost_pool

    @total_cost_pool.setter
    def total_cost_pool(self, total_cost_pool):
        """Sets the total_cost_pool of this Item.

        The value of the item on hand. Calculated using average cost accounting.  # noqa: E501

        :param total_cost_pool: The total_cost_pool of this Item.  # noqa: E501
        :type: float
        """

        self._total_cost_pool = total_cost_pool

    @property
    def quantity_on_hand(self):
        """Gets the quantity_on_hand of this Item.  # noqa: E501

        The quantity of the item on hand  # noqa: E501

        :return: The quantity_on_hand of this Item.  # noqa: E501
        :rtype: float
        """
        return self._quantity_on_hand

    @quantity_on_hand.setter
    def quantity_on_hand(self, quantity_on_hand):
        """Sets the quantity_on_hand of this Item.

        The quantity of the item on hand  # noqa: E501

        :param quantity_on_hand: The quantity_on_hand of this Item.  # noqa: E501
        :type: float
        """

        self._quantity_on_hand = quantity_on_hand

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Item.  # noqa: E501

        Last modified date in UTC format  # noqa: E501

        :return: The updated_date_utc of this Item.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Item.

        Last modified date in UTC format  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Item.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def item_id(self):
        """Gets the item_id of this Item.  # noqa: E501

        The Xero identifier for an Item  # noqa: E501

        :return: The item_id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this Item.

        The Xero identifier for an Item  # noqa: E501

        :param item_id: The item_id of this Item.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this Item.  # noqa: E501

        Status of object  # noqa: E501

        :return: The status_attribute_string of this Item.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this Item.

        Status of object  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this Item.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Item.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Item.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Item.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Item.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors