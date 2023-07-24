# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.dataprotection import DataProtectionMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-dataprotection
# USAGE
    python put_backup_instance.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataProtectionMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="04cf684a-d41f-4550-9f70-7708a3a2283b",
    )

    response = client.backup_instances.begin_create_or_update(
        resource_group_name="000pikumar",
        vault_name="PratikPrivatePreviewVault1",
        backup_instance_name="testInstance1",
        parameters={
            "properties": {
                "dataSourceInfo": {
                    "datasourceType": "Microsoft.DBforPostgreSQL/servers/databases",
                    "objectType": "Datasource",
                    "resourceID": "/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb",
                    "resourceLocation": "",
                    "resourceName": "testdb",
                    "resourceType": "Microsoft.DBforPostgreSQL/servers/databases",
                    "resourceUri": "",
                },
                "dataSourceSetInfo": {
                    "datasourceType": "Microsoft.DBforPostgreSQL/servers/databases",
                    "objectType": "DatasourceSet",
                    "resourceID": "/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest",
                    "resourceLocation": "",
                    "resourceName": "viveksipgtest",
                    "resourceType": "Microsoft.DBforPostgreSQL/servers",
                    "resourceUri": "",
                },
                "datasourceAuthCredentials": {
                    "objectType": "SecretStoreBasedAuthCredentials",
                    "secretStoreResource": {
                        "secretStoreType": "AzureKeyVault",
                        "uri": "https://samplevault.vault.azure.net/secrets/credentials",
                    },
                },
                "friendlyName": "harshitbi2",
                "objectType": "BackupInstance",
                "policyInfo": {
                    "policyId": "/subscriptions/04cf684a-d41f-4550-9f70-7708a3a2283b/resourceGroups/000pikumar/providers/Microsoft.DataProtection/Backupvaults/PratikPrivatePreviewVault1/backupPolicies/PratikPolicy1",
                    "policyParameters": {
                        "dataStoreParametersList": [
                            {
                                "dataStoreType": "OperationalStore",
                                "objectType": "AzureOperationalStoreParameters",
                                "resourceGroupId": "/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest",
                            }
                        ]
                    },
                },
                "validationType": "ShallowValidation",
            },
            "tags": {"key1": "val1"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/dataprotection/resource-manager/Microsoft.DataProtection/stable/2023-05-01/examples/BackupInstanceOperations/PutBackupInstance.json
if __name__ == "__main__":
    main()
