# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from azure.ai.ml._restclient.v2020_09_01_dataplanepreview.models import BatchJobResource
from typing import Any, Dict, Optional, Union
from azure.ai.ml.entities import ComputeConfiguration

class BatchJob(object):
    """Batch jobs that are created with batch deployments/endpoints invocation.

    This class shouldn't be instantiated directly. Instead, it is used as the return type of batch deployment/endpoint
    invocation and job listing.
    """

    def __init__(
        self,
        *,
        compute: Optional[ComputeConfiguration] = None,
        dataset: Optional["InferenceDataInputBase"] = None,
        description: Optional[str] = None,
        error_threshold: Optional[int] = None,
        input_data: Optional[Dict[str, "JobInput"]] = None,
        logging_level: Optional[Union[str, "BatchLoggingLevel"]] = None,
        max_concurrency_per_instance: Optional[int] = None,
        mini_batch_size: Optional[int] = None,
        name: Optional[str] = None,
        output_data: Optional[Dict[str, "JobOutputV2"]] = None,
        output_dataset: Optional["DataVersion"] = None,
        output_file_name: Optional[str] = None,
        partition_keys: Optional[List[str]] = None,
        properties: Optional[Dict[str, str]] = None,
        retry_settings: Optional["BatchRetrySettings"] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs       
        ):
        self.id = kwargs.get("id", None)
        self.name = kwargs.get("name", None)
        self.type = kwargs.get("type", None)
        self.status = kwargs.get("status", None)

    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "status": self.status,
        }

    @classmethod
    def _from_rest_object(cls, obj: BatchJobResource) -> "BatchJob":
        return cls(
            id=obj.id,
            name=obj.name,
            type=obj.type,
            status=obj.properties.status,
        )
