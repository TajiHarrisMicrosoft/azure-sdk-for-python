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
from ..._serialization import Deserializer, Serializer
from ._configuration import ContainerServiceClientConfiguration
from .operations import (
    AgentPoolsOperations,
    MaintenanceConfigurationsOperations,
    ManagedClustersOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    ResolvePrivateLinkServiceIdOperations,
    SnapshotsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class ContainerServiceClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Container Service Client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerservice.v2021_09_01.aio.operations.Operations
    :ivar managed_clusters: ManagedClustersOperations operations
    :vartype managed_clusters:
     azure.mgmt.containerservice.v2021_09_01.aio.operations.ManagedClustersOperations
    :ivar maintenance_configurations: MaintenanceConfigurationsOperations operations
    :vartype maintenance_configurations:
     azure.mgmt.containerservice.v2021_09_01.aio.operations.MaintenanceConfigurationsOperations
    :ivar agent_pools: AgentPoolsOperations operations
    :vartype agent_pools:
     azure.mgmt.containerservice.v2021_09_01.aio.operations.AgentPoolsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.containerservice.v2021_09_01.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.containerservice.v2021_09_01.aio.operations.PrivateLinkResourcesOperations
    :ivar resolve_private_link_service_id: ResolvePrivateLinkServiceIdOperations operations
    :vartype resolve_private_link_service_id:
     azure.mgmt.containerservice.v2021_09_01.aio.operations.ResolvePrivateLinkServiceIdOperations
    :ivar snapshots: SnapshotsOperations operations
    :vartype snapshots: azure.mgmt.containerservice.v2021_09_01.aio.operations.SnapshotsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2021-09-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ContainerServiceClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize, "2021-09-01")
        self.managed_clusters = ManagedClustersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2021-09-01"
        )
        self.maintenance_configurations = MaintenanceConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2021-09-01"
        )
        self.agent_pools = AgentPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2021-09-01"
        )
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2021-09-01"
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2021-09-01"
        )
        self.resolve_private_link_service_id = ResolvePrivateLinkServiceIdOperations(
            self._client, self._config, self._serialize, self._deserialize, "2021-09-01"
        )
        self.snapshots = SnapshotsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2021-09-01"
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

    async def __aenter__(self) -> "ContainerServiceClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
