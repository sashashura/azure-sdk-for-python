# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AddRemoveIncrementalNamedPartitionScalingMechanism
from ._models_py3 import ApplicationHealthPolicy
from ._models_py3 import ApplicationResource
from ._models_py3 import ApplicationResourceList
from ._models_py3 import ApplicationTypeResource
from ._models_py3 import ApplicationTypeResourceList
from ._models_py3 import ApplicationTypeUpdateParameters
from ._models_py3 import ApplicationTypeVersionResource
from ._models_py3 import ApplicationTypeVersionResourceList
from ._models_py3 import ApplicationTypeVersionUpdateParameters
from ._models_py3 import ApplicationTypeVersionsCleanupPolicy
from ._models_py3 import ApplicationUpdateParameters
from ._models_py3 import ApplicationUpgradePolicy
from ._models_py3 import ApplicationUserAssignedIdentity
from ._models_py3 import AvailableOperationDisplay
from ._models_py3 import AveragePartitionLoadScalingTrigger
from ._models_py3 import AverageServiceLoadScalingTrigger
from ._models_py3 import AzureActiveDirectory
from ._models_py3 import ClientCertificate
from ._models_py3 import EndpointRangeDescription
from ._models_py3 import ErrorModel
from ._models_py3 import ErrorModelError
from ._models_py3 import FrontendConfiguration
from ._models_py3 import IPTag
from ._models_py3 import LoadBalancingRule
from ._models_py3 import LongRunningOperationResult
from ._models_py3 import ManagedAzResiliencyStatus
from ._models_py3 import ManagedCluster
from ._models_py3 import ManagedClusterCodeVersionResult
from ._models_py3 import ManagedClusterListResult
from ._models_py3 import ManagedClusterUpdateParameters
from ._models_py3 import ManagedIdentity
from ._models_py3 import ManagedProxyResource
from ._models_py3 import ManagedVMSize
from ._models_py3 import ManagedVMSizesResult
from ._models_py3 import NamedPartitionScheme
from ._models_py3 import NetworkSecurityRule
from ._models_py3 import NodeType
from ._models_py3 import NodeTypeActionParameters
from ._models_py3 import NodeTypeAvailableSku
from ._models_py3 import NodeTypeListResult
from ._models_py3 import NodeTypeListSkuResult
from ._models_py3 import NodeTypeSku
from ._models_py3 import NodeTypeSkuCapacity
from ._models_py3 import NodeTypeSupportedSku
from ._models_py3 import NodeTypeUpdateParameters
from ._models_py3 import OperationListResult
from ._models_py3 import OperationResult
from ._models_py3 import Partition
from ._models_py3 import PartitionInstanceCountScaleMechanism
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import ResourceAzStatus
from ._models_py3 import RollingUpgradeMonitoringPolicy
from ._models_py3 import ScalingMechanism
from ._models_py3 import ScalingPolicy
from ._models_py3 import ScalingTrigger
from ._models_py3 import ServiceCorrelation
from ._models_py3 import ServiceEndpoint
from ._models_py3 import ServiceLoadMetric
from ._models_py3 import ServicePlacementInvalidDomainPolicy
from ._models_py3 import ServicePlacementNonPartiallyPlaceServicePolicy
from ._models_py3 import ServicePlacementPolicy
from ._models_py3 import ServicePlacementPreferPrimaryDomainPolicy
from ._models_py3 import ServicePlacementRequireDomainDistributionPolicy
from ._models_py3 import ServicePlacementRequiredDomainPolicy
from ._models_py3 import ServiceResource
from ._models_py3 import ServiceResourceList
from ._models_py3 import ServiceResourceProperties
from ._models_py3 import ServiceResourcePropertiesBase
from ._models_py3 import ServiceTypeHealthPolicy
from ._models_py3 import ServiceUpdateParameters
from ._models_py3 import SettingsParameterDescription
from ._models_py3 import SettingsSectionDescription
from ._models_py3 import SingletonPartitionScheme
from ._models_py3 import Sku
from ._models_py3 import StatefulServiceProperties
from ._models_py3 import StatelessServiceProperties
from ._models_py3 import SubResource
from ._models_py3 import Subnet
from ._models_py3 import SystemData
from ._models_py3 import UniformInt64RangePartitionScheme
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import VMSSExtension
from ._models_py3 import VMSize
from ._models_py3 import VaultCertificate
from ._models_py3 import VaultSecretGroup
from ._models_py3 import VmManagedIdentity
from ._models_py3 import VmssDataDisk

from ._service_fabric_managed_clusters_management_client_enums import Access
from ._service_fabric_managed_clusters_management_client_enums import ClusterState
from ._service_fabric_managed_clusters_management_client_enums import ClusterUpgradeCadence
from ._service_fabric_managed_clusters_management_client_enums import ClusterUpgradeMode
from ._service_fabric_managed_clusters_management_client_enums import Direction
from ._service_fabric_managed_clusters_management_client_enums import DiskType
from ._service_fabric_managed_clusters_management_client_enums import EvictionPolicyType
from ._service_fabric_managed_clusters_management_client_enums import FailureAction
from ._service_fabric_managed_clusters_management_client_enums import IPAddressType
from ._service_fabric_managed_clusters_management_client_enums import ManagedClusterAddOnFeature
from ._service_fabric_managed_clusters_management_client_enums import ManagedClusterVersionEnvironment
from ._service_fabric_managed_clusters_management_client_enums import ManagedIdentityType
from ._service_fabric_managed_clusters_management_client_enums import ManagedResourceProvisioningState
from ._service_fabric_managed_clusters_management_client_enums import MoveCost
from ._service_fabric_managed_clusters_management_client_enums import NodeTypeSkuScaleType
from ._service_fabric_managed_clusters_management_client_enums import NsgProtocol
from ._service_fabric_managed_clusters_management_client_enums import OsType
from ._service_fabric_managed_clusters_management_client_enums import PartitionScheme
from ._service_fabric_managed_clusters_management_client_enums import PrivateEndpointNetworkPolicies
from ._service_fabric_managed_clusters_management_client_enums import PrivateLinkServiceNetworkPolicies
from ._service_fabric_managed_clusters_management_client_enums import ProbeProtocol
from ._service_fabric_managed_clusters_management_client_enums import Protocol
from ._service_fabric_managed_clusters_management_client_enums import RollingUpgradeMode
from ._service_fabric_managed_clusters_management_client_enums import ServiceCorrelationScheme
from ._service_fabric_managed_clusters_management_client_enums import ServiceKind
from ._service_fabric_managed_clusters_management_client_enums import ServiceLoadMetricWeight
from ._service_fabric_managed_clusters_management_client_enums import ServicePackageActivationMode
from ._service_fabric_managed_clusters_management_client_enums import ServicePlacementPolicyType
from ._service_fabric_managed_clusters_management_client_enums import ServiceScalingMechanismKind
from ._service_fabric_managed_clusters_management_client_enums import ServiceScalingTriggerKind
from ._service_fabric_managed_clusters_management_client_enums import SkuName
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AddRemoveIncrementalNamedPartitionScalingMechanism",
    "ApplicationHealthPolicy",
    "ApplicationResource",
    "ApplicationResourceList",
    "ApplicationTypeResource",
    "ApplicationTypeResourceList",
    "ApplicationTypeUpdateParameters",
    "ApplicationTypeVersionResource",
    "ApplicationTypeVersionResourceList",
    "ApplicationTypeVersionUpdateParameters",
    "ApplicationTypeVersionsCleanupPolicy",
    "ApplicationUpdateParameters",
    "ApplicationUpgradePolicy",
    "ApplicationUserAssignedIdentity",
    "AvailableOperationDisplay",
    "AveragePartitionLoadScalingTrigger",
    "AverageServiceLoadScalingTrigger",
    "AzureActiveDirectory",
    "ClientCertificate",
    "EndpointRangeDescription",
    "ErrorModel",
    "ErrorModelError",
    "FrontendConfiguration",
    "IPTag",
    "LoadBalancingRule",
    "LongRunningOperationResult",
    "ManagedAzResiliencyStatus",
    "ManagedCluster",
    "ManagedClusterCodeVersionResult",
    "ManagedClusterListResult",
    "ManagedClusterUpdateParameters",
    "ManagedIdentity",
    "ManagedProxyResource",
    "ManagedVMSize",
    "ManagedVMSizesResult",
    "NamedPartitionScheme",
    "NetworkSecurityRule",
    "NodeType",
    "NodeTypeActionParameters",
    "NodeTypeAvailableSku",
    "NodeTypeListResult",
    "NodeTypeListSkuResult",
    "NodeTypeSku",
    "NodeTypeSkuCapacity",
    "NodeTypeSupportedSku",
    "NodeTypeUpdateParameters",
    "OperationListResult",
    "OperationResult",
    "Partition",
    "PartitionInstanceCountScaleMechanism",
    "ProxyResource",
    "Resource",
    "ResourceAzStatus",
    "RollingUpgradeMonitoringPolicy",
    "ScalingMechanism",
    "ScalingPolicy",
    "ScalingTrigger",
    "ServiceCorrelation",
    "ServiceEndpoint",
    "ServiceLoadMetric",
    "ServicePlacementInvalidDomainPolicy",
    "ServicePlacementNonPartiallyPlaceServicePolicy",
    "ServicePlacementPolicy",
    "ServicePlacementPreferPrimaryDomainPolicy",
    "ServicePlacementRequireDomainDistributionPolicy",
    "ServicePlacementRequiredDomainPolicy",
    "ServiceResource",
    "ServiceResourceList",
    "ServiceResourceProperties",
    "ServiceResourcePropertiesBase",
    "ServiceTypeHealthPolicy",
    "ServiceUpdateParameters",
    "SettingsParameterDescription",
    "SettingsSectionDescription",
    "SingletonPartitionScheme",
    "Sku",
    "StatefulServiceProperties",
    "StatelessServiceProperties",
    "SubResource",
    "Subnet",
    "SystemData",
    "UniformInt64RangePartitionScheme",
    "UserAssignedIdentity",
    "VMSSExtension",
    "VMSize",
    "VaultCertificate",
    "VaultSecretGroup",
    "VmManagedIdentity",
    "VmssDataDisk",
    "Access",
    "ClusterState",
    "ClusterUpgradeCadence",
    "ClusterUpgradeMode",
    "Direction",
    "DiskType",
    "EvictionPolicyType",
    "FailureAction",
    "IPAddressType",
    "ManagedClusterAddOnFeature",
    "ManagedClusterVersionEnvironment",
    "ManagedIdentityType",
    "ManagedResourceProvisioningState",
    "MoveCost",
    "NodeTypeSkuScaleType",
    "NsgProtocol",
    "OsType",
    "PartitionScheme",
    "PrivateEndpointNetworkPolicies",
    "PrivateLinkServiceNetworkPolicies",
    "ProbeProtocol",
    "Protocol",
    "RollingUpgradeMode",
    "ServiceCorrelationScheme",
    "ServiceKind",
    "ServiceLoadMetricWeight",
    "ServicePackageActivationMode",
    "ServicePlacementPolicyType",
    "ServiceScalingMechanismKind",
    "ServiceScalingTriggerKind",
    "SkuName",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
