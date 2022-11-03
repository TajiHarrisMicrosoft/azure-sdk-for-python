# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import DataShareManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    AccountsOperations,
    ConsumerInvitationsOperations,
    ConsumerSourceDataSetsOperations,
    DataSetMappingsOperations,
    DataSetsOperations,
    EmailRegistrationsOperations,
    InvitationsOperations,
    Operations,
    ProviderShareSubscriptionsOperations,
    ShareSubscriptionsOperations,
    SharesOperations,
    SynchronizationSettingsOperations,
    TriggersOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class DataShareManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Creates a Microsoft.DataShare management client.

    :ivar accounts: AccountsOperations operations
    :vartype accounts: azure.mgmt.datashare.operations.AccountsOperations
    :ivar consumer_invitations: ConsumerInvitationsOperations operations
    :vartype consumer_invitations: azure.mgmt.datashare.operations.ConsumerInvitationsOperations
    :ivar data_sets: DataSetsOperations operations
    :vartype data_sets: azure.mgmt.datashare.operations.DataSetsOperations
    :ivar data_set_mappings: DataSetMappingsOperations operations
    :vartype data_set_mappings: azure.mgmt.datashare.operations.DataSetMappingsOperations
    :ivar email_registrations: EmailRegistrationsOperations operations
    :vartype email_registrations: azure.mgmt.datashare.operations.EmailRegistrationsOperations
    :ivar invitations: InvitationsOperations operations
    :vartype invitations: azure.mgmt.datashare.operations.InvitationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datashare.operations.Operations
    :ivar shares: SharesOperations operations
    :vartype shares: azure.mgmt.datashare.operations.SharesOperations
    :ivar provider_share_subscriptions: ProviderShareSubscriptionsOperations operations
    :vartype provider_share_subscriptions:
     azure.mgmt.datashare.operations.ProviderShareSubscriptionsOperations
    :ivar share_subscriptions: ShareSubscriptionsOperations operations
    :vartype share_subscriptions: azure.mgmt.datashare.operations.ShareSubscriptionsOperations
    :ivar consumer_source_data_sets: ConsumerSourceDataSetsOperations operations
    :vartype consumer_source_data_sets:
     azure.mgmt.datashare.operations.ConsumerSourceDataSetsOperations
    :ivar synchronization_settings: SynchronizationSettingsOperations operations
    :vartype synchronization_settings:
     azure.mgmt.datashare.operations.SynchronizationSettingsOperations
    :ivar triggers: TriggersOperations operations
    :vartype triggers: azure.mgmt.datashare.operations.TriggersOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2020-09-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = DataShareManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.accounts = AccountsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.consumer_invitations = ConsumerInvitationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_sets = DataSetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_set_mappings = DataSetMappingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.email_registrations = EmailRegistrationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.invitations = InvitationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.shares = SharesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.provider_share_subscriptions = ProviderShareSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.share_subscriptions = ShareSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.consumer_source_data_sets = ConsumerSourceDataSetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.synchronization_settings = SynchronizationSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.triggers = TriggersOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DataShareManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
