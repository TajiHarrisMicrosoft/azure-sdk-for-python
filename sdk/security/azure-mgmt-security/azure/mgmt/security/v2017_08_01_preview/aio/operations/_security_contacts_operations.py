# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._security_contacts_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SecurityContactsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2017_08_01_preview.aio.SecurityCenter`'s
        :attr:`security_contacts` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, **kwargs: Any) -> AsyncIterable["_models.SecurityContact"]:
        """Security contact configurations for the subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecurityContact or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )  # type: Literal["2017-08-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SecurityContactList]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SecurityContactList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts"}  # type: ignore

    @distributed_trace_async
    async def get(self, security_contact_name: str, **kwargs: Any) -> _models.SecurityContact:
        """Security contact configurations for the subscription.

        :param security_contact_name: Name of the security contact object. Required.
        :type security_contact_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityContact or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )  # type: Literal["2017-08-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SecurityContact]

        request = build_get_request(
            security_contact_name=security_contact_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityContact", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName}"}  # type: ignore

    @overload
    async def create(
        self,
        security_contact_name: str,
        security_contact: _models.SecurityContact,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SecurityContact:
        """Security contact configurations for the subscription.

        :param security_contact_name: Name of the security contact object. Required.
        :type security_contact_name: str
        :param security_contact: Security contact object. Required.
        :type security_contact: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityContact or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self, security_contact_name: str, security_contact: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.SecurityContact:
        """Security contact configurations for the subscription.

        :param security_contact_name: Name of the security contact object. Required.
        :type security_contact_name: str
        :param security_contact: Security contact object. Required.
        :type security_contact: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityContact or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self, security_contact_name: str, security_contact: Union[_models.SecurityContact, IO], **kwargs: Any
    ) -> _models.SecurityContact:
        """Security contact configurations for the subscription.

        :param security_contact_name: Name of the security contact object. Required.
        :type security_contact_name: str
        :param security_contact: Security contact object. Is either a model type or a IO type.
         Required.
        :type security_contact: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityContact or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )  # type: Literal["2017-08-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SecurityContact]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(security_contact, (IO, bytes)):
            _content = security_contact
        else:
            _json = self._serialize.body(security_contact, "SecurityContact")

        request = build_create_request(
            security_contact_name=security_contact_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityContact", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, security_contact_name: str, **kwargs: Any
    ) -> None:
        """Security contact configurations for the subscription.

        :param security_contact_name: Name of the security contact object. Required.
        :type security_contact_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )  # type: Literal["2017-08-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            security_contact_name=security_contact_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName}"}  # type: ignore

    @overload
    async def update(
        self,
        security_contact_name: str,
        security_contact: _models.SecurityContact,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SecurityContact:
        """Security contact configurations for the subscription.

        :param security_contact_name: Name of the security contact object. Required.
        :type security_contact_name: str
        :param security_contact: Security contact object. Required.
        :type security_contact: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityContact or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, security_contact_name: str, security_contact: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.SecurityContact:
        """Security contact configurations for the subscription.

        :param security_contact_name: Name of the security contact object. Required.
        :type security_contact_name: str
        :param security_contact: Security contact object. Required.
        :type security_contact: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityContact or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self, security_contact_name: str, security_contact: Union[_models.SecurityContact, IO], **kwargs: Any
    ) -> _models.SecurityContact:
        """Security contact configurations for the subscription.

        :param security_contact_name: Name of the security contact object. Required.
        :type security_contact_name: str
        :param security_contact: Security contact object. Is either a model type or a IO type.
         Required.
        :type security_contact: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityContact or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2017_08_01_preview.models.SecurityContact
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", "2017-08-01-preview")
        )  # type: Literal["2017-08-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SecurityContact]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(security_contact, (IO, bytes)):
            _content = security_contact
        else:
            _json = self._serialize.body(security_contact, "SecurityContact")

        request = build_update_request(
            security_contact_name=security_contact_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SecurityContact", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/securityContacts/{securityContactName}"}  # type: ignore
