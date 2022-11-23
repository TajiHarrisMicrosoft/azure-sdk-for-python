# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.desktopvirtualization import DesktopVirtualizationMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-desktopvirtualization
# USAGE
    python host_pool_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DesktopVirtualizationMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="daefabc0-95b4-48b3-b645-8a753a63c4fa",
    )

    response = client.host_pools.create_or_update(
        resource_group_name="resourceGroup1",
        host_pool_name="hostPool1",
        host_pool={
            "location": "centralus",
            "properties": {
                "agentUpdate": {
                    "maintenanceWindowTimeZone": "Alaskan Standard Time",
                    "maintenanceWindows": [{"dayOfWeek": "Friday", "hour": 7}, {"dayOfWeek": "Saturday", "hour": 8}],
                    "type": "Scheduled",
                    "useSessionHostLocalTime": False,
                },
                "customRdpProperty": None,
                "description": "des1",
                "friendlyName": "friendly",
                "hostPoolType": "Pooled",
                "loadBalancerType": "BreadthFirst",
                "maxSessionLimit": 999999,
                "personalDesktopAssignmentType": "Automatic",
                "preferredAppGroupType": "Desktop",
                "registrationInfo": {
                    "expirationTime": "2020-10-01T14:01:54.9571247Z",
                    "registrationTokenOperation": "Update",
                },
                "ssoClientId": "client",
                "ssoClientSecretKeyVaultPath": "https://keyvault/secret",
                "ssoSecretType": "SharedKey",
                "ssoadfsAuthority": "https://adfs",
                "startVMOnConnect": False,
                "vmTemplate": "{json:json}",
            },
            "tags": {"tag1": "value1", "tag2": "value2"},
        },
    )
    print(response)


# x-ms-original-file: specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/stable/2022-09-09/examples/HostPool_Create.json
if __name__ == "__main__":
    main()
