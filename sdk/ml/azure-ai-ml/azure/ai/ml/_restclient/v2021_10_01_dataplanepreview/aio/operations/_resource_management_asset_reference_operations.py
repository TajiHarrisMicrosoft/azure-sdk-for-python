# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._resource_management_asset_reference_operations import build_import_method_request_initial

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ResourceManagementAssetReferenceOperations:
    """ResourceManagementAssetReferenceOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def _import_method_initial(
        self,
        resource_group_name: str,
        registry_name: str,
        body: "_models.ResourceManagementAssetReferenceData",
        **kwargs: Any
    ) -> Optional[Any]:
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[Any]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "2021-10-01-dataplanepreview")  # type: str
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = self._serialize.body(body, "ResourceManagementAssetReferenceData")

        request = build_import_method_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._import_method_initial.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("object", pipeline_response)

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _import_method_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/registries/{registryName}/import"}  # type: ignore

    @distributed_trace_async
    async def begin_import_method(
        self,
        resource_group_name: str,
        registry_name: str,
        body: "_models.ResourceManagementAssetReferenceData",
        **kwargs: Any
    ) -> AsyncLROPoller[Any]:
        """Import the source asset provided in the request into registry.
        The import performs a deep copy of the source asset given in the request into the registry.
        The destination name/version value in ImportSourceAssetReference allows the client to update
        the name/version value after being imported.
        If the destination resource exists, it will be overwritten.

        Import the source asset provided in the request into registry.
        The import performs a deep copy of the source asset given in the request into the registry.
        The destination name/version value in ImportSourceAssetReference allows the client to update
        the name/version value after being imported.
        If the destination resource exists, it will be overwritten.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param registry_name: Name of Azure Machine Learning registry.
        :type registry_name: str
        :param body: Import request contains the source asset reference value and destination version
         value.
        :type body: ~azure.mgmt.machinelearningservices.models.ResourceManagementAssetReferenceData
        :keyword api_version: Api Version. The default value is "2021-10-01-dataplanepreview". Note
         that overriding this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either any or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[any]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop("api_version", "2021-10-01-dataplanepreview")  # type: str
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, azure.core.polling.AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._import_method_initial(
                resource_group_name=resource_group_name,
                registry_name=registry_name,
                body=body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("object", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = AsyncARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_import_method.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/registries/{registryName}/import"}  # type: ignore
