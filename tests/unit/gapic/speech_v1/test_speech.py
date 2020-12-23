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

import os
import mock

import grpc
from grpc.experimental import aio
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule

from google import auth
from google.api_core import client_options
from google.api_core import exceptions
from google.api_core import future
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import operation_async  # type: ignore
from google.api_core import operations_v1
from google.auth import credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.speech_v1.services.speech import SpeechAsyncClient
from google.cloud.speech_v1.services.speech import SpeechClient
from google.cloud.speech_v1.services.speech import transports
from google.cloud.speech_v1.types import cloud_speech
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.rpc import status_pb2 as status  # type: ignore


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert SpeechClient._get_default_mtls_endpoint(None) is None
    assert SpeechClient._get_default_mtls_endpoint(api_endpoint) == api_mtls_endpoint
    assert (
        SpeechClient._get_default_mtls_endpoint(api_mtls_endpoint) == api_mtls_endpoint
    )
    assert (
        SpeechClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        SpeechClient._get_default_mtls_endpoint(sandbox_mtls_endpoint)
        == sandbox_mtls_endpoint
    )
    assert SpeechClient._get_default_mtls_endpoint(non_googleapi) == non_googleapi


@pytest.mark.parametrize("client_class", [SpeechClient, SpeechAsyncClient])
def test_speech_client_from_service_account_file(client_class):
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client._transport._credentials == creds

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client._transport._credentials == creds

        assert client._transport._host == "speech.googleapis.com:443"


def test_speech_client_get_transport_class():
    transport = SpeechClient.get_transport_class()
    assert transport == transports.SpeechGrpcTransport

    transport = SpeechClient.get_transport_class("grpc")
    assert transport == transports.SpeechGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (SpeechClient, transports.SpeechGrpcTransport, "grpc"),
        (SpeechAsyncClient, transports.SpeechGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
@mock.patch.object(
    SpeechClient, "DEFAULT_ENDPOINT", modify_default_endpoint(SpeechClient)
)
@mock.patch.object(
    SpeechAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(SpeechAsyncClient)
)
def test_speech_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(SpeechClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(SpeechClient, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            ssl_channel_credentials=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                ssl_channel_credentials=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                ssl_channel_credentials=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class()

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class()

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            ssl_channel_credentials=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (SpeechClient, transports.SpeechGrpcTransport, "grpc", "true"),
        (
            SpeechAsyncClient,
            transports.SpeechGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (SpeechClient, transports.SpeechGrpcTransport, "grpc", "false"),
        (
            SpeechAsyncClient,
            transports.SpeechGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
    ],
)
@mock.patch.object(
    SpeechClient, "DEFAULT_ENDPOINT", modify_default_endpoint(SpeechClient)
)
@mock.patch.object(
    SpeechAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(SpeechAsyncClient)
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_speech_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            ssl_channel_creds = mock.Mock()
            with mock.patch(
                "grpc.ssl_channel_credentials", return_value=ssl_channel_creds
            ):
                patched.return_value = None
                client = client_class(client_options=options)

                if use_client_cert_env == "false":
                    expected_ssl_channel_creds = None
                    expected_host = client.DEFAULT_ENDPOINT
                else:
                    expected_ssl_channel_creds = ssl_channel_creds
                    expected_host = client.DEFAULT_MTLS_ENDPOINT

                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=expected_host,
                    scopes=None,
                    ssl_channel_credentials=expected_ssl_channel_creds,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.grpc.SslCredentials.__init__", return_value=None
            ):
                with mock.patch(
                    "google.auth.transport.grpc.SslCredentials.is_mtls",
                    new_callable=mock.PropertyMock,
                ) as is_mtls_mock:
                    with mock.patch(
                        "google.auth.transport.grpc.SslCredentials.ssl_credentials",
                        new_callable=mock.PropertyMock,
                    ) as ssl_credentials_mock:
                        if use_client_cert_env == "false":
                            is_mtls_mock.return_value = False
                            ssl_credentials_mock.return_value = None
                            expected_host = client.DEFAULT_ENDPOINT
                            expected_ssl_channel_creds = None
                        else:
                            is_mtls_mock.return_value = True
                            ssl_credentials_mock.return_value = mock.Mock()
                            expected_host = client.DEFAULT_MTLS_ENDPOINT
                            expected_ssl_channel_creds = (
                                ssl_credentials_mock.return_value
                            )

                        patched.return_value = None
                        client = client_class()
                        patched.assert_called_once_with(
                            credentials=None,
                            credentials_file=None,
                            host=expected_host,
                            scopes=None,
                            ssl_channel_credentials=expected_ssl_channel_creds,
                            quota_project_id=None,
                            client_info=transports.base.DEFAULT_CLIENT_INFO,
                        )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.grpc.SslCredentials.__init__", return_value=None
            ):
                with mock.patch(
                    "google.auth.transport.grpc.SslCredentials.is_mtls",
                    new_callable=mock.PropertyMock,
                ) as is_mtls_mock:
                    is_mtls_mock.return_value = False
                    patched.return_value = None
                    client = client_class()
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=client.DEFAULT_ENDPOINT,
                        scopes=None,
                        ssl_channel_credentials=None,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                    )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (SpeechClient, transports.SpeechGrpcTransport, "grpc"),
        (SpeechAsyncClient, transports.SpeechGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_speech_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(scopes=["1", "2"],)
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            ssl_channel_credentials=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (SpeechClient, transports.SpeechGrpcTransport, "grpc"),
        (SpeechAsyncClient, transports.SpeechGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_speech_client_client_options_credentials_file(
    client_class, transport_class, transport_name
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            ssl_channel_credentials=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


def test_speech_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.speech_v1.services.speech.transports.SpeechGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = SpeechClient(client_options={"api_endpoint": "squid.clam.whelk"})
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            ssl_channel_credentials=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
        )


def test_recognize(transport: str = "grpc", request_type=cloud_speech.RecognizeRequest):
    client = SpeechClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.recognize), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_speech.RecognizeResponse()

        response = client.recognize(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == cloud_speech.RecognizeRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_speech.RecognizeResponse)


def test_recognize_from_dict():
    test_recognize(request_type=dict)


@pytest.mark.asyncio
async def test_recognize_async(transport: str = "grpc_asyncio"):
    client = SpeechAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = cloud_speech.RecognizeRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.recognize), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_speech.RecognizeResponse()
        )

        response = await client.recognize(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_speech.RecognizeResponse)


def test_recognize_flattened():
    client = SpeechClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.recognize), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_speech.RecognizeResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.recognize(
            config=cloud_speech.RecognitionConfig(
                encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
            ),
            audio=cloud_speech.RecognitionAudio(content=b"content_blob"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].config == cloud_speech.RecognitionConfig(
            encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
        )

        assert args[0].audio == cloud_speech.RecognitionAudio(content=b"content_blob")


def test_recognize_flattened_error():
    client = SpeechClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.recognize(
            cloud_speech.RecognizeRequest(),
            config=cloud_speech.RecognitionConfig(
                encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
            ),
            audio=cloud_speech.RecognitionAudio(content=b"content_blob"),
        )


@pytest.mark.asyncio
async def test_recognize_flattened_async():
    client = SpeechAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.recognize), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_speech.RecognizeResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_speech.RecognizeResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.recognize(
            config=cloud_speech.RecognitionConfig(
                encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
            ),
            audio=cloud_speech.RecognitionAudio(content=b"content_blob"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].config == cloud_speech.RecognitionConfig(
            encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
        )

        assert args[0].audio == cloud_speech.RecognitionAudio(content=b"content_blob")


@pytest.mark.asyncio
async def test_recognize_flattened_error_async():
    client = SpeechAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.recognize(
            cloud_speech.RecognizeRequest(),
            config=cloud_speech.RecognitionConfig(
                encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
            ),
            audio=cloud_speech.RecognitionAudio(content=b"content_blob"),
        )


def test_long_running_recognize(
    transport: str = "grpc", request_type=cloud_speech.LongRunningRecognizeRequest
):
    client = SpeechClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.long_running_recognize), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.long_running_recognize(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == cloud_speech.LongRunningRecognizeRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_long_running_recognize_from_dict():
    test_long_running_recognize(request_type=dict)


@pytest.mark.asyncio
async def test_long_running_recognize_async(transport: str = "grpc_asyncio"):
    client = SpeechAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = cloud_speech.LongRunningRecognizeRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.long_running_recognize), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.long_running_recognize(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_long_running_recognize_flattened():
    client = SpeechClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.long_running_recognize), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.long_running_recognize(
            config=cloud_speech.RecognitionConfig(
                encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
            ),
            audio=cloud_speech.RecognitionAudio(content=b"content_blob"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0].config == cloud_speech.RecognitionConfig(
            encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
        )

        assert args[0].audio == cloud_speech.RecognitionAudio(content=b"content_blob")


def test_long_running_recognize_flattened_error():
    client = SpeechClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.long_running_recognize(
            cloud_speech.LongRunningRecognizeRequest(),
            config=cloud_speech.RecognitionConfig(
                encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
            ),
            audio=cloud_speech.RecognitionAudio(content=b"content_blob"),
        )


@pytest.mark.asyncio
async def test_long_running_recognize_flattened_async():
    client = SpeechAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.long_running_recognize), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.long_running_recognize(
            config=cloud_speech.RecognitionConfig(
                encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
            ),
            audio=cloud_speech.RecognitionAudio(content=b"content_blob"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0].config == cloud_speech.RecognitionConfig(
            encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
        )

        assert args[0].audio == cloud_speech.RecognitionAudio(content=b"content_blob")


@pytest.mark.asyncio
async def test_long_running_recognize_flattened_error_async():
    client = SpeechAsyncClient(credentials=credentials.AnonymousCredentials(),)

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.long_running_recognize(
            cloud_speech.LongRunningRecognizeRequest(),
            config=cloud_speech.RecognitionConfig(
                encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16
            ),
            audio=cloud_speech.RecognitionAudio(content=b"content_blob"),
        )


def test_streaming_recognize(
    transport: str = "grpc", request_type=cloud_speech.StreamingRecognizeRequest
):
    client = SpeechClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    requests = [request]

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.streaming_recognize), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([cloud_speech.StreamingRecognizeResponse()])

        response = client.streaming_recognize(iter(requests))

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert next(args[0]) == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, cloud_speech.StreamingRecognizeResponse)


def test_streaming_recognize_from_dict():
    test_streaming_recognize(request_type=dict)


@pytest.mark.asyncio
async def test_streaming_recognize_async(transport: str = "grpc_asyncio"):
    client = SpeechAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = cloud_speech.StreamingRecognizeRequest()

    requests = [request]

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.streaming_recognize), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.StreamStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[cloud_speech.StreamingRecognizeResponse()]
        )

        response = await client.streaming_recognize(iter(requests))

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert next(args[0]) == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, cloud_speech.StreamingRecognizeResponse)


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.SpeechGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SpeechClient(
            credentials=credentials.AnonymousCredentials(), transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.SpeechGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SpeechClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.SpeechGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SpeechClient(
            client_options={"scopes": ["1", "2"]}, transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.SpeechGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    client = SpeechClient(transport=transport)
    assert client._transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.SpeechGrpcTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.SpeechGrpcAsyncIOTransport(
        credentials=credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [transports.SpeechGrpcTransport, transports.SpeechGrpcAsyncIOTransport],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = SpeechClient(credentials=credentials.AnonymousCredentials(),)
    assert isinstance(client._transport, transports.SpeechGrpcTransport,)


def test_speech_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(exceptions.DuplicateCredentialArgs):
        transport = transports.SpeechTransport(
            credentials=credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_speech_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.speech_v1.services.speech.transports.SpeechTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.SpeechTransport(
            credentials=credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "recognize",
        "long_running_recognize",
        "streaming_recognize",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_speech_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        auth, "load_credentials_from_file"
    ) as load_creds, mock.patch(
        "google.cloud.speech_v1.services.speech.transports.SpeechTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.SpeechTransport(
            credentials_file="credentials.json", quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_speech_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(auth, "default") as adc, mock.patch(
        "google.cloud.speech_v1.services.speech.transports.SpeechTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transport = transports.SpeechTransport()
        adc.assert_called_once()


def test_speech_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        SpeechClient()
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


def test_speech_transport_auth_adc():
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transports.SpeechGrpcTransport(
            host="squid.clam.whelk", quota_project_id="octopus"
        )
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_speech_host_no_port():
    client = SpeechClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="speech.googleapis.com"
        ),
    )
    assert client._transport._host == "speech.googleapis.com:443"


def test_speech_host_with_port():
    client = SpeechClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="speech.googleapis.com:8000"
        ),
    )
    assert client._transport._host == "speech.googleapis.com:8000"


def test_speech_grpc_transport_channel():
    channel = grpc.insecure_channel("http://localhost/")

    # Check that channel is used if provided.
    transport = transports.SpeechGrpcTransport(
        host="squid.clam.whelk", channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"


def test_speech_grpc_asyncio_transport_channel():
    channel = aio.insecure_channel("http://localhost/")

    # Check that channel is used if provided.
    transport = transports.SpeechGrpcAsyncIOTransport(
        host="squid.clam.whelk", channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"


@pytest.mark.parametrize(
    "transport_class",
    [transports.SpeechGrpcTransport, transports.SpeechGrpcAsyncIOTransport],
)
def test_speech_transport_channel_mtls_with_client_cert_source(transport_class):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel", autospec=True
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(auth, "default") as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=("https://www.googleapis.com/auth/cloud-platform",),
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
            )
            assert transport.grpc_channel == mock_grpc_channel


@pytest.mark.parametrize(
    "transport_class",
    [transports.SpeechGrpcTransport, transports.SpeechGrpcAsyncIOTransport],
)
def test_speech_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel", autospec=True
        ) as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=("https://www.googleapis.com/auth/cloud-platform",),
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_speech_grpc_lro_client():
    client = SpeechClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc",
    )
    transport = client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsClient,)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_speech_grpc_lro_async_client():
    client = SpeechAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc_asyncio",
    )
    transport = client._client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsAsyncClient,)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_client_withDEFAULT_CLIENT_INFO():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.SpeechTransport, "_prep_wrapped_messages"
    ) as prep:
        client = SpeechClient(
            credentials=credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.SpeechTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = SpeechClient.get_transport_class()
        transport = transport_class(
            credentials=credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)
