# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=no-self-use

import logging
from typing import Any

from marshmallow import fields, post_load

from azure.ai.ml._schema import NestedField, PatchedSchemaMeta, StringTransformedEnum, UnionField, RegistryStr
from azure.ai.ml._schema._deployment.batch.run_settings_schema import RunSettingsSchema
from azure.ai.ml._schema.pipeline.pipeline_component import PipelineComponentFileRefField
from azure.ai.ml.constants._common import JobTypes, AzureMLResourceType

module_logger = logging.getLogger(__name__)


class JobDefinitionSchema(metaclass=PatchedSchemaMeta):
    component_id = fields.Str()
    job = UnionField([RegistryStr(azureml_type=AzureMLResourceType.JOB), PipelineComponentFileRefField()])
    component = UnionField([ RegistryStr(azureml_type=AzureMLResourceType.COMPONENT), PipelineComponentFileRefField(),])
    type = StringTransformedEnum(
        required=True,
        allowed_values=[JobTypes.COMMAND_JOB, JobTypes.PIPELINE_JOB, JobTypes.SWEEP_JOB]
    )
    settings = fields.Dict()


    @post_load
    def make(self, data: Any, **kwargs: Any) -> Any:  # pylint: disable=unused-argument
        from azure.ai.ml.entities._deployment.job_definition import JobDefinition

        return JobDefinition(**data)