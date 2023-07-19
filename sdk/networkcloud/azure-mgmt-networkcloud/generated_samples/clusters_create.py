# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.networkcloud import NetworkCloudMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-networkcloud
# USAGE
    python clusters_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkCloudMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="123e4567-e89b-12d3-a456-426655440000",
    )

    response = client.clusters.begin_create_or_update(
        resource_group_name="resourceGroupName",
        cluster_name="clusterName",
        cluster_parameters={
            "extendedLocation": {
                "name": "/subscriptions/123e4567-e89b-12d3-a456-426655440000/resourceGroups/resourceGroupName/providers/Microsoft.ExtendedLocation/customLocations/clusterManagerExtendedLocationName",
                "type": "CustomLocation",
            },
            "location": "location",
            "properties": {
                "aggregatorOrSingleRackDefinition": {
                    "bareMetalMachineConfigurationData": [
                        {
                            "bmcCredentials": {"password": "{password}", "username": "username"},
                            "bmcMacAddress": "AA:BB:CC:DD:EE:FF",
                            "bootMacAddress": "00:BB:CC:DD:EE:FF",
                            "machineDetails": "extraDetails",
                            "machineName": "bmmName1",
                            "rackSlot": 1,
                            "serialNumber": "BM1219XXX",
                        },
                        {
                            "bmcCredentials": {"password": "{password}", "username": "username"},
                            "bmcMacAddress": "AA:BB:CC:DD:EE:00",
                            "bootMacAddress": "00:BB:CC:DD:EE:00",
                            "machineDetails": "extraDetails",
                            "machineName": "bmmName2",
                            "rackSlot": 2,
                            "serialNumber": "BM1219YYY",
                        },
                    ],
                    "networkRackId": "/subscriptions/123e4567-e89b-12d3-a456-426655440000/resourceGroups/resourceGroupName/providers/Microsoft.ManagedNetworkFabric/networkRacks/networkRackName",
                    "rackLocation": "Foo Datacenter, Floor 3, Aisle 9, Rack 2",
                    "rackSerialNumber": "AA1234",
                    "rackSkuId": "/subscriptions/123e4567-e89b-12d3-a456-426655440000/providers/Microsoft.NetworkCloud/rackSkus/rackSkuName",
                    "storageApplianceConfigurationData": [
                        {
                            "adminCredentials": {"password": "{password}", "username": "username"},
                            "rackSlot": 1,
                            "serialNumber": "BM1219XXX",
                            "storageApplianceName": "vmName",
                        }
                    ],
                },
                "analyticsWorkspaceId": "/subscriptions/123e4567-e89b-12d3-a456-426655440000/resourceGroups/resourceGroupName/providers/microsoft.operationalInsights/workspaces/logAnalyticsWorkspaceName",
                "clusterLocation": "Foo Street, 3rd Floor, row 9",
                "clusterServicePrincipal": {
                    "applicationId": "12345678-1234-1234-1234-123456789012",
                    "password": "{password}",
                    "principalId": "00000008-0004-0004-0004-000000000012",
                    "tenantId": "80000000-4000-4000-4000-120000000000",
                },
                "clusterType": "SingleRack",
                "clusterVersion": "1.0.0",
                "computeDeploymentThreshold": {"grouping": "PerCluster", "type": "PercentSuccess", "value": 90},
                "computeRackDefinitions": [
                    {
                        "bareMetalMachineConfigurationData": [
                            {
                                "bmcCredentials": {"password": "{password}", "username": "username"},
                                "bmcMacAddress": "AA:BB:CC:DD:EE:FF",
                                "bootMacAddress": "00:BB:CC:DD:EE:FF",
                                "machineDetails": "extraDetails",
                                "machineName": "bmmName1",
                                "rackSlot": 1,
                                "serialNumber": "BM1219XXX",
                            },
                            {
                                "bmcCredentials": {"password": "{password}", "username": "username"},
                                "bmcMacAddress": "AA:BB:CC:DD:EE:00",
                                "bootMacAddress": "00:BB:CC:DD:EE:00",
                                "machineDetails": "extraDetails",
                                "machineName": "bmmName2",
                                "rackSlot": 2,
                                "serialNumber": "BM1219YYY",
                            },
                        ],
                        "networkRackId": "/subscriptions/123e4567-e89b-12d3-a456-426655440000/resourceGroups/resourceGroupName/providers/Microsoft.ManagedNetworkFabric/networkRacks/networkRackName",
                        "rackLocation": "Foo Datacenter, Floor 3, Aisle 9, Rack 2",
                        "rackSerialNumber": "AA1234",
                        "rackSkuId": "/subscriptions/123e4567-e89b-12d3-a456-426655440000/providers/Microsoft.NetworkCloud/rackSkus/rackSkuName",
                        "storageApplianceConfigurationData": [
                            {
                                "adminCredentials": {"password": "{password}", "username": "username"},
                                "rackSlot": 1,
                                "serialNumber": "BM1219XXX",
                                "storageApplianceName": "vmName",
                            }
                        ],
                    }
                ],
                "managedResourceGroupConfiguration": {"location": "East US", "name": "my-managed-rg"},
                "networkFabricId": "/subscriptions/123e4567-e89b-12d3-a456-426655440000/resourceGroups/resourceGroupName/providers/Microsoft.ManagedNetworkFabric/networkFabrics/fabricName",
            },
            "tags": {"key1": "myvalue1", "key2": "myvalue2"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/networkcloud/resource-manager/Microsoft.NetworkCloud/preview/2023-05-01-preview/examples/Clusters_Create.json
if __name__ == "__main__":
    main()
