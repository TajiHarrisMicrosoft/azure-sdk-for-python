# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.hdinsight import HDInsightManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hdinsight
# USAGE
    python create_hd_insight_cluster_with_custom_network_properties.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HDInsightManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subId",
    )

    response = client.clusters.begin_create(
        resource_group_name="rg1",
        cluster_name="cluster1",
        parameters={
            "properties": {
                "clusterDefinition": {
                    "configurations": {
                        "gateway": {
                            "restAuthCredential.isEnabled": True,
                            "restAuthCredential.password": "**********",
                            "restAuthCredential.username": "admin",
                        }
                    },
                    "kind": "hadoop",
                },
                "clusterVersion": "3.6",
                "computeProfile": {
                    "roles": [
                        {
                            "hardwareProfile": {"vmSize": "standard_d3"},
                            "name": "headnode",
                            "osProfile": {
                                "linuxOperatingSystemProfile": {
                                    "password": "**********",
                                    "sshProfile": {"publicKeys": [{"certificateData": "**********"}]},
                                    "username": "sshuser",
                                }
                            },
                            "targetInstanceCount": 2,
                            "virtualNetworkProfile": {
                                "id": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnetname",
                                "subnet": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnetname/subnets/vnetsubnet",
                            },
                        },
                        {
                            "hardwareProfile": {"vmSize": "standard_d3"},
                            "name": "workernode",
                            "osProfile": {
                                "linuxOperatingSystemProfile": {
                                    "password": "**********",
                                    "sshProfile": {"publicKeys": [{"certificateData": "**********"}]},
                                    "username": "sshuser",
                                }
                            },
                            "targetInstanceCount": 2,
                            "virtualNetworkProfile": {
                                "id": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnetname",
                                "subnet": "/subscriptions/subId/resourceGroups/rg/providers/Microsoft.Network/virtualNetworks/vnetname/subnets/vnetsubnet",
                            },
                        },
                    ]
                },
                "networkProperties": {"privateLink": "Enabled", "resourceProviderConnection": "Outbound"},
                "osType": "Linux",
                "storageProfile": {
                    "storageaccounts": [
                        {
                            "container": "containername",
                            "isDefault": True,
                            "key": "storage account key",
                            "name": "mystorage",
                        }
                    ]
                },
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/hdinsight/resource-manager/Microsoft.HDInsight/stable/2021-06-01/examples/CreateHDInsightClusterWithCustomNetworkProperties.json
if __name__ == "__main__":
    main()
