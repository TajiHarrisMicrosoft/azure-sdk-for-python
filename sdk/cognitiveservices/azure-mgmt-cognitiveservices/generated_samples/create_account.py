# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cognitiveservices
# USAGE
    python create_account.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CognitiveServicesManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    )

    response = client.accounts.begin_create(
        resource_group_name="myResourceGroup",
        account_name="testCreate1",
        account={
            "identity": {"type": "SystemAssigned"},
            "kind": "Emotion",
            "location": "West US",
            "properties": {
                "encryption": {
                    "keySource": "Microsoft.KeyVault",
                    "keyVaultProperties": {
                        "keyName": "KeyName",
                        "keyVaultUri": "https://pltfrmscrts-use-pc-dev.vault.azure.net/",
                        "keyVersion": "891CF236-D241-4738-9462-D506AF493DFA",
                    },
                },
                "userOwnedStorage": [
                    {
                        "resourceId": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount"
                    }
                ],
            },
            "sku": {"name": "S0"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/stable/2023-05-01/examples/CreateAccount.json
if __name__ == "__main__":
    main()
