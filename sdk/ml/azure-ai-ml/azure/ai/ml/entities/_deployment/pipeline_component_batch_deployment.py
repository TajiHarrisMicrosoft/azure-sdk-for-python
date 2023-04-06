# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import Any, Dict, Optional, Union

from azure.ai.ml.entities._component.component import Component
from azure.ai.ml.entities._deployment.deployment_settings import BatchRetrySettings
from azure.ai.ml.entities import BatchDeployment, PipelineComponent
from azure.ai.ml._utils._experimental import experimental
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY
from azure.ai.ml._restclient.v2023_04_01_preview.models import BatchPipelineComponentDeploymentConfiguration, IdAssetReference, BatchDeploymentProperties, BatchDeployment as RestBatchDeployment

class PipelineComponentBatchDeployment(BatchDeployment):
    """Job Definition entity.

    :param type: Job definition type. Allowed value is: pipeline
    :type type: str
    :param name: Job name
    :type name: str
    :param job: Job definition
    :type job: Union[Job, str]
    :param component: Component definition
    :type component: Union[Component, str]
    :param settings: Job settings
    :type settings: Dict[str, Any]
    :param description: Job description.
    :type description: str
    :param tags: Job tags
    :type tags: Dict[str, Any]
    """

    def __init__(
        self,
        *,
        name: Optional[str],
        endpoint_name: Optional[str] = None,
        component: Optional[Union[Component, str]] = None,
        settings: Optional[Dict[str,str]] = None,
        **kwargs,  # pylint: disable=unused-argument
    ):  
        super().__init__(
            endpoint_name=endpoint_name,
            name=name,
            **kwargs
        )
        self.component = component
        self.settings = settings

    def _to_rest_object(self, location: str) -> "RestBatchDeployment": 
        if type(self.component) is PipelineComponent:
            id_asset_ref = IdAssetReference(
                asset_id=self.component.id
            )
            batch_pipeline_config = BatchPipelineComponentDeploymentConfiguration(
                settings=self.settings,
                tags=self.component.tags,
                description=self.component.description,
                component_id=id_asset_ref
            )
            return RestBatchDeployment(
                location=location,
                properties=BatchDeploymentProperties(deployment_configuration=batch_pipeline_config)
            )
