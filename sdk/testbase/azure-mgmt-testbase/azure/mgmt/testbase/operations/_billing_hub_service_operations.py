# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_free_hour_balance_request(
    resource_group_name: str, test_base_account_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-04-01-preview")
    )  # type: Literal["2022-04-01-preview"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/getFreeHourBalance",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "testBaseAccountName": _SERIALIZER.url("test_base_account_name", test_base_account_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_usage_request(
    resource_group_name: str, test_base_account_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-04-01-preview")
    )  # type: Literal["2022-04-01-preview"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/getUsage",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "testBaseAccountName": _SERIALIZER.url("test_base_account_name", test_base_account_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class BillingHubServiceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.testbase.TestBase`'s
        :attr:`billing_hub_service` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_free_hour_balance(
        self, resource_group_name: str, test_base_account_name: str, **kwargs: Any
    ) -> _models.BillingHubGetFreeHourBalanceResponse:
        """get_free_hour_balance.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BillingHubGetFreeHourBalanceResponse or the result of cls(response)
        :rtype: ~azure.mgmt.testbase.models.BillingHubGetFreeHourBalanceResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-04-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BillingHubGetFreeHourBalanceResponse]

        request = build_get_free_hour_balance_request(
            resource_group_name=resource_group_name,
            test_base_account_name=test_base_account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_free_hour_balance.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("BillingHubGetFreeHourBalanceResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_free_hour_balance.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/getFreeHourBalance"}  # type: ignore

    @overload
    def get_usage(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        get_usage_request: Optional[_models.BillingHubGetUsageRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.BillingHubGetUsageResponse:
        """get_usage.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :param get_usage_request: Default value is None.
        :type get_usage_request: ~azure.mgmt.testbase.models.BillingHubGetUsageRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BillingHubGetUsageResponse or the result of cls(response)
        :rtype: ~azure.mgmt.testbase.models.BillingHubGetUsageResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def get_usage(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        get_usage_request: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.BillingHubGetUsageResponse:
        """get_usage.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :param get_usage_request: Default value is None.
        :type get_usage_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BillingHubGetUsageResponse or the result of cls(response)
        :rtype: ~azure.mgmt.testbase.models.BillingHubGetUsageResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def get_usage(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        get_usage_request: Optional[Union[_models.BillingHubGetUsageRequest, IO]] = None,
        **kwargs: Any
    ) -> _models.BillingHubGetUsageResponse:
        """get_usage.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :param get_usage_request: Is either a model type or a IO type. Default value is None.
        :type get_usage_request: ~azure.mgmt.testbase.models.BillingHubGetUsageRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BillingHubGetUsageResponse or the result of cls(response)
        :rtype: ~azure.mgmt.testbase.models.BillingHubGetUsageResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-04-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BillingHubGetUsageResponse]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(get_usage_request, (IO, bytes)):
            _content = get_usage_request
        else:
            if get_usage_request is not None:
                _json = self._serialize.body(get_usage_request, "BillingHubGetUsageRequest")
            else:
                _json = None

        request = build_get_usage_request(
            resource_group_name=resource_group_name,
            test_base_account_name=test_base_account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.get_usage.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("BillingHubGetUsageResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_usage.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/getUsage"}  # type: ignore
