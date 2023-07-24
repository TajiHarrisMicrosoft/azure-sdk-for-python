# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.iotfirmwaredefense import IoTFirmwareDefenseMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-iotfirmwaredefense
# USAGE
    python firmware_generate_crypto_certificate_summary_minimum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = IoTFirmwareDefenseMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="C589E84A-5C11-4A25-9CF9-4E9C2F1EBFCA",
    )

    response = client.firmware.generate_crypto_certificate_summary(
        resource_group_name="rgworkspaces-firmwares",
        workspace_name="j5QE_",
        firmware_id="wujtpcgypfpqseyrsebolarkspy",
    )
    print(response)


# x-ms-original-file: specification/fist/resource-manager/Microsoft.IoTFirmwareDefense/preview/2023-02-08-preview/examples/Firmware_GenerateCryptoCertificateSummary_MinimumSet_Gen.json
if __name__ == "__main__":
    main()
