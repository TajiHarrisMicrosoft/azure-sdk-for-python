# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=unused-argument,no-self-use

import logging
from typing import Any

from marshmallow import fields, post_load
from azure.ai.ml._schema import(
    UnionField,
    ArmVersionedStr,
    RegistryStr,
)
from azure.ai.ml._schema._deployment.batch.job_definition_schema import JobDefinitionSchema
from azure.ai.ml._schema._deployment.deployment import DeploymentSchema
from azure.ai.ml._schema.core.fields import ComputeField, NestedField, StringTransformedEnum
from azure.ai.ml._schema.pipeline.pipeline_component import PipelineComponentFileRefField
from azure.ai.ml.constants._common import AzureMLResourceType
from azure.ai.ml._schema.job_resource_configuration import JobResourceConfigurationSchema
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY
from azure.ai.ml.constants._deployment import BatchDeploymentOutputAction, BatchDeploymentType

from .batch_deployment_settings import BatchRetrySettingsSchema

module_logger = logging.getLogger(__name__)


class BatchDeploymentSchema(DeploymentSchema):
    compute = ComputeField(required=False)
    error_threshold = fields.Int(
        metadata={
            "description": """Error threshold, if the error count for the entire input goes above this value,\r\n
            the batch inference will be aborted. Range is [-1, int.MaxValue].\r\n
            For FileDataset, this value is the count of file failures.\r\n
            For TabularDataset, this value is the count of record failures.\r\n
            If set to -1 (the lower bound), all failures during batch inference will be ignored."""
        }
    )
    retry_settings = NestedField(BatchRetrySettingsSchema)
    mini_batch_size = fields.Int()
    logging_level = fields.Str(
        metadata={
            "description": """A string of the logging level name, which is defined in 'logging'.
            Possible values are 'warning', 'info', and 'debug'."""
        }
    )
    output_action = StringTransformedEnum(
        allowed_values=[
            BatchDeploymentOutputAction.APPEND_ROW,
            BatchDeploymentOutputAction.SUMMARY_ONLY,
        ],
        metadata={"description": "Indicates how batch inferencing will handle output."},
        dump_default=BatchDeploymentOutputAction.APPEND_ROW,
    )
    output_file_name = fields.Str(metadata={"description": "Customized output file name for append_row output action."})
    max_concurrency_per_instance = fields.Int(
        metadata={"description": "Indicates maximum number of parallelism per instance."}
    )
    resources = NestedField(JobResourceConfigurationSchema)
    type = StringTransformedEnum(allowed_values=[BatchDeploymentType.COMPONENT, BatchDeploymentType.MODEL], required=False)

    job_definition = NestedField(JobDefinitionSchema)
    component = UnionField(
        [
            RegistryStr(azureml_type=AzureMLResourceType.COMPONENT),
            ArmVersionedStr(azureml_type=AzureMLResourceType.COMPONENT, allow_default_version=True),
            PipelineComponentFileRefField(),
        ]
    )
    settings = fields.Dict()

    @post_load
    def make(self, data: Any, **kwargs: Any) -> Any:
        from azure.ai.ml.entities import BatchDeployment, ModelBatchDeployment, PipelineComponentBatchDeployment
        import debugpy
        debugpy.connect(('localhost', 5678))
        debugpy.breakpoint()
        try:
            if data["type"]:
                if data["type"] == BatchDeploymentType.COMPONENT:
                    return PipelineComponentBatchDeployment(**data)
                elif data["type"] == BatchDeploymentType.MODEL:
                    return ModelBatchDeployment(base_path=self.context[BASE_PATH_CONTEXT_KEY], **data)
        except Exception as ex:
            raise ex
        # except:
        #     return BatchDeployment(base_path=self.context[BASE_PATH_CONTEXT_KEY], **data)
