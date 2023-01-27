# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=no-self-use

import logging
from typing import Any

from marshmallow import fields, post_load, validates, ValidationError

from azure.ai.ml._schema import NestedField, PatchedSchemaMeta, StringTransformedEnum
from azure.ai.ml._schema._deployment.online.destination_schema import DestinationSchema
from azure.ai.ml._schema._deployment.online.request_logging_schema import RequestLoggingSchema
from azure.ai.ml._schema._deployment.online.payload_request_schema import PayloadRequestSchema
from azure.ai.ml._schema._deployment.online.payload_response_schema import PayloadResponseSchema

from azure.ai.ml.constants._common import RollingRate

module_logger = logging.getLogger(__name__)


class DataCollectorSchema(metaclass=PatchedSchemaMeta):
    request = NestedField(PayloadRequestSchema)
    response = NestedField(PayloadResponseSchema)
    rolling_rate = StringTransformedEnum(
        required=False,
        allowed_values=[ RollingRate.MINUTE, RollingRate.DAY, RollingRate.HOUR],
    )
    destination = NestedField(DestinationSchema)
    sampling_rate = fields.Float()
    request_logging = NestedField(RequestLoggingSchema)

    # pylint: disable=unused-argument,no-self-use
    @validates("sampling_rate")
    def validate_sampling_rate(self, value, **kwargs):
        if value > 1.0 or value < 0.0:
            raise ValidationError("Random Sample Percentage must be an number between 0.0-1.0")

    @post_load
    def make(self, data: Any, **kwargs: Any) -> Any:  # pylint: disable=unused-argument
        from azure.ai.ml.entities._deployment.data_collector import DataCollector

        return DataCollector(**data)
