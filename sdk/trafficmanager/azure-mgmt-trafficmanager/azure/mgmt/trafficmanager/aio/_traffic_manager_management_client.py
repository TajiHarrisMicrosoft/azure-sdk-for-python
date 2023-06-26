# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import TrafficManagerManagementClientConfiguration
from .operations import (
    EndpointsOperations,
    GeographicHierarchiesOperations,
    HeatMapOperations,
    ProfilesOperations,
    TrafficManagerUserMetricsKeysOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class TrafficManagerManagementClient:  # pylint: disable=client-accepts-api-version-keyword
    """TrafficManagerManagementClient.

    :ivar endpoints: EndpointsOperations operations
    :vartype endpoints: azure.mgmt.trafficmanager.aio.operations.EndpointsOperations
    :ivar profiles: ProfilesOperations operations
    :vartype profiles: azure.mgmt.trafficmanager.aio.operations.ProfilesOperations
    :ivar geographic_hierarchies: GeographicHierarchiesOperations operations
    :vartype geographic_hierarchies:
     azure.mgmt.trafficmanager.aio.operations.GeographicHierarchiesOperations
    :ivar heat_map: HeatMapOperations operations
    :vartype heat_map: azure.mgmt.trafficmanager.aio.operations.HeatMapOperations
    :ivar traffic_manager_user_metrics_keys: TrafficManagerUserMetricsKeysOperations operations
    :vartype traffic_manager_user_metrics_keys:
     azure.mgmt.trafficmanager.aio.operations.TrafficManagerUserMetricsKeysOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-04-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = TrafficManagerManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.endpoints = EndpointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.profiles = ProfilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.geographic_hierarchies = GeographicHierarchiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.heat_map = HeatMapOperations(self._client, self._config, self._serialize, self._deserialize)
        self.traffic_manager_user_metrics_keys = TrafficManagerUserMetricsKeysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "TrafficManagerManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
