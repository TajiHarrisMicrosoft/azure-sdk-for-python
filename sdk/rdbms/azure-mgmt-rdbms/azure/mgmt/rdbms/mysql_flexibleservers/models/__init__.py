# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AdministratorListResult
from ._models_py3 import AzureADAdministrator
from ._models_py3 import Backup
from ._models_py3 import CapabilitiesListResult
from ._models_py3 import CapabilityProperties
from ._models_py3 import Configuration
from ._models_py3 import ConfigurationForBatchUpdate
from ._models_py3 import ConfigurationListForBatchUpdate
from ._models_py3 import ConfigurationListResult
from ._models_py3 import DataEncryption
from ._models_py3 import Database
from ._models_py3 import DatabaseListResult
from ._models_py3 import DelegatedSubnetUsage
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorResponse
from ._models_py3 import FirewallRule
from ._models_py3 import FirewallRuleListResult
from ._models_py3 import GetPrivateDnsZoneSuffixResponse
from ._models_py3 import HighAvailability
from ._models_py3 import Identity
from ._models_py3 import LogFile
from ._models_py3 import LogFileListResult
from ._models_py3 import MaintenanceWindow
from ._models_py3 import NameAvailability
from ._models_py3 import NameAvailabilityRequest
from ._models_py3 import Network
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import Server
from ._models_py3 import ServerBackup
from ._models_py3 import ServerBackupListResult
from ._models_py3 import ServerEditionCapability
from ._models_py3 import ServerForUpdate
from ._models_py3 import ServerListResult
from ._models_py3 import ServerRestartParameter
from ._models_py3 import ServerVersionCapability
from ._models_py3 import Sku
from ._models_py3 import SkuCapability
from ._models_py3 import Storage
from ._models_py3 import StorageEditionCapability
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import VirtualNetworkSubnetUsageParameter
from ._models_py3 import VirtualNetworkSubnetUsageResult

from ._my_sql_management_client_enums import AdministratorName
from ._my_sql_management_client_enums import AdministratorType
from ._my_sql_management_client_enums import ConfigurationSource
from ._my_sql_management_client_enums import CreateMode
from ._my_sql_management_client_enums import CreatedByType
from ._my_sql_management_client_enums import DataEncryptionType
from ._my_sql_management_client_enums import EnableStatusEnum
from ._my_sql_management_client_enums import HighAvailabilityMode
from ._my_sql_management_client_enums import HighAvailabilityState
from ._my_sql_management_client_enums import IsConfigPendingRestart
from ._my_sql_management_client_enums import IsDynamicConfig
from ._my_sql_management_client_enums import IsReadOnly
from ._my_sql_management_client_enums import ReplicationRole
from ._my_sql_management_client_enums import ResetAllToDefault
from ._my_sql_management_client_enums import ServerState
from ._my_sql_management_client_enums import ServerVersion
from ._my_sql_management_client_enums import SkuTier
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AdministratorListResult",
    "AzureADAdministrator",
    "Backup",
    "CapabilitiesListResult",
    "CapabilityProperties",
    "Configuration",
    "ConfigurationForBatchUpdate",
    "ConfigurationListForBatchUpdate",
    "ConfigurationListResult",
    "DataEncryption",
    "Database",
    "DatabaseListResult",
    "DelegatedSubnetUsage",
    "ErrorAdditionalInfo",
    "ErrorResponse",
    "FirewallRule",
    "FirewallRuleListResult",
    "GetPrivateDnsZoneSuffixResponse",
    "HighAvailability",
    "Identity",
    "LogFile",
    "LogFileListResult",
    "MaintenanceWindow",
    "NameAvailability",
    "NameAvailabilityRequest",
    "Network",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "ProxyResource",
    "Resource",
    "Server",
    "ServerBackup",
    "ServerBackupListResult",
    "ServerEditionCapability",
    "ServerForUpdate",
    "ServerListResult",
    "ServerRestartParameter",
    "ServerVersionCapability",
    "Sku",
    "SkuCapability",
    "Storage",
    "StorageEditionCapability",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "VirtualNetworkSubnetUsageParameter",
    "VirtualNetworkSubnetUsageResult",
    "AdministratorName",
    "AdministratorType",
    "ConfigurationSource",
    "CreateMode",
    "CreatedByType",
    "DataEncryptionType",
    "EnableStatusEnum",
    "HighAvailabilityMode",
    "HighAvailabilityState",
    "IsConfigPendingRestart",
    "IsDynamicConfig",
    "IsReadOnly",
    "ReplicationRole",
    "ResetAllToDefault",
    "ServerState",
    "ServerVersion",
    "SkuTier",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
