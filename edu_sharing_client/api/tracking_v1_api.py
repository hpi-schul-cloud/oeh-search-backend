# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from edu_sharing_client.api_client import ApiClient


class TRACKINGV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def track_event(self, repository, event, **kwargs):  # noqa: E501
        """Track a user interaction  # noqa: E501

        Currently limited to video / audio play interactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.track_event(repository, event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str event: type of event to track (required)
        :param str node: node id for which the event is tracked. For some event, this can be null
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.track_event_with_http_info(repository, event, **kwargs)  # noqa: E501
        else:
            (data) = self.track_event_with_http_info(repository, event, **kwargs)  # noqa: E501
            return data

    def track_event_with_http_info(self, repository, event, **kwargs):  # noqa: E501
        """Track a user interaction  # noqa: E501

        Currently limited to video / audio play interactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.track_event_with_http_info(repository, event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repository: ID of repository (or \"-home-\" for home repository) (required)
        :param str event: type of event to track (required)
        :param str node: node id for which the event is tracked. For some event, this can be null
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repository', 'event', 'node']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method track_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repository' is set
        if ('repository' not in params or
                params['repository'] is None):
            raise ValueError("Missing the required parameter `repository` when calling `track_event`")  # noqa: E501
        # verify the required parameter 'event' is set
        if ('event' not in params or
                params['event'] is None):
            raise ValueError("Missing the required parameter `event` when calling `track_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repository' in params:
            path_params['repository'] = params['repository']  # noqa: E501
        if 'event' in params:
            path_params['event'] = params['event']  # noqa: E501

        query_params = []
        if 'node' in params:
            query_params.append(('node', params['node']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/tracking/v1/tracking/{repository}/{event}', 'PUT',
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