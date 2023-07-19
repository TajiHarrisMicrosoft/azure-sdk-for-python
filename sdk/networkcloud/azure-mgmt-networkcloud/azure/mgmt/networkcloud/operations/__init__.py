# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._bare_metal_machines_operations import BareMetalMachinesOperations
from ._cloud_services_networks_operations import CloudServicesNetworksOperations
from ._cluster_managers_operations import ClusterManagersOperations
from ._clusters_operations import ClustersOperations
from ._kubernetes_clusters_operations import KubernetesClustersOperations
from ._l2_networks_operations import L2NetworksOperations
from ._l3_networks_operations import L3NetworksOperations
from ._rack_skus_operations import RackSkusOperations
from ._racks_operations import RacksOperations
from ._storage_appliances_operations import StorageAppliancesOperations
from ._trunked_networks_operations import TrunkedNetworksOperations
from ._virtual_machines_operations import VirtualMachinesOperations
from ._volumes_operations import VolumesOperations
from ._bare_metal_machine_key_sets_operations import BareMetalMachineKeySetsOperations
from ._bmc_key_sets_operations import BmcKeySetsOperations
from ._metrics_configurations_operations import MetricsConfigurationsOperations
from ._agent_pools_operations import AgentPoolsOperations
from ._consoles_operations import ConsolesOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "BareMetalMachinesOperations",
    "CloudServicesNetworksOperations",
    "ClusterManagersOperations",
    "ClustersOperations",
    "KubernetesClustersOperations",
    "L2NetworksOperations",
    "L3NetworksOperations",
    "RackSkusOperations",
    "RacksOperations",
    "StorageAppliancesOperations",
    "TrunkedNetworksOperations",
    "VirtualMachinesOperations",
    "VolumesOperations",
    "BareMetalMachineKeySetsOperations",
    "BmcKeySetsOperations",
    "MetricsConfigurationsOperations",
    "AgentPoolsOperations",
    "ConsolesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
