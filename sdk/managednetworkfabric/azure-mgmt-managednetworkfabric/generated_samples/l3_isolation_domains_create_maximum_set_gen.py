# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.managednetworkfabric import ManagedNetworkFabricMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-managednetworkfabric
# USAGE
    python l3_isolation_domains_create_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagedNetworkFabricMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="subscriptionId",
    )

    response = client.l3_isolation_domains.begin_create(
        resource_group_name="resourceGroupName",
        l3_isolation_domain_name="example-l3domain",
        body={
            "location": "eastus",
            "properties": {
                "aggregateRouteConfiguration": {
                    "ipv4Routes": [{"prefix": "10.0.0.0/24"}],
                    "ipv6Routes": [{"prefix": "10.0.0.1"}],
                },
                "connectedSubnetRoutePolicy": {
                    "exportRoutePolicyId": "/subscriptions/subscriptionId/resourceGroups/resourceGroupName/providers/Microsoft.ManagedNetworkFabric/routePolicies/routePolicyName2"
                },
                "description": "creating L3 isolation domain",
                "networkFabricId": "/subscriptions/xxxxxx/resourceGroups/resourcegroupname/providers/Microsoft.ManagedNetworkFabric/networkFabrics/FabricName",
                "redistributeConnectedSubnets": "True",
                "redistributeStaticRoutes": "False",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/preview/2023-02-01-preview/examples/L3IsolationDomains_Create_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
