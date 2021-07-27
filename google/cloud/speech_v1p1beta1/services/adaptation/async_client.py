# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.speech_v1p1beta1.services.adaptation import pagers
from google.cloud.speech_v1p1beta1.types import cloud_speech_adaptation
from google.cloud.speech_v1p1beta1.types import resource
from google.protobuf import field_mask_pb2  # type: ignore
from .transports.base import AdaptationTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import AdaptationGrpcAsyncIOTransport
from .client import AdaptationClient


class AdaptationAsyncClient:
    """Service that implements Google Cloud Speech Adaptation API."""

    _client: AdaptationClient

    DEFAULT_ENDPOINT = AdaptationClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AdaptationClient.DEFAULT_MTLS_ENDPOINT

    custom_class_path = staticmethod(AdaptationClient.custom_class_path)
    parse_custom_class_path = staticmethod(AdaptationClient.parse_custom_class_path)
    phrase_set_path = staticmethod(AdaptationClient.phrase_set_path)
    parse_phrase_set_path = staticmethod(AdaptationClient.parse_phrase_set_path)
    common_billing_account_path = staticmethod(
        AdaptationClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AdaptationClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AdaptationClient.common_folder_path)
    parse_common_folder_path = staticmethod(AdaptationClient.parse_common_folder_path)
    common_organization_path = staticmethod(AdaptationClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        AdaptationClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AdaptationClient.common_project_path)
    parse_common_project_path = staticmethod(AdaptationClient.parse_common_project_path)
    common_location_path = staticmethod(AdaptationClient.common_location_path)
    parse_common_location_path = staticmethod(
        AdaptationClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AdaptationAsyncClient: The constructed client.
        """
        return AdaptationClient.from_service_account_info.__func__(AdaptationAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AdaptationAsyncClient: The constructed client.
        """
        return AdaptationClient.from_service_account_file.__func__(AdaptationAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> AdaptationTransport:
        """Returns the transport used by the client instance.

        Returns:
            AdaptationTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(AdaptationClient).get_transport_class, type(AdaptationClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, AdaptationTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the adaptation client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.AdaptationTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = AdaptationClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_phrase_set(
        self,
        request: cloud_speech_adaptation.CreatePhraseSetRequest = None,
        *,
        parent: str = None,
        phrase_set: resource.PhraseSet = None,
        phrase_set_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.PhraseSet:
        r"""Create a set of phrase hints. Each item in the set
        can be a single word or a multi-word phrase. The items
        in the PhraseSet are favored by the recognition model
        when you send a call that includes the PhraseSet.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.CreatePhraseSetRequest`):
                The request object. Message sent by the client for the
                `CreatePhraseSet` method.
            parent (:class:`str`):
                Required. The parent resource where this phrase set will
                be created. Format:
                {api_version}/projects/{project}/locations/{location}/phraseSets

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            phrase_set (:class:`google.cloud.speech_v1p1beta1.types.PhraseSet`):
                Required. The phrase set to create.
                This corresponds to the ``phrase_set`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            phrase_set_id (:class:`str`):
                Required. The ID to use for the phrase set, which will
                become the final component of the phrase set's resource
                name.

                This value should be 4-63 characters, and valid
                characters are /[a-z][0-9]-/.

                This corresponds to the ``phrase_set_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.speech_v1p1beta1.types.PhraseSet:
                Provides "hints" to the speech
                recognizer to favor specific words and
                phrases in the results.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, phrase_set, phrase_set_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.CreatePhraseSetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if phrase_set is not None:
            request.phrase_set = phrase_set
        if phrase_set_id is not None:
            request.phrase_set_id = phrase_set_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_phrase_set,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_phrase_set(
        self,
        request: cloud_speech_adaptation.GetPhraseSetRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.PhraseSet:
        r"""Get a phrase set.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.GetPhraseSetRequest`):
                The request object. Message sent by the client for the
                `GetPhraseSet` method.
            name (:class:`str`):
                Required. The name of the phrase set to retrieve.
                Format:
                {api_version}/projects/{project}/locations/{location}/phraseSets/{phrase_set}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.speech_v1p1beta1.types.PhraseSet:
                Provides "hints" to the speech
                recognizer to favor specific words and
                phrases in the results.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.GetPhraseSetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_phrase_set,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_phrase_set(
        self,
        request: cloud_speech_adaptation.ListPhraseSetRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListPhraseSetAsyncPager:
        r"""List phrase sets.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.ListPhraseSetRequest`):
                The request object. Message sent by the client for the
                `ListPhraseSet` method.
            parent (:class:`str`):
                Required. The parent, which owns this
                collection of phrase set. Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.speech_v1p1beta1.services.adaptation.pagers.ListPhraseSetAsyncPager:
                Message returned to the client by the ListPhraseSet
                method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.ListPhraseSetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_phrase_set,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListPhraseSetAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_phrase_set(
        self,
        request: cloud_speech_adaptation.UpdatePhraseSetRequest = None,
        *,
        phrase_set: resource.PhraseSet = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.PhraseSet:
        r"""Update a phrase set.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.UpdatePhraseSetRequest`):
                The request object. Message sent by the client for the
                `UpdatePhraseSet` method.
            phrase_set (:class:`google.cloud.speech_v1p1beta1.types.PhraseSet`):
                Required. The phrase set to update.

                The phrase set's ``name`` field is used to identify the
                set to be updated. Format:
                {api_version}/projects/{project}/locations/{location}/phraseSets/{phrase_set}

                This corresponds to the ``phrase_set`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.speech_v1p1beta1.types.PhraseSet:
                Provides "hints" to the speech
                recognizer to favor specific words and
                phrases in the results.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([phrase_set, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.UpdatePhraseSetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if phrase_set is not None:
            request.phrase_set = phrase_set
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_phrase_set,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("phrase_set.name", request.phrase_set.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_phrase_set(
        self,
        request: cloud_speech_adaptation.DeletePhraseSetRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Delete a phrase set.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.DeletePhraseSetRequest`):
                The request object. Message sent by the client for the
                `DeletePhraseSet` method.
            name (:class:`str`):
                Required. The name of the phrase set to delete. Format:
                {api_version}/projects/{project}/locations/{location}/phraseSets/{phrase_set}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.DeletePhraseSetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_phrase_set,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def create_custom_class(
        self,
        request: cloud_speech_adaptation.CreateCustomClassRequest = None,
        *,
        parent: str = None,
        custom_class: resource.CustomClass = None,
        custom_class_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.CustomClass:
        r"""Create a custom class.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.CreateCustomClassRequest`):
                The request object. Message sent by the client for the
                `CreateCustomClass` method.
            parent (:class:`str`):
                Required. The parent resource where this custom class
                will be created. Format:
                {api_version}/projects/{project}/locations/{location}/customClasses

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            custom_class (:class:`google.cloud.speech_v1p1beta1.types.CustomClass`):
                Required. The custom class to create.
                This corresponds to the ``custom_class`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            custom_class_id (:class:`str`):
                Required. The ID to use for the custom class, which will
                become the final component of the custom class' resource
                name.

                This value should be 4-63 characters, and valid
                characters are /[a-z][0-9]-/.

                This corresponds to the ``custom_class_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.speech_v1p1beta1.types.CustomClass:
                A set of words or phrases that
                represents a common concept likely to
                appear in your audio, for example a list
                of passenger ship names. CustomClass
                items can be substituted into
                placeholders that you set in PhraseSet
                phrases.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, custom_class, custom_class_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.CreateCustomClassRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if custom_class is not None:
            request.custom_class = custom_class
        if custom_class_id is not None:
            request.custom_class_id = custom_class_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_custom_class,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_custom_class(
        self,
        request: cloud_speech_adaptation.GetCustomClassRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.CustomClass:
        r"""Get a custom class.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.GetCustomClassRequest`):
                The request object. Message sent by the client for the
                `GetCustomClass` method.
            name (:class:`str`):
                Required. The name of the custom class to retrieve.
                Format:
                {api_version}/projects/{project}/locations/{location}/customClasses/{custom_class}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.speech_v1p1beta1.types.CustomClass:
                A set of words or phrases that
                represents a common concept likely to
                appear in your audio, for example a list
                of passenger ship names. CustomClass
                items can be substituted into
                placeholders that you set in PhraseSet
                phrases.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.GetCustomClassRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_custom_class,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_custom_classes(
        self,
        request: cloud_speech_adaptation.ListCustomClassesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCustomClassesAsyncPager:
        r"""List custom classes.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.ListCustomClassesRequest`):
                The request object. Message sent by the client for the
                `ListCustomClasses` method.
            parent (:class:`str`):
                Required. The parent, which owns this collection of
                custom classes. Format:
                {api_version}/projects/{project}/locations/{location}/customClasses

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.speech_v1p1beta1.services.adaptation.pagers.ListCustomClassesAsyncPager:
                Message returned to the client by the ListCustomClasses
                method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.ListCustomClassesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_custom_classes,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCustomClassesAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_custom_class(
        self,
        request: cloud_speech_adaptation.UpdateCustomClassRequest = None,
        *,
        custom_class: resource.CustomClass = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resource.CustomClass:
        r"""Update a custom class.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.UpdateCustomClassRequest`):
                The request object. Message sent by the client for the
                `UpdateCustomClass` method.
            custom_class (:class:`google.cloud.speech_v1p1beta1.types.CustomClass`):
                Required. The custom class to update.

                The custom class's ``name`` field is used to identify
                the custom class to be updated. Format:
                {api_version}/projects/{project}/locations/{location}/customClasses/{custom_class}

                This corresponds to the ``custom_class`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.speech_v1p1beta1.types.CustomClass:
                A set of words or phrases that
                represents a common concept likely to
                appear in your audio, for example a list
                of passenger ship names. CustomClass
                items can be substituted into
                placeholders that you set in PhraseSet
                phrases.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([custom_class, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.UpdateCustomClassRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if custom_class is not None:
            request.custom_class = custom_class
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_custom_class,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("custom_class.name", request.custom_class.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_custom_class(
        self,
        request: cloud_speech_adaptation.DeleteCustomClassRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Delete a custom class.

        Args:
            request (:class:`google.cloud.speech_v1p1beta1.types.DeleteCustomClassRequest`):
                The request object. Message sent by the client for the
                `DeleteCustomClass` method.
            name (:class:`str`):
                Required. The name of the custom class to delete.
                Format:
                {api_version}/projects/{project}/locations/{location}/customClasses/{custom_class}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = cloud_speech_adaptation.DeleteCustomClassRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_custom_class,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-speech",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("AdaptationAsyncClient",)
