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
from amazon_selling_partner_api.api.reports_api import ReportsApi  # noqa: E501
from amazon_selling_partner_api.rest import ApiException


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self):
        self.api = ReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_report(self):
        """Test case for cancel_report

        """
        pass

    def test_cancel_report_schedule(self):
        """Test case for cancel_report_schedule

        """
        pass

    def test_create_report(self):
        """Test case for create_report

        """
        pass

    def test_create_report_schedule(self):
        """Test case for create_report_schedule

        """
        pass

    def test_get_report(self):
        """Test case for get_report

        """
        pass

    def test_get_report_document(self):
        """Test case for get_report_document

        """
        pass

    def test_get_report_schedule(self):
        """Test case for get_report_schedule

        """
        pass

    def test_get_report_schedules(self):
        """Test case for get_report_schedules

        """
        pass

    def test_get_reports(self):
        """Test case for get_reports

        """
        pass


if __name__ == '__main__':
    unittest.main()
