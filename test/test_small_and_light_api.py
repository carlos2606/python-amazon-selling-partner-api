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
from amazon_selling_partner_api.api.small_and_light_api import SmallAndLightApi  # noqa: E501
from amazon_selling_partner_api.rest import ApiException


class TestSmallAndLightApi(unittest.TestCase):
    """SmallAndLightApi unit test stubs"""

    def setUp(self):
        self.api = SmallAndLightApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_small_and_light_enrollment_by_seller_sku(self):
        """Test case for delete_small_and_light_enrollment_by_seller_sku

        """
        pass

    def test_get_small_and_light_eligibility_by_seller_sku(self):
        """Test case for get_small_and_light_eligibility_by_seller_sku

        """
        pass

    def test_get_small_and_light_enrollment_by_seller_sku(self):
        """Test case for get_small_and_light_enrollment_by_seller_sku

        """
        pass

    def test_get_small_and_light_fee_preview(self):
        """Test case for get_small_and_light_fee_preview

        """
        pass

    def test_put_small_and_light_enrollment_by_seller_sku(self):
        """Test case for put_small_and_light_enrollment_by_seller_sku

        """
        pass


if __name__ == '__main__':
    unittest.main()
