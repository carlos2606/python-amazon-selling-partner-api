# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import amazon_selling_partner_api
from amazon_selling_partner_api.api.fba_inbound_api import FbaInboundApi  # noqa: E501
from amazon_selling_partner_api.rest import ApiException


class TestFbaInboundApi(unittest.TestCase):
    """FbaInboundApi unit test stubs"""

    def setUp(self):
        self.api = FbaInboundApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_confirm_preorder(self):
        """Test case for confirm_preorder

        """
        pass

    def test_confirm_transport(self):
        """Test case for confirm_transport

        """
        pass

    def test_create_inbound_shipment(self):
        """Test case for create_inbound_shipment

        """
        pass

    def test_create_inbound_shipment_plan(self):
        """Test case for create_inbound_shipment_plan

        """
        pass

    def test_estimate_transport(self):
        """Test case for estimate_transport

        """
        pass

    def test_get_bill_of_lading(self):
        """Test case for get_bill_of_lading

        """
        pass

    def test_get_inbound_guidance(self):
        """Test case for get_inbound_guidance

        """
        pass

    def test_get_item_eligibility_preview(self):
        """Test case for get_item_eligibility_preview

        """
        pass

    def test_get_labels(self):
        """Test case for get_labels

        """
        pass

    def test_get_preorder_info(self):
        """Test case for get_preorder_info

        """
        pass

    def test_get_prep_instructions(self):
        """Test case for get_prep_instructions

        """
        pass

    def test_get_shipment_items(self):
        """Test case for get_shipment_items

        """
        pass

    def test_get_shipment_items_by_shipment_id(self):
        """Test case for get_shipment_items_by_shipment_id

        """
        pass

    def test_get_shipments(self):
        """Test case for get_shipments

        """
        pass

    def test_get_transport_details(self):
        """Test case for get_transport_details

        """
        pass

    def test_put_transport_details(self):
        """Test case for put_transport_details

        """
        pass

    def test_update_inbound_shipment(self):
        """Test case for update_inbound_shipment

        """
        pass

    def test_void_transport(self):
        """Test case for void_transport

        """
        pass


if __name__ == '__main__':
    unittest.main()
