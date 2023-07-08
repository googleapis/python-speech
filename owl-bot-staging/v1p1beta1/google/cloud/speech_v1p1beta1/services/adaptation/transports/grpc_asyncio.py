# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1
from google.api_core import grpc_helpers_async
from google.auth import credentials as ga_credentials   # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc                        # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.speech_v1p1beta1.types import cloud_speech_adaptation
from google.cloud.speech_v1p1beta1.types import resource
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2  # type: ignore
from .base import AdaptationTransport, DEFAULT_CLIENT_INFO
from .grpc import AdaptationGrpcTransport


class AdaptationGrpcAsyncIOTransport(AdaptationTransport):
    """gRPC AsyncIO backend transport for Adaptation.

    Service that implements Google Cloud Speech Adaptation API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(cls,
                       host: str = 'speech.googleapis.com',
                       credentials: Optional[ga_credentials.Credentials] = None,
                       credentials_file: Optional[str] = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    def __init__(self, *,
            host: str = 'speech.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            channel: Optional[aio.Channel] = None,
            api_mtls_endpoint: Optional[str] = None,
            client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
            ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
            client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_phrase_set(self) -> Callable[
            [cloud_speech_adaptation.CreatePhraseSetRequest],
            Awaitable[resource.PhraseSet]]:
        r"""Return a callable for the create phrase set method over gRPC.

        Create a set of phrase hints. Each item in the set
        can be a single word or a multi-word phrase. The items
        in the PhraseSet are favored by the recognition model
        when you send a call that includes the PhraseSet.

        Returns:
            Callable[[~.CreatePhraseSetRequest],
                    Awaitable[~.PhraseSet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_phrase_set' not in self._stubs:
            self._stubs['create_phrase_set'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/CreatePhraseSet',
                request_serializer=cloud_speech_adaptation.CreatePhraseSetRequest.serialize,
                response_deserializer=resource.PhraseSet.deserialize,
            )
        return self._stubs['create_phrase_set']

    @property
    def get_phrase_set(self) -> Callable[
            [cloud_speech_adaptation.GetPhraseSetRequest],
            Awaitable[resource.PhraseSet]]:
        r"""Return a callable for the get phrase set method over gRPC.

        Get a phrase set.

        Returns:
            Callable[[~.GetPhraseSetRequest],
                    Awaitable[~.PhraseSet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_phrase_set' not in self._stubs:
            self._stubs['get_phrase_set'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/GetPhraseSet',
                request_serializer=cloud_speech_adaptation.GetPhraseSetRequest.serialize,
                response_deserializer=resource.PhraseSet.deserialize,
            )
        return self._stubs['get_phrase_set']

    @property
    def list_phrase_set(self) -> Callable[
            [cloud_speech_adaptation.ListPhraseSetRequest],
            Awaitable[cloud_speech_adaptation.ListPhraseSetResponse]]:
        r"""Return a callable for the list phrase set method over gRPC.

        List phrase sets.

        Returns:
            Callable[[~.ListPhraseSetRequest],
                    Awaitable[~.ListPhraseSetResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_phrase_set' not in self._stubs:
            self._stubs['list_phrase_set'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/ListPhraseSet',
                request_serializer=cloud_speech_adaptation.ListPhraseSetRequest.serialize,
                response_deserializer=cloud_speech_adaptation.ListPhraseSetResponse.deserialize,
            )
        return self._stubs['list_phrase_set']

    @property
    def update_phrase_set(self) -> Callable[
            [cloud_speech_adaptation.UpdatePhraseSetRequest],
            Awaitable[resource.PhraseSet]]:
        r"""Return a callable for the update phrase set method over gRPC.

        Update a phrase set.

        Returns:
            Callable[[~.UpdatePhraseSetRequest],
                    Awaitable[~.PhraseSet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_phrase_set' not in self._stubs:
            self._stubs['update_phrase_set'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/UpdatePhraseSet',
                request_serializer=cloud_speech_adaptation.UpdatePhraseSetRequest.serialize,
                response_deserializer=resource.PhraseSet.deserialize,
            )
        return self._stubs['update_phrase_set']

    @property
    def delete_phrase_set(self) -> Callable[
            [cloud_speech_adaptation.DeletePhraseSetRequest],
            Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete phrase set method over gRPC.

        Delete a phrase set.

        Returns:
            Callable[[~.DeletePhraseSetRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_phrase_set' not in self._stubs:
            self._stubs['delete_phrase_set'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/DeletePhraseSet',
                request_serializer=cloud_speech_adaptation.DeletePhraseSetRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_phrase_set']

    @property
    def create_custom_class(self) -> Callable[
            [cloud_speech_adaptation.CreateCustomClassRequest],
            Awaitable[resource.CustomClass]]:
        r"""Return a callable for the create custom class method over gRPC.

        Create a custom class.

        Returns:
            Callable[[~.CreateCustomClassRequest],
                    Awaitable[~.CustomClass]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_custom_class' not in self._stubs:
            self._stubs['create_custom_class'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/CreateCustomClass',
                request_serializer=cloud_speech_adaptation.CreateCustomClassRequest.serialize,
                response_deserializer=resource.CustomClass.deserialize,
            )
        return self._stubs['create_custom_class']

    @property
    def get_custom_class(self) -> Callable[
            [cloud_speech_adaptation.GetCustomClassRequest],
            Awaitable[resource.CustomClass]]:
        r"""Return a callable for the get custom class method over gRPC.

        Get a custom class.

        Returns:
            Callable[[~.GetCustomClassRequest],
                    Awaitable[~.CustomClass]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_custom_class' not in self._stubs:
            self._stubs['get_custom_class'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/GetCustomClass',
                request_serializer=cloud_speech_adaptation.GetCustomClassRequest.serialize,
                response_deserializer=resource.CustomClass.deserialize,
            )
        return self._stubs['get_custom_class']

    @property
    def list_custom_classes(self) -> Callable[
            [cloud_speech_adaptation.ListCustomClassesRequest],
            Awaitable[cloud_speech_adaptation.ListCustomClassesResponse]]:
        r"""Return a callable for the list custom classes method over gRPC.

        List custom classes.

        Returns:
            Callable[[~.ListCustomClassesRequest],
                    Awaitable[~.ListCustomClassesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_custom_classes' not in self._stubs:
            self._stubs['list_custom_classes'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/ListCustomClasses',
                request_serializer=cloud_speech_adaptation.ListCustomClassesRequest.serialize,
                response_deserializer=cloud_speech_adaptation.ListCustomClassesResponse.deserialize,
            )
        return self._stubs['list_custom_classes']

    @property
    def update_custom_class(self) -> Callable[
            [cloud_speech_adaptation.UpdateCustomClassRequest],
            Awaitable[resource.CustomClass]]:
        r"""Return a callable for the update custom class method over gRPC.

        Update a custom class.

        Returns:
            Callable[[~.UpdateCustomClassRequest],
                    Awaitable[~.CustomClass]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_custom_class' not in self._stubs:
            self._stubs['update_custom_class'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/UpdateCustomClass',
                request_serializer=cloud_speech_adaptation.UpdateCustomClassRequest.serialize,
                response_deserializer=resource.CustomClass.deserialize,
            )
        return self._stubs['update_custom_class']

    @property
    def delete_custom_class(self) -> Callable[
            [cloud_speech_adaptation.DeleteCustomClassRequest],
            Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete custom class method over gRPC.

        Delete a custom class.

        Returns:
            Callable[[~.DeleteCustomClassRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_custom_class' not in self._stubs:
            self._stubs['delete_custom_class'] = self.grpc_channel.unary_unary(
                '/google.cloud.speech.v1p1beta1.Adaptation/DeleteCustomClass',
                request_serializer=cloud_speech_adaptation.DeleteCustomClassRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_custom_class']

    def close(self):
        return self.grpc_channel.close()

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[[operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse]:
        r"""Return a callable for the list_operations method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]


__all__ = (
    'AdaptationGrpcAsyncIOTransport',
)
