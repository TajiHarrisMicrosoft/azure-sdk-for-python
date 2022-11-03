# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import functools
import os
from typing import Optional, Dict

from azure.core.pipeline.transport import HttpRequest

from .._constants import EnvironmentVariables
from .._internal.managed_identity_base import ManagedIdentityBase
from .._internal.managed_identity_client import ManagedIdentityClient


class AppServiceCredential(ManagedIdentityBase):
    def get_client(self, **kwargs) -> Optional[ManagedIdentityClient]:
        client_args = _get_client_args(**kwargs)
        if client_args:
            return ManagedIdentityClient(**client_args)
        return None

    def get_unavailable_message(self) -> str:
        return "App Service managed identity configuration not found in environment"


def _get_client_args(**kwargs) -> Optional[Dict]:
    identity_config = kwargs.pop("identity_config", None) or {}

    url = os.environ.get(EnvironmentVariables.IDENTITY_ENDPOINT)
    secret = os.environ.get(EnvironmentVariables.IDENTITY_HEADER)
    if not (url and secret):
        # App Service managed identity isn't available in this environment
        return None

    return dict(
        kwargs,
        identity_config=identity_config,
        base_headers={"X-IDENTITY-HEADER": secret},
        request_factory=functools.partial(_get_request, url),
    )


def _get_request(url: str, scope: str, identity_config: Dict) -> HttpRequest:
    request = HttpRequest("GET", url)
    request.format_parameters(dict({"api-version": "2019-08-01", "resource": scope}, **identity_config))
    return request
