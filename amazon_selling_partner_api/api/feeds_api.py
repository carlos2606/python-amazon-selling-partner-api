# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from amazon_selling_partner_api.api_client import ApiClient


class FeedsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_feed(self, , **kwargs):  # noqa: E501
        """cancel_feed  # noqa: E501

        Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled. Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_feed(, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : The identifier for the feed. This identifier is unique only in combination with a seller ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_feed_with_http_info(, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_feed_with_http_info(, **kwargs)  # noqa: E501
            return data

    def cancel_feed_with_http_info(self, , **kwargs):  # noqa: E501
        """cancel_feed  # noqa: E501

        Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled. Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_feed_with_http_info(, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : The identifier for the feed. This identifier is unique only in combination with a seller ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_feed" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '' is set
        if ('' not in params or
                params[''] is None):
            raise ValueError("Missing the required parameter `` when calling `cancel_feed`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if '' in params:
            path_params['feedId'] = params['']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feeds/2020-09-04/feeds/{feedId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_feed(self, **kwargs):  # noqa: E501
        """create_feed  # noqa: E501

        Creates a feed. Encrypt and upload the contents of the feed document before calling this operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0083 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_feed(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_feed_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_feed_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_feed_with_http_info(self, **kwargs):  # noqa: E501
        """create_feed  # noqa: E501

        Creates a feed. Encrypt and upload the contents of the feed document before calling this operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0083 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_feed_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_feed" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feeds/2020-09-04/feeds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_feed_document(self, **kwargs):  # noqa: E501
        """create_feed_document  # noqa: E501

        Creates a feed document for the feed type that you specify. This operation returns encryption details for encrypting the contents of the document, as well as a presigned URL for uploading the encrypted feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0083 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_feed_document(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_feed_document_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_feed_document_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_feed_document_with_http_info(self, **kwargs):  # noqa: E501
        """create_feed_document  # noqa: E501

        Creates a feed document for the feed type that you specify. This operation returns encryption details for encrypting the contents of the document, as well as a presigned URL for uploading the encrypted feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0083 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_feed_document_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_feed_document" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feeds/2020-09-04/documents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feed(self, , **kwargs):  # noqa: E501
        """get_feed  # noqa: E501

        Returns feed details (including the resultDocumentId, if available) for the feed that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2.0 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feed(, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : The identifier for the feed. This identifier is unique only in combination with a seller ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_feed_with_http_info(, **kwargs)  # noqa: E501
        else:
            (data) = self.get_feed_with_http_info(, **kwargs)  # noqa: E501
            return data

    def get_feed_with_http_info(self, , **kwargs):  # noqa: E501
        """get_feed  # noqa: E501

        Returns feed details (including the resultDocumentId, if available) for the feed that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2.0 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feed_with_http_info(, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : The identifier for the feed. This identifier is unique only in combination with a seller ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feed" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '' is set
        if ('' not in params or
                params[''] is None):
            raise ValueError("Missing the required parameter `` when calling `get_feed`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if '' in params:
            path_params['feedId'] = params['']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feeds/2020-09-04/feeds/{feedId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feed_document(self, , **kwargs):  # noqa: E501
        """get_feed_document  # noqa: E501

        Returns the information required for retrieving a feed document's contents. This includes a presigned URL for the feed document as well as the information required to decrypt the document's contents.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feed_document(, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : The identifier of the feed document. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_feed_document_with_http_info(, **kwargs)  # noqa: E501
        else:
            (data) = self.get_feed_document_with_http_info(, **kwargs)  # noqa: E501
            return data

    def get_feed_document_with_http_info(self, , **kwargs):  # noqa: E501
        """get_feed_document  # noqa: E501

        Returns the information required for retrieving a feed document's contents. This includes a presigned URL for the feed document as well as the information required to decrypt the document's contents.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feed_document_with_http_info(, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : The identifier of the feed document. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feed_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '' is set
        if ('' not in params or
                params[''] is None):
            raise ValueError("Missing the required parameter `` when calling `get_feed_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if '' in params:
            path_params['feedDocumentId'] = params['']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feeds/2020-09-04/documents/{feedDocumentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feeds(self, **kwargs):  # noqa: E501
        """get_feeds  # noqa: E501

        Returns feed details for the feeds that match the filters that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feeds(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.
        :param  : A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.
        :param  : The maximum number of feeds to return in a single call.
        :param  : A list of processing statuses used to filter feeds.
        :param  : The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.
        :param  : The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.
        :param  : A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_feeds_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_feeds_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_feeds_with_http_info(self, **kwargs):  # noqa: E501
        """get_feeds  # noqa: E501

        Returns feed details for the feeds that match the filters that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0222 | 10 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_feeds_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.
        :param  : A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.
        :param  : The maximum number of feeds to return in a single call.
        :param  : A list of processing statuses used to filter feeds.
        :param  : The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.
        :param  : The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.
        :param  : A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['', '', '', '', '', '', '']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feeds" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '' in params:
            query_params.append(('feedTypes', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('marketplaceIds', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('pageSize', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('processingStatuses', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('createdSince', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('createdUntil', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('nextToken', params['']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feeds/2020-09-04/feeds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
