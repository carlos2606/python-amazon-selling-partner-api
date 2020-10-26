# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.authorization_api import AuthorizationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAuthorizationApi(unittest.TestCase):
    """AuthorizationApi unit test stubs"""

    def setUp(self):
        self.api = api.authorization_api.AuthorizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_authorization_code(self):
        """Test case for get_authorization_code

        Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()