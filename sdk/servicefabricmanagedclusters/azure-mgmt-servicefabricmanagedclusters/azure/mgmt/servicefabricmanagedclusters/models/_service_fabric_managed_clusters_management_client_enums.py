# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Access(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The network traffic is allowed or denied.
    """

    ALLOW = "allow"
    DENY = "deny"

class ClusterState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the cluster.
    """

    #: Indicates that the cluster resource is created and the resource provider is waiting for Service
    #: Fabric VM extension to boot up and report to it.
    WAITING_FOR_NODES = "WaitingForNodes"
    #: Indicates that the Service Fabric runtime is being installed on the VMs. Cluster resource will
    #: be in this state until the cluster boots up and system services are up.
    DEPLOYING = "Deploying"
    #: Indicates that the cluster is upgrading to establishes the cluster version. This upgrade is
    #: automatically initiated when the cluster boots up for the first time.
    BASELINE_UPGRADE = "BaselineUpgrade"
    #: Indicates that the cluster is being upgraded with the user provided configuration.
    UPGRADING = "Upgrading"
    #: Indicates that the last upgrade for the cluster has failed.
    UPGRADE_FAILED = "UpgradeFailed"
    #: Indicates that the cluster is in a stable state.
    READY = "Ready"

class ClusterUpgradeCadence(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates when new cluster runtime version upgrades will be applied after they are released. By
    default is Wave0.
    """

    #: Cluster upgrade starts immediately after a new version is rolled out. Recommended for Test/Dev
    #: clusters.
    WAVE0 = "Wave0"
    #: Cluster upgrade starts 7 days after a new version is rolled out. Recommended for Pre-prod
    #: clusters.
    WAVE1 = "Wave1"
    #: Cluster upgrade starts 14 days after a new version is rolled out. Recommended for Production
    #: clusters.
    WAVE2 = "Wave2"

class ClusterUpgradeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The upgrade mode of the cluster when new Service Fabric runtime version is available.
    """

    #: The cluster will be automatically upgraded to the latest Service Fabric runtime version,
    #: **clusterUpgradeCadence** will determine when the upgrade starts after the new version becomes
    #: available.
    AUTOMATIC = "Automatic"
    #: The cluster will not be automatically upgraded to the latest Service Fabric runtime version.
    #: The cluster is upgraded by setting the **clusterCodeVersion** property in the cluster resource.
    MANUAL = "Manual"

class Direction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Network security rule direction.
    """

    INBOUND = "inbound"
    OUTBOUND = "outbound"

class DiskType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Managed data disk type. IOPS and throughput are given by the disk size, to see more information
    go to https://docs.microsoft.com/en-us/azure/virtual-machines/disks-types.
    """

    #: Standard HDD locally redundant storage. Best for backup, non-critical, and infrequent access.
    STANDARD_LRS = "Standard_LRS"
    #: Standard SSD locally redundant storage. Best for web servers, lightly used enterprise
    #: applications and dev/test.
    STANDARD_SSD_LRS = "StandardSSD_LRS"
    #: Premium SSD locally redundant storage. Best for production and performance sensitive workloads.
    PREMIUM_LRS = "Premium_LRS"

class FailureAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The compensating action to perform when a Monitored upgrade encounters monitoring policy or
    health policy violations. Invalid indicates the failure action is invalid. Rollback specifies
    that the upgrade will start rolling back automatically. Manual indicates that the upgrade will
    switch to UnmonitoredManual upgrade mode.
    """

    #: Indicates that a rollback of the upgrade will be performed by Service Fabric if the upgrade
    #: fails.
    ROLLBACK = "Rollback"
    #: Indicates that a manual repair will need to be performed by the administrator if the upgrade
    #: fails. Service Fabric will not proceed to the next upgrade domain automatically.
    MANUAL = "Manual"

class ManagedClusterAddOnFeature(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Available cluster add-on features
    """

    DNS_SERVICE = "DnsService"
    BACKUP_RESTORE_SERVICE = "BackupRestoreService"
    RESOURCE_MONITOR_SERVICE = "ResourceMonitorService"

class ManagedIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of managed identity for the resource.
    """

    #: Indicates that no identity is associated with the resource.
    NONE = "None"
    #: Indicates that system assigned identity is associated with the resource.
    SYSTEM_ASSIGNED = "SystemAssigned"
    #: Indicates that user assigned identity is associated with the resource.
    USER_ASSIGNED = "UserAssigned"
    #: Indicates that both system assigned and user assigned identity are associated with the
    #: resource.
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"

class ManagedResourceProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the managed resource.
    """

    NONE = "None"
    CREATING = "Creating"
    CREATED = "Created"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETING = "Deleting"
    DELETED = "Deleted"
    OTHER = "Other"

class MoveCost(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the move cost for the service.
    """

    #: Zero move cost. This value is zero.
    ZERO = "Zero"
    #: Specifies the move cost of the service as Low. The value is 1.
    LOW = "Low"
    #: Specifies the move cost of the service as Medium. The value is 2.
    MEDIUM = "Medium"
    #: Specifies the move cost of the service as High. The value is 3.
    HIGH = "High"

class NsgProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Network protocol this rule applies to.
    """

    HTTP = "http"
    HTTPS = "https"
    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"
    AH = "ah"
    ESP = "esp"

class PartitionScheme(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates the ways that a service can be partitioned.
    """

    #: Indicates that the partition is based on string names, and is a SingletonPartitionScheme
    #: object, The value is 0.
    SINGLETON = "Singleton"
    #: Indicates that the partition is based on Int64 key ranges, and is a
    #: UniformInt64RangePartitionScheme object. The value is 1.
    UNIFORM_INT64_RANGE = "UniformInt64Range"
    #: Indicates that the partition is based on string names, and is a NamedPartitionScheme object.
    #: The value is 2.
    NAMED = "Named"

class ProbeProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """the reference to the load balancer probe used by the load balancing rule.
    """

    TCP = "tcp"
    HTTP = "http"
    HTTPS = "https"

class Protocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reference to the transport protocol used by the load balancing rule.
    """

    TCP = "tcp"
    UDP = "udp"

class RollingUpgradeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The mode used to monitor health during a rolling upgrade. The values are Monitored, and
    UnmonitoredAuto.
    """

    #: The upgrade will stop after completing each upgrade domain and automatically monitor health
    #: before proceeding. The value is 0.
    MONITORED = "Monitored"
    #: The upgrade will proceed automatically without performing any health monitoring. The value is
    #: 1.
    UNMONITORED_AUTO = "UnmonitoredAuto"

class ServiceCorrelationScheme(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The service correlation scheme.
    """

    #: Aligned affinity ensures that the primaries of the partitions of the affinitized services are
    #: collocated on the same nodes. This is the default and is the same as selecting the Affinity
    #: scheme. The value is 0.
    ALIGNED_AFFINITY = "AlignedAffinity"
    #: Non-Aligned affinity guarantees that all replicas of each service will be placed on the same
    #: nodes. Unlike Aligned Affinity, this does not guarantee that replicas of particular role will
    #: be collocated. The value is 1.
    NON_ALIGNED_AFFINITY = "NonAlignedAffinity"

class ServiceKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of service (Stateless or Stateful).
    """

    #: Does not use Service Fabric to make its state highly available or reliable. The value is 0.
    STATELESS = "Stateless"
    #: Uses Service Fabric to make its state or part of its state highly available and reliable. The
    #: value is 1.
    STATEFUL = "Stateful"

class ServiceLoadMetricWeight(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Determines the metric weight relative to the other metrics that are configured for this
    service. During runtime, if two metrics end up in conflict, the Cluster Resource Manager
    prefers the metric with the higher weight.
    """

    #: Disables resource balancing for this metric. This value is zero.
    ZERO = "Zero"
    #: Specifies the metric weight of the service load as Low. The value is 1.
    LOW = "Low"
    #: Specifies the metric weight of the service load as Medium. The value is 2.
    MEDIUM = "Medium"
    #: Specifies the metric weight of the service load as High. The value is 3.
    HIGH = "High"

class ServicePackageActivationMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The activation Mode of the service package
    """

    #: Indicates the application package activation mode will use shared process.
    SHARED_PROCESS = "SharedProcess"
    #: Indicates the application package activation mode will use exclusive process.
    EXCLUSIVE_PROCESS = "ExclusiveProcess"

class ServicePlacementPolicyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of placement policy for a service fabric service. Following are the possible values.
    """

    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementInvalidDomainPolicyDescription, which indicates that a particular fault or
    #: upgrade domain cannot be used for placement of this service. The value is 0.
    INVALID_DOMAIN = "InvalidDomain"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementRequireDomainDistributionPolicyDescription indicating that the replicas of the
    #: service must be placed in a specific domain. The value is 1.
    REQUIRED_DOMAIN = "RequiredDomain"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementPreferPrimaryDomainPolicyDescription, which indicates that if possible the
    #: Primary replica for the partitions of the service should be located in a particular domain as
    #: an optimization. The value is 2.
    PREFERRED_PRIMARY_DOMAIN = "PreferredPrimaryDomain"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementRequireDomainDistributionPolicyDescription, indicating that the system will
    #: disallow placement of any two replicas from the same partition in the same domain at any time.
    #: The value is 3.
    REQUIRED_DOMAIN_DISTRIBUTION = "RequiredDomainDistribution"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementNonPartiallyPlaceServicePolicyDescription, which indicates that if possible all
    #: replicas of a particular partition of the service should be placed atomically. The value is 4.
    NON_PARTIALLY_PLACE_SERVICE = "NonPartiallyPlaceService"

class ServiceScalingMechanismKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates the ways that a service can be partitioned.
    """

    #: Represents a scaling mechanism for adding or removing instances of stateless service partition.
    #: The value is 0.
    SCALE_PARTITION_INSTANCE_COUNT = "ScalePartitionInstanceCount"
    #: Represents a scaling mechanism for adding or removing named partitions of a stateless service.
    #: The value is 1.
    ADD_REMOVE_INCREMENTAL_NAMED_PARTITION = "AddRemoveIncrementalNamedPartition"

class ServiceScalingTriggerKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates the ways that a service can be partitioned.
    """

    #: Represents a scaling trigger related to an average load of a metric/resource of a partition.
    #: The value is 0.
    AVERAGE_PARTITION_LOAD = "AveragePartitionLoad"
    #: Represents a scaling policy related to an average load of a metric/resource of a service. The
    #: value is 1.
    AVERAGE_SERVICE_LOAD = "AverageServiceLoad"

class SkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Sku Name.
    """

    #: Basic requires a minimum of 3 nodes and allows only 1 node type.
    BASIC = "Basic"
    #: Requires a minimum of 5 nodes and allows 1 or more node type.
    STANDARD = "Standard"
