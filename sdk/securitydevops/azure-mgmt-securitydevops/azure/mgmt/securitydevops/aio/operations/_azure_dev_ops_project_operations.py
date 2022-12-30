# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._azure_dev_ops_project_operations import (
    build_create_or_update_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AzureDevOpsProjectOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.securitydevops.aio.MicrosoftSecurityDevOps`'s
        :attr:`azure_dev_ops_project` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, resource_group_name: str, azure_dev_ops_connector_name: str, azure_dev_ops_org_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.AzureDevOpsProject"]:
        """list.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_dev_ops_connector_name: Name of the AzureDevOps Connector. Required.
        :type azure_dev_ops_connector_name: str
        :param azure_dev_ops_org_name: Name of the AzureDevOps Org. Required.
        :type azure_dev_ops_org_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AzureDevOpsProject or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.securitydevops.models.AzureDevOpsProject]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.AzureDevOpsProjectListResponse] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    azure_dev_ops_connector_name=azure_dev_ops_connector_name,
                    azure_dev_ops_org_name=azure_dev_ops_org_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AzureDevOpsProjectListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SecurityDevOps/azureDevOpsConnectors/{azureDevOpsConnectorName}/orgs/{azureDevOpsOrgName}/projects"
    }

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        **kwargs: Any
    ) -> _models.AzureDevOpsProject:
        """Returns a monitored AzureDevOps Project resource for a given ID.

        Returns a monitored AzureDevOps Project resource for a given ID.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_dev_ops_connector_name: Name of the AzureDevOps Connector. Required.
        :type azure_dev_ops_connector_name: str
        :param azure_dev_ops_org_name: Name of the AzureDevOps Org. Required.
        :type azure_dev_ops_org_name: str
        :param azure_dev_ops_project_name: Name of the AzureDevOps Project. Required.
        :type azure_dev_ops_project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AzureDevOpsProject or the result of cls(response)
        :rtype: ~azure.mgmt.securitydevops.models.AzureDevOpsProject
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

        api_version: Literal["2022-09-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.AzureDevOpsProject] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            azure_dev_ops_connector_name=azure_dev_ops_connector_name,
            azure_dev_ops_org_name=azure_dev_ops_org_name,
            azure_dev_ops_project_name=azure_dev_ops_project_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AzureDevOpsProject", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SecurityDevOps/azureDevOpsConnectors/{azureDevOpsConnectorName}/orgs/{azureDevOpsOrgName}/projects/{azureDevOpsProjectName}"
    }

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        azure_dev_ops_project: Union[_models.AzureDevOpsProject, IO],
        **kwargs: Any
    ) -> _models.AzureDevOpsProject:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureDevOpsProject] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(azure_dev_ops_project, (IO, bytes)):
            _content = azure_dev_ops_project
        else:
            _json = self._serialize.body(azure_dev_ops_project, "AzureDevOpsProject")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            azure_dev_ops_connector_name=azure_dev_ops_connector_name,
            azure_dev_ops_org_name=azure_dev_ops_org_name,
            azure_dev_ops_project_name=azure_dev_ops_project_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_or_update_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("AzureDevOpsProject", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("AzureDevOpsProject", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    _create_or_update_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SecurityDevOps/azureDevOpsConnectors/{azureDevOpsConnectorName}/orgs/{azureDevOpsOrgName}/projects/{azureDevOpsProjectName}"
    }

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        azure_dev_ops_project: _models.AzureDevOpsProject,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureDevOpsProject]:
        """Creates or updates an Azure DevOps Project.

        Creates or updates an Azure DevOps Project.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_dev_ops_connector_name: Name of the AzureDevOps Connector. Required.
        :type azure_dev_ops_connector_name: str
        :param azure_dev_ops_org_name: Name of the AzureDevOps Org. Required.
        :type azure_dev_ops_org_name: str
        :param azure_dev_ops_project_name: Name of the AzureDevOps Project. Required.
        :type azure_dev_ops_project_name: str
        :param azure_dev_ops_project: Azure DevOps Org resource payload. Required.
        :type azure_dev_ops_project: ~azure.mgmt.securitydevops.models.AzureDevOpsProject
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AzureDevOpsProject or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.securitydevops.models.AzureDevOpsProject]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        azure_dev_ops_project: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureDevOpsProject]:
        """Creates or updates an Azure DevOps Project.

        Creates or updates an Azure DevOps Project.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_dev_ops_connector_name: Name of the AzureDevOps Connector. Required.
        :type azure_dev_ops_connector_name: str
        :param azure_dev_ops_org_name: Name of the AzureDevOps Org. Required.
        :type azure_dev_ops_org_name: str
        :param azure_dev_ops_project_name: Name of the AzureDevOps Project. Required.
        :type azure_dev_ops_project_name: str
        :param azure_dev_ops_project: Azure DevOps Org resource payload. Required.
        :type azure_dev_ops_project: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AzureDevOpsProject or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.securitydevops.models.AzureDevOpsProject]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        azure_dev_ops_project: Union[_models.AzureDevOpsProject, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureDevOpsProject]:
        """Creates or updates an Azure DevOps Project.

        Creates or updates an Azure DevOps Project.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_dev_ops_connector_name: Name of the AzureDevOps Connector. Required.
        :type azure_dev_ops_connector_name: str
        :param azure_dev_ops_org_name: Name of the AzureDevOps Org. Required.
        :type azure_dev_ops_org_name: str
        :param azure_dev_ops_project_name: Name of the AzureDevOps Project. Required.
        :type azure_dev_ops_project_name: str
        :param azure_dev_ops_project: Azure DevOps Org resource payload. Is either a model type or a IO
         type. Required.
        :type azure_dev_ops_project: ~azure.mgmt.securitydevops.models.AzureDevOpsProject or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AzureDevOpsProject or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.securitydevops.models.AzureDevOpsProject]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureDevOpsProject] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                azure_dev_ops_connector_name=azure_dev_ops_connector_name,
                azure_dev_ops_org_name=azure_dev_ops_org_name,
                azure_dev_ops_project_name=azure_dev_ops_project_name,
                azure_dev_ops_project=azure_dev_ops_project,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("AzureDevOpsProject", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SecurityDevOps/azureDevOpsConnectors/{azureDevOpsConnectorName}/orgs/{azureDevOpsOrgName}/projects/{azureDevOpsProjectName}"
    }

    async def _update_initial(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        azure_dev_ops_project: Optional[Union[_models.AzureDevOpsProject, IO]] = None,
        **kwargs: Any
    ) -> _models.AzureDevOpsProject:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureDevOpsProject] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(azure_dev_ops_project, (IO, bytes)):
            _content = azure_dev_ops_project
        else:
            if azure_dev_ops_project is not None:
                _json = self._serialize.body(azure_dev_ops_project, "AzureDevOpsProject")
            else:
                _json = None

        request = build_update_request(
            resource_group_name=resource_group_name,
            azure_dev_ops_connector_name=azure_dev_ops_connector_name,
            azure_dev_ops_org_name=azure_dev_ops_org_name,
            azure_dev_ops_project_name=azure_dev_ops_project_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._update_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("AzureDevOpsProject", pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize("AzureDevOpsProject", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    _update_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SecurityDevOps/azureDevOpsConnectors/{azureDevOpsConnectorName}/orgs/{azureDevOpsOrgName}/projects/{azureDevOpsProjectName}"
    }

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        azure_dev_ops_project: Optional[_models.AzureDevOpsProject] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureDevOpsProject]:
        """Update monitored AzureDevOps Project details.

        Update monitored AzureDevOps Project details.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_dev_ops_connector_name: Name of the AzureDevOps Connector. Required.
        :type azure_dev_ops_connector_name: str
        :param azure_dev_ops_org_name: Name of the AzureDevOps Org. Required.
        :type azure_dev_ops_org_name: str
        :param azure_dev_ops_project_name: Name of the AzureDevOps Project. Required.
        :type azure_dev_ops_project_name: str
        :param azure_dev_ops_project: Azure DevOps Project resource payload. Default value is None.
        :type azure_dev_ops_project: ~azure.mgmt.securitydevops.models.AzureDevOpsProject
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AzureDevOpsProject or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.securitydevops.models.AzureDevOpsProject]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        azure_dev_ops_project: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureDevOpsProject]:
        """Update monitored AzureDevOps Project details.

        Update monitored AzureDevOps Project details.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_dev_ops_connector_name: Name of the AzureDevOps Connector. Required.
        :type azure_dev_ops_connector_name: str
        :param azure_dev_ops_org_name: Name of the AzureDevOps Org. Required.
        :type azure_dev_ops_org_name: str
        :param azure_dev_ops_project_name: Name of the AzureDevOps Project. Required.
        :type azure_dev_ops_project_name: str
        :param azure_dev_ops_project: Azure DevOps Project resource payload. Default value is None.
        :type azure_dev_ops_project: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AzureDevOpsProject or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.securitydevops.models.AzureDevOpsProject]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        azure_dev_ops_connector_name: str,
        azure_dev_ops_org_name: str,
        azure_dev_ops_project_name: str,
        azure_dev_ops_project: Optional[Union[_models.AzureDevOpsProject, IO]] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AzureDevOpsProject]:
        """Update monitored AzureDevOps Project details.

        Update monitored AzureDevOps Project details.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_dev_ops_connector_name: Name of the AzureDevOps Connector. Required.
        :type azure_dev_ops_connector_name: str
        :param azure_dev_ops_org_name: Name of the AzureDevOps Org. Required.
        :type azure_dev_ops_org_name: str
        :param azure_dev_ops_project_name: Name of the AzureDevOps Project. Required.
        :type azure_dev_ops_project_name: str
        :param azure_dev_ops_project: Azure DevOps Project resource payload. Is either a model type or
         a IO type. Default value is None.
        :type azure_dev_ops_project: ~azure.mgmt.securitydevops.models.AzureDevOpsProject or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either AzureDevOpsProject or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.securitydevops.models.AzureDevOpsProject]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2022-09-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureDevOpsProject] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                azure_dev_ops_connector_name=azure_dev_ops_connector_name,
                azure_dev_ops_org_name=azure_dev_ops_org_name,
                azure_dev_ops_project_name=azure_dev_ops_project_name,
                azure_dev_ops_project=azure_dev_ops_project,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("AzureDevOpsProject", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SecurityDevOps/azureDevOpsConnectors/{azureDevOpsConnectorName}/orgs/{azureDevOpsOrgName}/projects/{azureDevOpsProjectName}"
    }
