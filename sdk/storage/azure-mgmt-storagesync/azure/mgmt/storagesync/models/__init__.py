# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import BackupRequest
from ._models_py3 import CheckNameAvailabilityParameters
from ._models_py3 import CheckNameAvailabilityResult
from ._models_py3 import CloudEndpoint
from ._models_py3 import CloudEndpointAfsShareMetadataCertificatePublicKeys
from ._models_py3 import CloudEndpointArray
from ._models_py3 import CloudEndpointChangeEnumerationActivity
from ._models_py3 import CloudEndpointChangeEnumerationStatus
from ._models_py3 import CloudEndpointCreateParameters
from ._models_py3 import CloudEndpointLastChangeEnumerationStatus
from ._models_py3 import CloudTieringCachePerformance
from ._models_py3 import CloudTieringDatePolicyStatus
from ._models_py3 import CloudTieringFilesNotTiering
from ._models_py3 import CloudTieringLowDiskMode
from ._models_py3 import CloudTieringSpaceSavings
from ._models_py3 import CloudTieringVolumeFreeSpacePolicyStatus
from ._models_py3 import FilesNotTieringError
from ._models_py3 import LocationOperationStatus
from ._models_py3 import OperationDisplayInfo
from ._models_py3 import OperationDisplayResource
from ._models_py3 import OperationEntity
from ._models_py3 import OperationEntityListResult
from ._models_py3 import OperationProperties
from ._models_py3 import OperationResourceMetricSpecification
from ._models_py3 import OperationResourceMetricSpecificationDimension
from ._models_py3 import OperationResourceServiceSpecification
from ._models_py3 import OperationStatus
from ._models_py3 import PostBackupResponse
from ._models_py3 import PostRestoreRequest
from ._models_py3 import PreRestoreRequest
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import RecallActionParameters
from ._models_py3 import RegisteredServer
from ._models_py3 import RegisteredServerArray
from ._models_py3 import RegisteredServerCreateParameters
from ._models_py3 import Resource
from ._models_py3 import ResourcesMoveInfo
from ._models_py3 import RestoreFileSpec
from ._models_py3 import ServerEndpoint
from ._models_py3 import ServerEndpointArray
from ._models_py3 import ServerEndpointBackgroundDataDownloadActivity
from ._models_py3 import ServerEndpointCloudTieringStatus
from ._models_py3 import ServerEndpointCreateParameters
from ._models_py3 import ServerEndpointFilesNotSyncingError
from ._models_py3 import ServerEndpointRecallError
from ._models_py3 import ServerEndpointRecallStatus
from ._models_py3 import ServerEndpointSyncActivityStatus
from ._models_py3 import ServerEndpointSyncSessionStatus
from ._models_py3 import ServerEndpointSyncStatus
from ._models_py3 import ServerEndpointUpdateParameters
from ._models_py3 import StorageSyncApiError
from ._models_py3 import StorageSyncError
from ._models_py3 import StorageSyncErrorDetails
from ._models_py3 import StorageSyncInnerErrorDetails
from ._models_py3 import StorageSyncService
from ._models_py3 import StorageSyncServiceArray
from ._models_py3 import StorageSyncServiceCreateParameters
from ._models_py3 import StorageSyncServiceUpdateParameters
from ._models_py3 import SubscriptionState
from ._models_py3 import SyncGroup
from ._models_py3 import SyncGroupArray
from ._models_py3 import SyncGroupCreateParameters
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import TriggerChangeDetectionParameters
from ._models_py3 import TriggerRolloverRequest
from ._models_py3 import Workflow
from ._models_py3 import WorkflowArray

from ._microsoft_storage_sync_enums import ChangeDetectionMode
from ._microsoft_storage_sync_enums import CloudEndpointChangeEnumerationActivityState
from ._microsoft_storage_sync_enums import CloudEndpointChangeEnumerationTotalCountsState
from ._microsoft_storage_sync_enums import CloudTieringLowDiskModeState
from ._microsoft_storage_sync_enums import CreatedByType
from ._microsoft_storage_sync_enums import FeatureStatus
from ._microsoft_storage_sync_enums import IncomingTrafficPolicy
from ._microsoft_storage_sync_enums import InitialDownloadPolicy
from ._microsoft_storage_sync_enums import InitialUploadPolicy
from ._microsoft_storage_sync_enums import LocalCacheMode
from ._microsoft_storage_sync_enums import NameAvailabilityReason
from ._microsoft_storage_sync_enums import OperationDirection
from ._microsoft_storage_sync_enums import PrivateEndpointConnectionProvisioningState
from ._microsoft_storage_sync_enums import PrivateEndpointServiceConnectionStatus
from ._microsoft_storage_sync_enums import ProgressType
from ._microsoft_storage_sync_enums import Reason
from ._microsoft_storage_sync_enums import RegisteredServerAgentVersionStatus
from ._microsoft_storage_sync_enums import ServerEndpointHealthState
from ._microsoft_storage_sync_enums import ServerEndpointOfflineDataTransferState
from ._microsoft_storage_sync_enums import ServerEndpointSyncActivityState
from ._microsoft_storage_sync_enums import ServerEndpointSyncMode
from ._microsoft_storage_sync_enums import WorkflowStatus
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BackupRequest",
    "CheckNameAvailabilityParameters",
    "CheckNameAvailabilityResult",
    "CloudEndpoint",
    "CloudEndpointAfsShareMetadataCertificatePublicKeys",
    "CloudEndpointArray",
    "CloudEndpointChangeEnumerationActivity",
    "CloudEndpointChangeEnumerationStatus",
    "CloudEndpointCreateParameters",
    "CloudEndpointLastChangeEnumerationStatus",
    "CloudTieringCachePerformance",
    "CloudTieringDatePolicyStatus",
    "CloudTieringFilesNotTiering",
    "CloudTieringLowDiskMode",
    "CloudTieringSpaceSavings",
    "CloudTieringVolumeFreeSpacePolicyStatus",
    "FilesNotTieringError",
    "LocationOperationStatus",
    "OperationDisplayInfo",
    "OperationDisplayResource",
    "OperationEntity",
    "OperationEntityListResult",
    "OperationProperties",
    "OperationResourceMetricSpecification",
    "OperationResourceMetricSpecificationDimension",
    "OperationResourceServiceSpecification",
    "OperationStatus",
    "PostBackupResponse",
    "PostRestoreRequest",
    "PreRestoreRequest",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "ProxyResource",
    "RecallActionParameters",
    "RegisteredServer",
    "RegisteredServerArray",
    "RegisteredServerCreateParameters",
    "Resource",
    "ResourcesMoveInfo",
    "RestoreFileSpec",
    "ServerEndpoint",
    "ServerEndpointArray",
    "ServerEndpointBackgroundDataDownloadActivity",
    "ServerEndpointCloudTieringStatus",
    "ServerEndpointCreateParameters",
    "ServerEndpointFilesNotSyncingError",
    "ServerEndpointRecallError",
    "ServerEndpointRecallStatus",
    "ServerEndpointSyncActivityStatus",
    "ServerEndpointSyncSessionStatus",
    "ServerEndpointSyncStatus",
    "ServerEndpointUpdateParameters",
    "StorageSyncApiError",
    "StorageSyncError",
    "StorageSyncErrorDetails",
    "StorageSyncInnerErrorDetails",
    "StorageSyncService",
    "StorageSyncServiceArray",
    "StorageSyncServiceCreateParameters",
    "StorageSyncServiceUpdateParameters",
    "SubscriptionState",
    "SyncGroup",
    "SyncGroupArray",
    "SyncGroupCreateParameters",
    "SystemData",
    "TrackedResource",
    "TriggerChangeDetectionParameters",
    "TriggerRolloverRequest",
    "Workflow",
    "WorkflowArray",
    "ChangeDetectionMode",
    "CloudEndpointChangeEnumerationActivityState",
    "CloudEndpointChangeEnumerationTotalCountsState",
    "CloudTieringLowDiskModeState",
    "CreatedByType",
    "FeatureStatus",
    "IncomingTrafficPolicy",
    "InitialDownloadPolicy",
    "InitialUploadPolicy",
    "LocalCacheMode",
    "NameAvailabilityReason",
    "OperationDirection",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProgressType",
    "Reason",
    "RegisteredServerAgentVersionStatus",
    "ServerEndpointHealthState",
    "ServerEndpointOfflineDataTransferState",
    "ServerEndpointSyncActivityState",
    "ServerEndpointSyncMode",
    "WorkflowStatus",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
