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
from amazon_selling_partner_api.api.solicitations_api import SolicitationsApi  # noqa: E501
from amazon_selling_partner_api.rest import ApiException


class TestSolicitationsApi(unittest.TestCase):
    """SolicitationsApi unit test stubs"""

    def setUp(self):
        self.api = SolicitationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_product_review_and_seller_feedback_solicitation(self):
        """Test case for create_product_review_and_seller_feedback_solicitation

        """
        pass

    def test_get_solicitation_actions_for_order(self):
        """Test case for get_solicitation_actions_for_order

        """
        pass


if __name__ == '__main__':
    unittest.main()
