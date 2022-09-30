# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
import proto  # type: ignore

from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.speech.v2",
    manifest={
        "CreateRecognizerRequest",
        "OperationMetadata",
        "ListRecognizersRequest",
        "ListRecognizersResponse",
        "GetRecognizerRequest",
        "UpdateRecognizerRequest",
        "DeleteRecognizerRequest",
        "UndeleteRecognizerRequest",
        "Recognizer",
        "AutoDetectDecodingConfig",
        "ExplicitDecodingConfig",
        "SpeakerDiarizationConfig",
        "RecognitionFeatures",
        "SpeechAdaptation",
        "RecognitionConfig",
        "RecognizeRequest",
        "RecognitionResponseMetadata",
        "SpeechRecognitionAlternative",
        "WordInfo",
        "SpeechRecognitionResult",
        "RecognizeResponse",
        "StreamingRecognitionFeatures",
        "StreamingRecognitionConfig",
        "StreamingRecognizeRequest",
        "BatchRecognizeRequest",
        "BatchRecognizeResponse",
        "BatchRecognizeFileResult",
        "BatchRecognizeTranscriptionMetadata",
        "BatchRecognizeMetadata",
        "BatchRecognizeFileMetadata",
        "StreamingRecognitionResult",
        "StreamingRecognizeResponse",
        "Config",
        "GetConfigRequest",
        "UpdateConfigRequest",
        "CustomClass",
        "PhraseSet",
        "CreateCustomClassRequest",
        "ListCustomClassesRequest",
        "ListCustomClassesResponse",
        "GetCustomClassRequest",
        "UpdateCustomClassRequest",
        "DeleteCustomClassRequest",
        "UndeleteCustomClassRequest",
        "CreatePhraseSetRequest",
        "ListPhraseSetsRequest",
        "ListPhraseSetsResponse",
        "GetPhraseSetRequest",
        "UpdatePhraseSetRequest",
        "DeletePhraseSetRequest",
        "UndeletePhraseSetRequest",
    },
)


class CreateRecognizerRequest(proto.Message):
    r"""Request message for the
    [CreateRecognizer][google.cloud.speech.v2.Speech.CreateRecognizer]
    method.

    Attributes:
        recognizer (google.cloud.speech_v2.types.Recognizer):
            Required. The Recognizer to create.
        validate_only (bool):
            If set, validate the request and preview the
            Recognizer, but do not actually create it.
        recognizer_id (str):
            The ID to use for the Recognizer, which will become the
            final component of the Recognizer's resource name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-/.
        parent (str):
            Required. The project and location where this Recognizer
            will be created. The expected format is
            ``projects/{project}/locations/{location}``.
    """

    recognizer = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Recognizer",
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    recognizer_id = proto.Field(
        proto.STRING,
        number=3,
    )
    parent = proto.Field(
        proto.STRING,
        number=4,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of a long-running operation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was last updated.
        resource (str):
            The resource path for the target of the
            operation.
        method (str):
            The method that triggered the operation.
        kms_key_name (str):
            The `KMS key
            name <https://cloud.google.com/kms/docs/resource-hierarchy#keys>`__
            with which the content of the Operation is encrypted. The
            expected format is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.
        kms_key_version_name (str):
            The `KMS key version
            name <https://cloud.google.com/kms/docs/resource-hierarchy#key_versions>`__
            with which content of the Operation is encrypted. The
            expected format is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}``.
        batch_recognize_request (google.cloud.speech_v2.types.BatchRecognizeRequest):
            The BatchRecognizeRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        create_recognizer_request (google.cloud.speech_v2.types.CreateRecognizerRequest):
            The CreateRecognizerRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        update_recognizer_request (google.cloud.speech_v2.types.UpdateRecognizerRequest):
            The UpdateRecognizerRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        delete_recognizer_request (google.cloud.speech_v2.types.DeleteRecognizerRequest):
            The DeleteRecognizerRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        undelete_recognizer_request (google.cloud.speech_v2.types.UndeleteRecognizerRequest):
            The UndeleteRecognizerRequest that spawned
            the Operation.

            This field is a member of `oneof`_ ``request``.
        create_custom_class_request (google.cloud.speech_v2.types.CreateCustomClassRequest):
            The CreateCustomClassRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        update_custom_class_request (google.cloud.speech_v2.types.UpdateCustomClassRequest):
            The UpdateCustomClassRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        delete_custom_class_request (google.cloud.speech_v2.types.DeleteCustomClassRequest):
            The DeleteCustomClassRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        undelete_custom_class_request (google.cloud.speech_v2.types.UndeleteCustomClassRequest):
            The UndeleteCustomClassRequest that spawned
            the Operation.

            This field is a member of `oneof`_ ``request``.
        create_phrase_set_request (google.cloud.speech_v2.types.CreatePhraseSetRequest):
            The CreatePhraseSetRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        update_phrase_set_request (google.cloud.speech_v2.types.UpdatePhraseSetRequest):
            The UpdatePhraseSetRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        delete_phrase_set_request (google.cloud.speech_v2.types.DeletePhraseSetRequest):
            The DeletePhraseSetRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        undelete_phrase_set_request (google.cloud.speech_v2.types.UndeletePhraseSetRequest):
            The UndeletePhraseSetRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        update_config_request (google.cloud.speech_v2.types.UpdateConfigRequest):
            The UpdateConfigRequest that spawned the
            Operation.

            This field is a member of `oneof`_ ``request``.
        progress_percent (int):
            The percent progress of the Operation. Values
            can range from 0-100. If the value is 100, then
            the operation is finished.
        batch_recognize_metadata (google.cloud.speech_v2.types.BatchRecognizeMetadata):
            Metadata specific to the BatchRecognize
            method.

            This field is a member of `oneof`_ ``metadata``.
    """

    create_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    resource = proto.Field(
        proto.STRING,
        number=3,
    )
    method = proto.Field(
        proto.STRING,
        number=4,
    )
    kms_key_name = proto.Field(
        proto.STRING,
        number=6,
    )
    kms_key_version_name = proto.Field(
        proto.STRING,
        number=7,
    )
    batch_recognize_request = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="request",
        message="BatchRecognizeRequest",
    )
    create_recognizer_request = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="request",
        message="CreateRecognizerRequest",
    )
    update_recognizer_request = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="request",
        message="UpdateRecognizerRequest",
    )
    delete_recognizer_request = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="request",
        message="DeleteRecognizerRequest",
    )
    undelete_recognizer_request = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="request",
        message="UndeleteRecognizerRequest",
    )
    create_custom_class_request = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="request",
        message="CreateCustomClassRequest",
    )
    update_custom_class_request = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="request",
        message="UpdateCustomClassRequest",
    )
    delete_custom_class_request = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="request",
        message="DeleteCustomClassRequest",
    )
    undelete_custom_class_request = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="request",
        message="UndeleteCustomClassRequest",
    )
    create_phrase_set_request = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="request",
        message="CreatePhraseSetRequest",
    )
    update_phrase_set_request = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="request",
        message="UpdatePhraseSetRequest",
    )
    delete_phrase_set_request = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="request",
        message="DeletePhraseSetRequest",
    )
    undelete_phrase_set_request = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="request",
        message="UndeletePhraseSetRequest",
    )
    update_config_request = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="request",
        message="UpdateConfigRequest",
    )
    progress_percent = proto.Field(
        proto.INT32,
        number=22,
    )
    batch_recognize_metadata = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="metadata",
        message="BatchRecognizeMetadata",
    )


class ListRecognizersRequest(proto.Message):
    r"""Request message for the
    [ListRecognizers][google.cloud.speech.v2.Speech.ListRecognizers]
    method.

    Attributes:
        parent (str):
            Required. The project and location of Recognizers to list.
            The expected format is
            ``projects/{project}/locations/{location}``.
        page_size (int):
            The maximum number of Recognizers to return.
            The service may return fewer than this value. If
            unspecified, at most 20 Recognizers will be
            returned. The maximum value is 20; values above
            20 will be coerced to 20.
        page_token (str):
            A page token, received from a previous
            [ListRecognizers][google.cloud.speech.v2.Speech.ListRecognizers]
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            [ListRecognizers][google.cloud.speech.v2.Speech.ListRecognizers]
            must match the call that provided the page token.
        show_deleted (bool):
            Whether, or not, to show resources that have
            been deleted.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )
    show_deleted = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListRecognizersResponse(proto.Message):
    r"""Response message for the
    [ListRecognizers][google.cloud.speech.v2.Speech.ListRecognizers]
    method.

    Attributes:
        recognizers (Sequence[google.cloud.speech_v2.types.Recognizer]):
            The list of requested Recognizers.
        next_page_token (str):
            A token, which can be sent as
            [page_token][google.cloud.speech.v2.ListRecognizersRequest.page_token]
            to retrieve the next page. If this field is omitted, there
            are no subsequent pages. This token expires after 72 hours.
    """

    @property
    def raw_page(self):
        return self

    recognizers = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Recognizer",
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class GetRecognizerRequest(proto.Message):
    r"""Request message for the
    [GetRecognizer][google.cloud.speech.v2.Speech.GetRecognizer] method.

    Attributes:
        name (str):
            Required. The name of the Recognizer to retrieve. The
            expected format is
            ``projects/{project}/locations/{location}/recognizers/{recognizer}``.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRecognizerRequest(proto.Message):
    r"""Request message for the
    [UpdateRecognizer][google.cloud.speech.v2.Speech.UpdateRecognizer]
    method.

    Attributes:
        recognizer (google.cloud.speech_v2.types.Recognizer):
            Required. The Recognizer to update.

            The Recognizer's ``name`` field is used to identify the
            Recognizer to update. Format:
            ``projects/{project}/locations/{location}/recognizers/{recognizer}``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. If empty, all non-default
            valued fields are considered for update. Use ``*`` to update
            the entire Recognizer resource.
        validate_only (bool):
            If set, validate the request and preview the
            updated Recognizer, but do not actually update
            it.
    """

    recognizer = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Recognizer",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeleteRecognizerRequest(proto.Message):
    r"""Request message for the
    [DeleteRecognizer][google.cloud.speech.v2.Speech.DeleteRecognizer]
    method.

    Attributes:
        name (str):
            Required. The name of the Recognizer to delete. Format:
            ``projects/{project}/locations/{location}/recognizers/{recognizer}``
        validate_only (bool):
            If set, validate the request and preview the
            deleted Recognizer, but do not actually delete
            it.
        allow_missing (bool):
            If set to true, and the Recognizer is not
            found, the request will succeed and  be a no-op
            (no Operation is recorded in this case).
        etag (str):
            This checksum is computed by the server based
            on the value of other fields. This may be sent
            on update, undelete, and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    allow_missing = proto.Field(
        proto.BOOL,
        number=4,
    )
    etag = proto.Field(
        proto.STRING,
        number=3,
    )


class UndeleteRecognizerRequest(proto.Message):
    r"""Request message for the
    [UndeleteRecognizer][google.cloud.speech.v2.Speech.UndeleteRecognizer]
    method.

    Attributes:
        name (str):
            Required. The name of the Recognizer to undelete. Format:
            ``projects/{project}/locations/{location}/recognizers/{recognizer}``
        validate_only (bool):
            If set, validate the request and preview the
            undeleted Recognizer, but do not actually
            undelete it.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields. This may be sent
            on update, undelete, and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag = proto.Field(
        proto.STRING,
        number=4,
    )


class Recognizer(proto.Message):
    r"""A Recognizer message. Stores recognition configuration and
    metadata.

    Attributes:
        name (str):
            Output only. The resource name of the Recognizer. Format:
            ``projects/{project}/locations/{location}/recognizers/{recognizer}``.
        uid (str):
            Output only. System-assigned unique
            identifier for the Recognizer.
        display_name (str):
            User-settable, human-readable name for the
            Recognizer. Must be 63 characters or less.
        model (str):
            Required. Which model to use for recognition requests.
            Select the model best suited to your domain to get best
            results.

            Supported models:

            -  ``latest_long``

               Best for long form content like media or conversation.

            -  ``latest_short``

               Best for short form content like commands or single shot
               directed speech. When using this model, the service will
               stop transcribing audio after the first utterance is
               detected and completed.

            When using this model,
            [SEPARATE_RECOGNITION_PER_CHANNEL][google.cloud.speech.v2.RecognitionFeatures.MultiChannelMode.SEPARATE_RECOGNITION_PER_CHANNEL]
            is not supported; multi-channel audio is accepted, but only
            the first channel will be processed and transcribed.
        language_codes (Sequence[str]):
            Required. The language of the supplied audio as a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag.

            Supported languages:

            -  ``en-US``

            -  ``en-GB``

            -  ``fr-FR``

            If additional languages are provided, recognition result
            will contain recognition in the most likely language
            detected. The recognition result will include the language
            tag of the language detected in the audio. When you create
            or update a Recognizer, these values are stored in
            normalized BCP-47 form. For example, "en-us" is stored as
            "en-US".
        default_recognition_config (google.cloud.speech_v2.types.RecognitionConfig):
            Default configuration to use for requests with this
            Recognizer. This can be overwritten by inline configuration
            in the
            [RecognizeRequest.config][google.cloud.speech.v2.RecognizeRequest.config]
            field.
        annotations (Mapping[str, str]):
            Allows users to store small amounts of
            arbitrary data. Both the key and the value must
            be 63 characters or less each. At most 100
            annotations.
        state (google.cloud.speech_v2.types.Recognizer.State):
            Output only. The Recognizer lifecycle state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time this
            Recognizer was modified.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            Recognizer was requested for deletion.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            Recognizer will be purged.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields. This
            may be sent on update, undelete, and delete
            requests to ensure the client has an up-to-date
            value before proceeding.
        reconciling (bool):
            Output only. Whether or not this Recognizer
            is in the process of being updated.
        kms_key_name (str):
            Output only. The `KMS key
            name <https://cloud.google.com/kms/docs/resource-hierarchy#keys>`__
            with which the Recognizer is encrypted. The expected format
            is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.
        kms_key_version_name (str):
            Output only. The `KMS key version
            name <https://cloud.google.com/kms/docs/resource-hierarchy#key_versions>`__
            with which the Recognizer is encrypted. The expected format
            is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}``.
    """

    class State(proto.Enum):
        r"""Set of states that define the lifecycle of a Recognizer."""
        STATE_UNSPECIFIED = 0
        ACTIVE = 2
        DELETED = 4

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    uid = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name = proto.Field(
        proto.STRING,
        number=3,
    )
    model = proto.Field(
        proto.STRING,
        number=4,
    )
    language_codes = proto.RepeatedField(
        proto.STRING,
        number=17,
    )
    default_recognition_config = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RecognitionConfig",
    )
    annotations = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    state = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    delete_time = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    expire_time = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    etag = proto.Field(
        proto.STRING,
        number=12,
    )
    reconciling = proto.Field(
        proto.BOOL,
        number=13,
    )
    kms_key_name = proto.Field(
        proto.STRING,
        number=15,
    )
    kms_key_version_name = proto.Field(
        proto.STRING,
        number=16,
    )


class AutoDetectDecodingConfig(proto.Message):
    r"""Automatically detected decoding parameters. Supported for the
    following encodings:

    -  WAV_LINEAR16: 16-bit signed little-endian PCM samples in a WAV
       container.
    -  WAV_MULAW: 8-bit companded mulaw samples in a WAV container.
    -  WAV_ALAW: 8-bit companded alaw samples in a WAV container.
    -  RFC4867_5_AMR: AMR frames with an rfc4867.5 header.
    -  RFC4867_5_AMRWB: AMR-WB frames with an rfc4867.5 header.
    -  FLAC: FLAC frames in the "native FLAC" container format.
    -  MP3: MPEG audio frames with optional (ignored) ID3 metadata.
    -  OGG_OPUS: Opus audio frames in an Ogg container.
    -  WEBM_OPUS: Opus audio frames in a WebM container.

    """


class ExplicitDecodingConfig(proto.Message):
    r"""Explicitly specified decoding parameters.

    Attributes:
        encoding (google.cloud.speech_v2.types.ExplicitDecodingConfig.AudioEncoding):
            Required. Encoding of the audio data sent for
            recognition.
        sample_rate_hertz (int):
            Sample rate in Hertz of the audio data sent for recognition.
            Valid values are: 8000-48000. 16000 is optimal. For best
            results, set the sampling rate of the audio source to 16000
            Hz. If that's not possible, use the native sample rate of
            the audio source (instead of re-sampling). Supported for the
            following encodings:

            -  LINEAR16: Headerless 16-bit signed little-endian PCM
               samples.
            -  MULAW: Headerless 8-bit companded mulaw samples.
            -  ALAW: Headerless 8-bit companded alaw samples.
        audio_channel_count (int):
            Number of channels present in the audio data sent for
            recognition. Supported for the following encodings:

            -  LINEAR16: Headerless 16-bit signed little-endian PCM
               samples.
            -  MULAW: Headerless 8-bit companded mulaw samples.
            -  ALAW: Headerless 8-bit companded alaw samples.
    """

    class AudioEncoding(proto.Enum):
        r"""Supported audio data encodings."""
        AUDIO_ENCODING_UNSPECIFIED = 0
        LINEAR16 = 1
        MULAW = 2
        ALAW = 3

    encoding = proto.Field(
        proto.ENUM,
        number=1,
        enum=AudioEncoding,
    )
    sample_rate_hertz = proto.Field(
        proto.INT32,
        number=2,
    )
    audio_channel_count = proto.Field(
        proto.INT32,
        number=3,
    )


class SpeakerDiarizationConfig(proto.Message):
    r"""Configuration to enable speaker diarization.

    Attributes:
        min_speaker_count (int):
            Required. Minimum number of speakers in the conversation.
            This range gives you more flexibility by allowing the system
            to automatically determine the correct number of speakers.
            If not set, the default value is 2.

            To fix the number of speakers detected in the audio, set
            ``min_speaker_count`` = ``max_speaker_count``.
        max_speaker_count (int):
            Required. Maximum number of speakers in the conversation.
            Valid values are: 1-6. Must be >= ``min_speaker_count``.
            This range gives you more flexibility by allowing the system
            to automatically determine the correct number of speakers.
    """

    min_speaker_count = proto.Field(
        proto.INT32,
        number=2,
    )
    max_speaker_count = proto.Field(
        proto.INT32,
        number=3,
    )


class RecognitionFeatures(proto.Message):
    r"""Available recognition features.

    Attributes:
        profanity_filter (bool):
            If set to ``true``, the server will attempt to filter out
            profanities, replacing all but the initial character in each
            filtered word with asterisks, for instance, "f***". If set
            to ``false`` or omitted, profanities won't be filtered out.
        enable_word_time_offsets (bool):
            If ``true``, the top result includes a list of words and the
            start and end time offsets (timestamps) for those words. If
            ``false``, no word-level time offset information is
            returned. The default is ``false``.
        enable_word_confidence (bool):
            If ``true``, the top result includes a list of words and the
            confidence for those words. If ``false``, no word-level
            confidence information is returned. The default is
            ``false``.
        enable_automatic_punctuation (bool):
            If ``true``, adds punctuation to recognition result
            hypotheses. This feature is only available in select
            languages. The default ``false`` value does not add
            punctuation to result hypotheses.
        enable_spoken_punctuation (bool):
            The spoken punctuation behavior for the call. If ``true``,
            replaces spoken punctuation with the corresponding symbols
            in the request. For example, "how are you question mark"
            becomes "how are you?". See
            https://cloud.google.com/speech-to-text/docs/spoken-punctuation
            for support. If ``false``, spoken punctuation is not
            replaced.
        enable_spoken_emojis (bool):
            The spoken emoji behavior for the call. If ``true``, adds
            spoken emoji formatting for the request. This will replace
            spoken emojis with the corresponding Unicode symbols in the
            final transcript. If ``false``, spoken emojis are not
            replaced.
        multi_channel_mode (google.cloud.speech_v2.types.RecognitionFeatures.MultiChannelMode):
            Mode for recognizing multi-channel audio.
        diarization_config (google.cloud.speech_v2.types.SpeakerDiarizationConfig):
            Configuration to enable speaker diarization
            and set additional parameters to make
            diarization better suited for your application.
            When this is enabled, we send all the words from
            the beginning of the audio for the top
            alternative in every consecutive STREAMING
            responses. This is done in order to improve our
            speaker tags as our models learn to identify the
            speakers in the conversation over time. For
            non-streaming requests, the diarization results
            will be provided only in the top alternative of
            the FINAL SpeechRecognitionResult.
        max_alternatives (int):
            Maximum number of recognition hypotheses to be returned. The
            server may return fewer than ``max_alternatives``. Valid
            values are ``0``-``30``. A value of ``0`` or ``1`` will
            return a maximum of one. If omitted, will return a maximum
            of one.
    """

    class MultiChannelMode(proto.Enum):
        r"""Options for how to recognize multi-channel audio."""
        MULTI_CHANNEL_MODE_UNSPECIFIED = 0
        SEPARATE_RECOGNITION_PER_CHANNEL = 1

    profanity_filter = proto.Field(
        proto.BOOL,
        number=1,
    )
    enable_word_time_offsets = proto.Field(
        proto.BOOL,
        number=2,
    )
    enable_word_confidence = proto.Field(
        proto.BOOL,
        number=3,
    )
    enable_automatic_punctuation = proto.Field(
        proto.BOOL,
        number=4,
    )
    enable_spoken_punctuation = proto.Field(
        proto.BOOL,
        number=14,
    )
    enable_spoken_emojis = proto.Field(
        proto.BOOL,
        number=15,
    )
    multi_channel_mode = proto.Field(
        proto.ENUM,
        number=17,
        enum=MultiChannelMode,
    )
    diarization_config = proto.Field(
        proto.MESSAGE,
        number=9,
        message="SpeakerDiarizationConfig",
    )
    max_alternatives = proto.Field(
        proto.INT32,
        number=16,
    )


class SpeechAdaptation(proto.Message):
    r"""Provides "hints" to the speech recognizer to favor specific
    words and phrases in the results. Phrase sets can be specified
    as an inline resource, or a reference to an existing phrase set
    resource.

    Attributes:
        phrase_sets (Sequence[google.cloud.speech_v2.types.SpeechAdaptation.AdaptationPhraseSet]):
            A list of inline or referenced phrase sets.
        custom_classes (Sequence[google.cloud.speech_v2.types.CustomClass]):
            A list of inline custom classes. Existing
            custom class resources can be referenced
            directly in a phrase set.
    """

    class AdaptationPhraseSet(proto.Message):
        r"""A biasing phrase set, which can be either a string
        referencing the name of an existing phrase set resource, or an
        inline definition of a phrase set.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            phrase_set (str):
                The name of an existing phrase set resource.
                The user must have read access to the resource
                and it must not be deleted.

                This field is a member of `oneof`_ ``value``.
            inline_phrase_set (google.cloud.speech_v2.types.PhraseSet):
                An inline defined phrase set.

                This field is a member of `oneof`_ ``value``.
        """

        phrase_set = proto.Field(
            proto.STRING,
            number=1,
            oneof="value",
        )
        inline_phrase_set = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="value",
            message="PhraseSet",
        )

    phrase_sets = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=AdaptationPhraseSet,
    )
    custom_classes = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CustomClass",
    )


class RecognitionConfig(proto.Message):
    r"""Provides information to the Recognizer that specifies how to
    process the recognition request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        auto_decoding_config (google.cloud.speech_v2.types.AutoDetectDecodingConfig):
            Automatically detect decoding parameters.
            Preferred for supported formats.

            This field is a member of `oneof`_ ``decoding_config``.
        explicit_decoding_config (google.cloud.speech_v2.types.ExplicitDecodingConfig):
            Explicitly specified decoding parameters.
            Required if using headerless PCM audio
            (linear16, mulaw, alaw).

            This field is a member of `oneof`_ ``decoding_config``.
        features (google.cloud.speech_v2.types.RecognitionFeatures):
            Speech recognition features to enable.
        adaptation (google.cloud.speech_v2.types.SpeechAdaptation):
            Speech adaptation context that weights
            recognizer predictions for specific words and
            phrases.
    """

    auto_decoding_config = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="decoding_config",
        message="AutoDetectDecodingConfig",
    )
    explicit_decoding_config = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="decoding_config",
        message="ExplicitDecodingConfig",
    )
    features = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RecognitionFeatures",
    )
    adaptation = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SpeechAdaptation",
    )


class RecognizeRequest(proto.Message):
    r"""Request message for the
    [Recognize][google.cloud.speech.v2.Speech.Recognize] method. Either
    ``content`` or ``uri`` must be supplied. Supplying both or neither
    returns [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]. See
    `content
    limits <https://cloud.google.com/speech-to-text/quotas#content>`__.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        recognizer (str):
            Required. The name of the Recognizer to use during
            recognition. The expected format is
            ``projects/{project}/locations/{location}/recognizers/{recognizer}``.
        config (google.cloud.speech_v2.types.RecognitionConfig):
            Features and audio metadata to use for the Automatic Speech
            Recognition. This field in combination with the
            [config_mask][google.cloud.speech.v2.RecognizeRequest.config_mask]
            field can be used to override parts of the
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config]
            of the Recognizer resource.
        config_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields in
            [config][google.cloud.speech.v2.RecognizeRequest.config]
            that override the values in the
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config]
            of the recognizer during this recognition request. If no
            mask is provided, all non-default valued fields in
            [config][google.cloud.speech.v2.RecognizeRequest.config]
            override the values in the recognizer for this recognition
            request. If a mask is provided, only the fields listed in
            the mask override the config in the recognizer for this
            recognition request. If a wildcard (``*``) is provided,
            [config][google.cloud.speech.v2.RecognizeRequest.config]
            completely overrides and replaces the config in the
            recognizer for this recognition request.
        content (bytes):
            The audio data bytes encoded as specified in
            [RecognitionConfig][google.cloud.speech.v2.RecognitionConfig].
            As with all bytes fields, proto buffers use a pure binary
            representation, whereas JSON representations use base64.

            This field is a member of `oneof`_ ``audio_source``.
        uri (str):
            URI that points to a file that contains audio data bytes as
            specified in
            [RecognitionConfig][google.cloud.speech.v2.RecognitionConfig].
            The file must not be compressed (for example, gzip).
            Currently, only Google Cloud Storage URIs are supported,
            which must be specified in the following format:
            ``gs://bucket_name/object_name`` (other URI formats return
            [INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]). For
            more information, see `Request
            URIs <https://cloud.google.com/storage/docs/reference-uris>`__.

            This field is a member of `oneof`_ ``audio_source``.
    """

    recognizer = proto.Field(
        proto.STRING,
        number=3,
    )
    config = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RecognitionConfig",
    )
    config_mask = proto.Field(
        proto.MESSAGE,
        number=8,
        message=field_mask_pb2.FieldMask,
    )
    content = proto.Field(
        proto.BYTES,
        number=5,
        oneof="audio_source",
    )
    uri = proto.Field(
        proto.STRING,
        number=6,
        oneof="audio_source",
    )


class RecognitionResponseMetadata(proto.Message):
    r"""Metadata about the recognition request and response.

    Attributes:
        total_billed_duration (google.protobuf.duration_pb2.Duration):
            When available, billed audio seconds for the
            corresponding request.
    """

    total_billed_duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )


class SpeechRecognitionAlternative(proto.Message):
    r"""Alternative hypotheses (a.k.a. n-best list).

    Attributes:
        transcript (str):
            Transcript text representing the words that
            the user spoke.
        confidence (float):
            The confidence estimate between 0.0 and 1.0. A higher number
            indicates an estimated greater likelihood that the
            recognized words are correct. This field is set only for the
            top alternative of a non-streaming result or, of a streaming
            result where
            [is_final][google.cloud.speech.v2.StreamingRecognitionResult.is_final]
            is set to ``true``. This field is not guaranteed to be
            accurate and users should not rely on it to be always
            provided. The default of 0.0 is a sentinel value indicating
            ``confidence`` was not set.
        words (Sequence[google.cloud.speech_v2.types.WordInfo]):
            A list of word-specific information for each recognized
            word. When
            [enable_speaker_diarization][google.cloud.speech.v2.SpeakerDiarizationConfig.enable_speaker_diarization]
            is true, you will see all the words from the beginning of
            the audio.
    """

    transcript = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence = proto.Field(
        proto.FLOAT,
        number=2,
    )
    words = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="WordInfo",
    )


class WordInfo(proto.Message):
    r"""Word-specific information for recognized words.

    Attributes:
        start_offset (google.protobuf.duration_pb2.Duration):
            Time offset relative to the beginning of the audio, and
            corresponding to the start of the spoken word. This field is
            only set if
            [enable_word_time_offsets][google.cloud.speech.v2.RecognitionFeatures.enable_word_time_offsets]
            is ``true`` and only in the top hypothesis. This is an
            experimental feature and the accuracy of the time offset can
            vary.
        end_offset (google.protobuf.duration_pb2.Duration):
            Time offset relative to the beginning of the audio, and
            corresponding to the end of the spoken word. This field is
            only set if
            [enable_word_time_offsets][google.cloud.speech.v2.RecognitionFeatures.enable_word_time_offsets]
            is ``true`` and only in the top hypothesis. This is an
            experimental feature and the accuracy of the time offset can
            vary.
        word (str):
            The word corresponding to this set of
            information.
        confidence (float):
            The confidence estimate between 0.0 and 1.0. A higher number
            indicates an estimated greater likelihood that the
            recognized words are correct. This field is set only for the
            top alternative of a non-streaming result or, of a streaming
            result where
            [is_final][google.cloud.speech.v2.StreamingRecognitionResult.is_final]
            is set to ``true``. This field is not guaranteed to be
            accurate and users should not rely on it to be always
            provided. The default of 0.0 is a sentinel value indicating
            ``confidence`` was not set.
        speaker_label (str):
            A distinct label is assigned for every speaker within the
            audio. This field specifies which one of those speakers was
            detected to have spoken this word. ``speaker_label`` is set
            if
            [enable_speaker_diarization][google.cloud.speech.v2.SpeakerDiarizationConfig.enable_speaker_diarization]
            is ``true`` and only in the top alternative.
    """

    start_offset = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    end_offset = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    word = proto.Field(
        proto.STRING,
        number=3,
    )
    confidence = proto.Field(
        proto.FLOAT,
        number=4,
    )
    speaker_label = proto.Field(
        proto.STRING,
        number=6,
    )


class SpeechRecognitionResult(proto.Message):
    r"""A speech recognition result corresponding to a portion of the
    audio.

    Attributes:
        alternatives (Sequence[google.cloud.speech_v2.types.SpeechRecognitionAlternative]):
            May contain one or more recognition
            hypotheses. These alternatives are ordered in
            terms of accuracy, with the top (first)
            alternative being the most probable, as ranked
            by the recognizer.
        channel_tag (int):
            For multi-channel audio, this is the channel number
            corresponding to the recognized result for the audio from
            that channel. For ``audio_channel_count`` = ``N``, its
            output values can range from ``1`` to ``N``.
        result_end_offset (google.protobuf.duration_pb2.Duration):
            Time offset of the end of this result
            relative to the beginning of the audio.
        language_code (str):
            Output only. The
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag of the language in this result. This language
            code was detected to have the most likelihood of being
            spoken in the audio.
    """

    alternatives = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SpeechRecognitionAlternative",
    )
    channel_tag = proto.Field(
        proto.INT32,
        number=2,
    )
    result_end_offset = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    language_code = proto.Field(
        proto.STRING,
        number=5,
    )


class RecognizeResponse(proto.Message):
    r"""Response message for the
    [Recognize][google.cloud.speech.v2.Speech.Recognize] method.

    Attributes:
        results (Sequence[google.cloud.speech_v2.types.SpeechRecognitionResult]):
            Sequential list of transcription results
            corresponding to sequential portions of audio.
        metadata (google.cloud.speech_v2.types.RecognitionResponseMetadata):
            Metadata about the recognition.
    """

    results = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SpeechRecognitionResult",
    )
    metadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RecognitionResponseMetadata",
    )


class StreamingRecognitionFeatures(proto.Message):
    r"""Available recognition features specific to streaming
    recognition requests.

    Attributes:
        enable_voice_activity_events (bool):
            If ``true``, responses with voice activity speech events
            will be returned as they are detected.
        interim_results (bool):
            Whether or not to stream interim results to
            the client. If set to true, interim results will
            be streamed to the client. Otherwise, only the
            final response will be streamed back.
        voice_activity_timeout (google.cloud.speech_v2.types.StreamingRecognitionFeatures.VoiceActivityTimeout):
            If set, the server will automatically close the stream after
            the specified duration has elapsed after the last
            VOICE_ACTIVITY speech event has been sent. The field
            ``voice_activity_events`` must also be set to true.
    """

    class VoiceActivityTimeout(proto.Message):
        r"""Events that a timeout can be set on for voice activity.

        Attributes:
            speech_start_timeout (google.protobuf.duration_pb2.Duration):
                Duration to timeout the stream if no speech
                begins. If this is set and no speech is detected
                in this duration at the start of the stream, the
                server will close the stream.
            speech_end_timeout (google.protobuf.duration_pb2.Duration):
                Duration to timeout the stream after speech
                ends. If this is set and no speech is detected
                in this duration after speech was detected, the
                server will close the stream.
        """

        speech_start_timeout = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        speech_end_timeout = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    enable_voice_activity_events = proto.Field(
        proto.BOOL,
        number=1,
    )
    interim_results = proto.Field(
        proto.BOOL,
        number=2,
    )
    voice_activity_timeout = proto.Field(
        proto.MESSAGE,
        number=3,
        message=VoiceActivityTimeout,
    )


class StreamingRecognitionConfig(proto.Message):
    r"""Provides configuration information for the StreamingRecognize
    request.

    Attributes:
        config (google.cloud.speech_v2.types.RecognitionConfig):
            Required. Features and audio metadata to use for the
            Automatic Speech Recognition. This field in combination with
            the
            [config_mask][google.cloud.speech.v2.StreamingRecognitionConfig.config_mask]
            field can be used to override parts of the
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config]
            of the Recognizer resource.
        config_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields in
            [config][google.cloud.speech.v2.StreamingRecognitionConfig.config]
            that override the values in the
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config]
            of the recognizer during this recognition request. If no
            mask is provided, all non-default valued fields in
            [config][google.cloud.speech.v2.StreamingRecognitionConfig.config]
            override the values in the recognizer for this recognition
            request. If a mask is provided, only the fields listed in
            the mask override the config in the recognizer for this
            recognition request. If a wildcard (``*``) is provided,
            [config][google.cloud.speech.v2.StreamingRecognitionConfig.config]
            completely overrides and replaces the config in the
            recognizer for this recognition request.
        streaming_features (google.cloud.speech_v2.types.StreamingRecognitionFeatures):
            Speech recognition features to enable
            specific to streaming audio recognition
            requests.
    """

    config = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RecognitionConfig",
    )
    config_mask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )
    streaming_features = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StreamingRecognitionFeatures",
    )


class StreamingRecognizeRequest(proto.Message):
    r"""Request message for the
    [StreamingRecognize][google.cloud.speech.v2.Speech.StreamingRecognize]
    method. Multiple
    [StreamingRecognizeRequest][google.cloud.speech.v2.StreamingRecognizeRequest]
    messages are sent. The first message must contain a
    [recognizer][google.cloud.speech.v2.StreamingRecognizeRequest.recognizer]
    and optionally a
    [streaming_config][google.cloud.speech.v2.StreamingRecognizeRequest.streaming_config]
    message and must not contain
    [audio][google.cloud.speech.v2.StreamingRecognizeRequest.audio]. All
    subsequent messages must contain
    [audio][google.cloud.speech.v2.StreamingRecognizeRequest.audio] and
    must not contain a
    [streaming_config][google.cloud.speech.v2.StreamingRecognizeRequest.streaming_config]
    message.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        recognizer (str):
            Required. Streaming recognition should start with an initial
            request having a ``recognizer``. Subsequent requests carry
            the audio data to be recognized.

            The initial request with configuration can be omitted if the
            Recognizer being used has a
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config].
        streaming_config (google.cloud.speech_v2.types.StreamingRecognitionConfig):
            StreamingRecognitionConfig to be used in this
            recognition attempt. If provided, it will
            override the default RecognitionConfig stored in
            the Recognizer.

            This field is a member of `oneof`_ ``streaming_request``.
        audio (bytes):
            Inline audio bytes to be Recognized.

            This field is a member of `oneof`_ ``streaming_request``.
    """

    recognizer = proto.Field(
        proto.STRING,
        number=3,
    )
    streaming_config = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="streaming_request",
        message="StreamingRecognitionConfig",
    )
    audio = proto.Field(
        proto.BYTES,
        number=5,
        oneof="streaming_request",
    )


class BatchRecognizeRequest(proto.Message):
    r"""Request message for the
    [BatchRecognize][google.cloud.speech.v2.Speech.BatchRecognize]
    method.

    Attributes:
        recognizer (str):
            Required. Resource name of the recognizer to
            be used for ASR.
        config (google.cloud.speech_v2.types.RecognitionConfig):
            Features and audio metadata to use for the Automatic Speech
            Recognition. This field in combination with the
            [config_mask][google.cloud.speech.v2.BatchRecognizeRequest.config_mask]
            field can be used to override parts of the
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config]
            of the Recognizer resource.
        config_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields in
            [config][google.cloud.speech.v2.BatchRecognizeRequest.config]
            that override the values in the
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config]
            of the recognizer during this recognition request. If no
            mask is provided, all given fields in
            [config][google.cloud.speech.v2.BatchRecognizeRequest.config]
            override the values in the recognizer for this recognition
            request. If a mask is provided, only the fields listed in
            the mask override the config in the recognizer for this
            recognition request. If a wildcard (``*``) is provided,
            [config][google.cloud.speech.v2.BatchRecognizeRequest.config]
            completely overrides and replaces the config in the
            recognizer for this recognition request.
        files (Sequence[google.cloud.speech_v2.types.BatchRecognizeFileMetadata]):
            Audio files with file metadata for ASR.
    """

    recognizer = proto.Field(
        proto.STRING,
        number=1,
    )
    config = proto.Field(
        proto.MESSAGE,
        number=4,
        message="RecognitionConfig",
    )
    config_mask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )
    files = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="BatchRecognizeFileMetadata",
    )


class BatchRecognizeResponse(proto.Message):
    r"""Response message for
    [BatchRecognize][google.cloud.speech.v2.Speech.BatchRecognize] that
    is packaged into a longrunning
    [Operation][google.longrunning.Operation].

    Attributes:
        results (Mapping[str, google.cloud.speech_v2.types.BatchRecognizeFileResult]):
            Map from filename to the final result for
            that file.
    """

    results = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="BatchRecognizeFileResult",
    )


class BatchRecognizeFileResult(proto.Message):
    r"""Final results for a single file.

    Attributes:
        uri (str):
            The GCS URI to which recognition results were
            written.
        error (google.rpc.status_pb2.Status):
            Error if one was encountered.
    """

    uri = proto.Field(
        proto.STRING,
        number=1,
    )
    error = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )


class BatchRecognizeTranscriptionMetadata(proto.Message):
    r"""Metadata about transcription for a single file (for example,
    progress percent).

    Attributes:
        progress_percent (int):
            How much of the file has been transcribed so
            far.
        error (google.rpc.status_pb2.Status):
            Error if one was encountered.
        uri (str):
            The GCS URI to which recognition results will
            be written.
    """

    progress_percent = proto.Field(
        proto.INT32,
        number=1,
    )
    error = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    uri = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchRecognizeMetadata(proto.Message):
    r"""Operation metadata for
    [BatchRecognize][google.cloud.speech.v2.Speech.BatchRecognize].

    Attributes:
        transcription_metadata (Mapping[str, google.cloud.speech_v2.types.BatchRecognizeTranscriptionMetadata]):
            Map from provided filename to the
            transcription metadata for that file.
    """

    transcription_metadata = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="BatchRecognizeTranscriptionMetadata",
    )


class BatchRecognizeFileMetadata(proto.Message):
    r"""Metadata about a single file in a batch for BatchRecognize.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            Cloud Storage URI for the audio file.

            This field is a member of `oneof`_ ``audio_source``.
        config (google.cloud.speech_v2.types.RecognitionConfig):
            Features and audio metadata to use for the Automatic Speech
            Recognition. This field in combination with the
            [config_mask][google.cloud.speech.v2.BatchRecognizeFileMetadata.config_mask]
            field can be used to override parts of the
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config]
            of the Recognizer resource as well as the
            [config][google.cloud.speech.v2.BatchRecognizeRequest.config]
            at the request level.
        config_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields in
            [config][google.cloud.speech.v2.BatchRecognizeFileMetadata.config]
            that override the values in the
            [default_recognition_config][google.cloud.speech.v2.Recognizer.default_recognition_config]
            of the recognizer during this recognition request. If no
            mask is provided, all non-default valued fields in
            [config][google.cloud.speech.v2.BatchRecognizeFileMetadata.config]
            override the values in the recognizer for this recognition
            request. If a mask is provided, only the fields listed in
            the mask override the config in the recognizer for this
            recognition request. If a wildcard (``*``) is provided,
            [config][google.cloud.speech.v2.BatchRecognizeFileMetadata.config]
            completely overrides and replaces the config in the
            recognizer for this recognition request.
    """

    uri = proto.Field(
        proto.STRING,
        number=1,
        oneof="audio_source",
    )
    config = proto.Field(
        proto.MESSAGE,
        number=4,
        message="RecognitionConfig",
    )
    config_mask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )


class StreamingRecognitionResult(proto.Message):
    r"""A streaming speech recognition result corresponding to a
    portion of the audio that is currently being processed.

    Attributes:
        alternatives (Sequence[google.cloud.speech_v2.types.SpeechRecognitionAlternative]):
            May contain one or more recognition
            hypotheses. These alternatives are ordered in
            terms of accuracy, with the top (first)
            alternative being the most probable, as ranked
            by the recognizer.
        is_final (bool):
            If ``false``, this
            [StreamingRecognitionResult][google.cloud.speech.v2.StreamingRecognitionResult]
            represents an interim result that may change. If ``true``,
            this is the final time the speech service will return this
            particular
            [StreamingRecognitionResult][google.cloud.speech.v2.StreamingRecognitionResult],
            the recognizer will not return any further hypotheses for
            this portion of the transcript and corresponding audio.
        stability (float):
            An estimate of the likelihood that the recognizer will not
            change its guess about this interim result. Values range
            from 0.0 (completely unstable) to 1.0 (completely stable).
            This field is only provided for interim results
            ([is_final][google.cloud.speech.v2.StreamingRecognitionResult.is_final]=``false``).
            The default of 0.0 is a sentinel value indicating
            ``stability`` was not set.
        result_end_offset (google.protobuf.duration_pb2.Duration):
            Time offset of the end of this result
            relative to the beginning of the audio.
        channel_tag (int):
            For multi-channel audio, this is the channel number
            corresponding to the recognized result for the audio from
            that channel. For ``audio_channel_count`` = ``N``, its
            output values can range from ``1`` to ``N``.
        language_code (str):
            Output only. The
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag of the language in this result. This language
            code was detected to have the most likelihood of being
            spoken in the audio.
    """

    alternatives = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SpeechRecognitionAlternative",
    )
    is_final = proto.Field(
        proto.BOOL,
        number=2,
    )
    stability = proto.Field(
        proto.FLOAT,
        number=3,
    )
    result_end_offset = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    channel_tag = proto.Field(
        proto.INT32,
        number=5,
    )
    language_code = proto.Field(
        proto.STRING,
        number=6,
    )


class StreamingRecognizeResponse(proto.Message):
    r"""``StreamingRecognizeResponse`` is the only message returned to the
    client by ``StreamingRecognize``. A series of zero or more
    ``StreamingRecognizeResponse`` messages are streamed back to the
    client. If there is no recognizable audio then no messages are
    streamed back to the client.

    Here are some examples of ``StreamingRecognizeResponse``\ s that
    might be returned while processing audio:

    1. results { alternatives { transcript: "tube" } stability: 0.01 }

    2. results { alternatives { transcript: "to be a" } stability: 0.01
       }

    3. results { alternatives { transcript: "to be" } stability: 0.9 }
       results { alternatives { transcript: " or not to be" } stability:
       0.01 }

    4. results { alternatives { transcript: "to be or not to be"
       confidence: 0.92 } alternatives { transcript: "to bee or not to
       bee" } is_final: true }

    5. results { alternatives { transcript: " that's" } stability: 0.01
       }

    6. results { alternatives { transcript: " that is" } stability: 0.9
       } results { alternatives { transcript: " the question" }
       stability: 0.01 }

    7. results { alternatives { transcript: " that is the question"
       confidence: 0.98 } alternatives { transcript: " that was the
       question" } is_final: true }

    Notes:

    -  Only two of the above responses #4 and #7 contain final results;
       they are indicated by ``is_final: true``. Concatenating these
       together generates the full transcript: "to be or not to be that
       is the question".

    -  The others contain interim ``results``. #3 and #6 contain two
       interim ``results``: the first portion has a high stability and
       is less likely to change; the second portion has a low stability
       and is very likely to change. A UI designer might choose to show
       only high stability ``results``.

    -  The specific ``stability`` and ``confidence`` values shown above
       are only for illustrative purposes. Actual values may vary.

    -  In each response, only one of these fields will be set:
       ``error``, ``speech_event_type``, or one or more (repeated)
       ``results``.

    Attributes:
        results (Sequence[google.cloud.speech_v2.types.StreamingRecognitionResult]):
            This repeated list contains zero or more results that
            correspond to consecutive portions of the audio currently
            being processed. It contains zero or one
            [is_final][google.cloud.speech.v2.StreamingRecognitionResult.is_final]=``true``
            result (the newly settled portion), followed by zero or more
            [is_final][google.cloud.speech.v2.StreamingRecognitionResult.is_final]=``false``
            results (the interim results).
        speech_event_type (google.cloud.speech_v2.types.StreamingRecognizeResponse.SpeechEventType):
            Indicates the type of speech event.
        speech_event_offset (google.protobuf.duration_pb2.Duration):
            Time offset between the beginning of the
            audio and event emission.
        metadata (google.cloud.speech_v2.types.RecognitionResponseMetadata):
            Metadata about the recognition.
    """

    class SpeechEventType(proto.Enum):
        r"""Indicates the type of speech event."""
        SPEECH_EVENT_TYPE_UNSPECIFIED = 0
        END_OF_SINGLE_UTTERANCE = 1
        SPEECH_ACTIVITY_BEGIN = 2
        SPEECH_ACTIVITY_END = 3

    results = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="StreamingRecognitionResult",
    )
    speech_event_type = proto.Field(
        proto.ENUM,
        number=3,
        enum=SpeechEventType,
    )
    speech_event_offset = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    metadata = proto.Field(
        proto.MESSAGE,
        number=5,
        message="RecognitionResponseMetadata",
    )


class Config(proto.Message):
    r"""Message representing the config for the Speech-to-Text API. This
    includes an optional `KMS
    key <https://cloud.google.com/kms/docs/resource-hierarchy#keys>`__
    with which incoming data will be encrypted.

    Attributes:
        name (str):
            Output only. The name of the config resource. There is
            exactly one config resource per project per location. The
            expected format is
            ``projects/{project}/locations/{location}/config``.
        kms_key_name (str):
            Optional. An optional `KMS key
            name <https://cloud.google.com/kms/docs/resource-hierarchy#keys>`__
            that if present, will be used to encrypt Speech-to-Text
            resources at-rest. Updating this key will not encrypt
            existing resources using this key; only new resources will
            be encrypted using this key. The expected format is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time this
            resource was modified.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key_name = proto.Field(
        proto.STRING,
        number=2,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class GetConfigRequest(proto.Message):
    r"""Request message for the
    [GetConfig][google.cloud.speech.v2.Speech.GetConfig] method.

    Attributes:
        name (str):
            Required. The name of the config to retrieve. There is
            exactly one config resource per project per location. The
            expected format is
            ``projects/{project}/locations/{location}/config``.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateConfigRequest(proto.Message):
    r"""Request message for the
    [UpdateConfig][google.cloud.speech.v2.Speech.UpdateConfig] method.

    Attributes:
        config (google.cloud.speech_v2.types.Config):
            Required. The config to update.

            The config's ``name`` field is used to identify the config
            to be updated. The expected format is
            ``projects/{project}/locations/{location}/config``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    config = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Config",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CustomClass(proto.Message):
    r"""CustomClass for biasing in speech recognition. Used to define
    a set of words or phrases that represents a common concept or
    theme likely to appear in your audio, for example a list of
    passenger ship names.

    Attributes:
        name (str):
            Output only. The resource name of the CustomClass. Format:
            ``projects/{project}/locations/{location}/customClasses/{custom_class}``.
        uid (str):
            Output only. System-assigned unique
            identifier for the CustomClass.
        display_name (str):
            User-settable, human-readable name for the
            CustomClass. Must be 63 characters or less.
        items (Sequence[google.cloud.speech_v2.types.CustomClass.ClassItem]):
            A collection of class items.
        state (google.cloud.speech_v2.types.CustomClass.State):
            Output only. The CustomClass lifecycle state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time this
            resource was modified.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this resource
            was requested for deletion.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this resource
            will be purged.
        annotations (Mapping[str, str]):
            Allows users to store small amounts of
            arbitrary data. Both the key and the value must
            be 63 characters or less each. At most 100
            annotations.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields. This
            may be sent on update, undelete, and delete
            requests to ensure the client has an up-to-date
            value before proceeding.
        reconciling (bool):
            Output only. Whether or not this CustomClass
            is in the process of being updated.
        kms_key_name (str):
            Output only. The `KMS key
            name <https://cloud.google.com/kms/docs/resource-hierarchy#keys>`__
            with which the CustomClass is encrypted. The expected format
            is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.
        kms_key_version_name (str):
            Output only. The `KMS key version
            name <https://cloud.google.com/kms/docs/resource-hierarchy#key_versions>`__
            with which the CustomClass is encrypted. The expected format
            is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}``.
    """

    class State(proto.Enum):
        r"""Set of states that define the lifecycle of a CustomClass."""
        STATE_UNSPECIFIED = 0
        ACTIVE = 2
        DELETED = 4

    class ClassItem(proto.Message):
        r"""An item of the class.

        Attributes:
            value (str):
                The class item's value.
        """

        value = proto.Field(
            proto.STRING,
            number=1,
        )

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    uid = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name = proto.Field(
        proto.STRING,
        number=4,
    )
    items = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=ClassItem,
    )
    state = proto.Field(
        proto.ENUM,
        number=15,
        enum=State,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    delete_time = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    expire_time = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    annotations = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    etag = proto.Field(
        proto.STRING,
        number=11,
    )
    reconciling = proto.Field(
        proto.BOOL,
        number=12,
    )
    kms_key_name = proto.Field(
        proto.STRING,
        number=13,
    )
    kms_key_version_name = proto.Field(
        proto.STRING,
        number=14,
    )


class PhraseSet(proto.Message):
    r"""PhraseSet for biasing in speech recognition. A PhraseSet is
    used to provide "hints" to the speech recognizer to favor
    specific words and phrases in the results.

    Attributes:
        name (str):
            Output only. The resource name of the PhraseSet. Format:
            ``projects/{project}/locations/{location}/phraseSets/{phrase_set}``.
        uid (str):
            Output only. System-assigned unique
            identifier for the PhraseSet.
        phrases (Sequence[google.cloud.speech_v2.types.PhraseSet.Phrase]):
            A list of word and phrases.
        boost (float):
            Hint Boost. Positive value will increase the probability
            that a specific phrase will be recognized over other similar
            sounding phrases. The higher the boost, the higher the
            chance of false positive recognition as well. Valid
            ``boost`` values are between 0 (exclusive) and 20. We
            recommend using a binary search approach to finding the
            optimal value for your use case.
        display_name (str):
            User-settable, human-readable name for the
            PhraseSet. Must be 63 characters or less.
        state (google.cloud.speech_v2.types.PhraseSet.State):
            Output only. The PhraseSet lifecycle state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time this
            resource was modified.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this resource
            was requested for deletion.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this resource
            will be purged.
        annotations (Mapping[str, str]):
            Allows users to store small amounts of
            arbitrary data. Both the key and the value must
            be 63 characters or less each. At most 100
            annotations.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields. This
            may be sent on update, undelete, and delete
            requests to ensure the client has an up-to-date
            value before proceeding.
        reconciling (bool):
            Output only. Whether or not this PhraseSet is
            in the process of being updated.
        kms_key_name (str):
            Output only. The `KMS key
            name <https://cloud.google.com/kms/docs/resource-hierarchy#keys>`__
            with which the PhraseSet is encrypted. The expected format
            is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.
        kms_key_version_name (str):
            Output only. The `KMS key version
            name <https://cloud.google.com/kms/docs/resource-hierarchy#key_versions>`__
            with which the PhraseSet is encrypted. The expected format
            is
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}``.
    """

    class State(proto.Enum):
        r"""Set of states that define the lifecycle of a PhraseSet."""
        STATE_UNSPECIFIED = 0
        ACTIVE = 2
        DELETED = 4

    class Phrase(proto.Message):
        r"""A Phrase contains words and phrase "hints" so that the speech
        recognition is more likely to recognize them. This can be used
        to improve the accuracy for specific words and phrases, for
        example, if specific commands are typically spoken by the user.
        This can also be used to add additional words to the vocabulary
        of the recognizer.

        List items can also include CustomClass references containing
        groups of words that represent common concepts that occur in
        natural language.

        Attributes:
            value (str):
                The phrase itself.
            boost (float):
                Hint Boost. Overrides the boost set at the phrase set level.
                Positive value will increase the probability that a specific
                phrase will be recognized over other similar sounding
                phrases. The higher the boost, the higher the chance of
                false positive recognition as well. Negative boost values
                would correspond to anti-biasing. Anti-biasing is not
                enabled, so negative boost will simply be ignored. Though
                ``boost`` can accept a wide range of positive values, most
                use cases are best served with values between 0 and 20. We
                recommend using a binary search approach to finding the
                optimal value for your use case. Speech recognition will
                skip PhraseSets with a boost value of 0.
        """

        value = proto.Field(
            proto.STRING,
            number=1,
        )
        boost = proto.Field(
            proto.FLOAT,
            number=2,
        )

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    uid = proto.Field(
        proto.STRING,
        number=2,
    )
    phrases = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Phrase,
    )
    boost = proto.Field(
        proto.FLOAT,
        number=4,
    )
    display_name = proto.Field(
        proto.STRING,
        number=5,
    )
    state = proto.Field(
        proto.ENUM,
        number=15,
        enum=State,
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    delete_time = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    expire_time = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    annotations = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    etag = proto.Field(
        proto.STRING,
        number=11,
    )
    reconciling = proto.Field(
        proto.BOOL,
        number=12,
    )
    kms_key_name = proto.Field(
        proto.STRING,
        number=13,
    )
    kms_key_version_name = proto.Field(
        proto.STRING,
        number=14,
    )


class CreateCustomClassRequest(proto.Message):
    r"""Request message for the
    [CreateCustomClass][google.cloud.speech.v2.Speech.CreateCustomClass]
    method.

    Attributes:
        custom_class (google.cloud.speech_v2.types.CustomClass):
            Required. The CustomClass to create.
        validate_only (bool):
            If set, validate the request and preview the
            CustomClass, but do not actually create it.
        custom_class_id (str):
            The ID to use for the CustomClass, which will become the
            final component of the CustomClass's resource name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-/.
        parent (str):
            Required. The project and location where this CustomClass
            will be created. The expected format is
            ``projects/{project}/locations/{location}``.
    """

    custom_class = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CustomClass",
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    custom_class_id = proto.Field(
        proto.STRING,
        number=3,
    )
    parent = proto.Field(
        proto.STRING,
        number=4,
    )


class ListCustomClassesRequest(proto.Message):
    r"""Request message for the
    [ListCustomClasses][google.cloud.speech.v2.Speech.ListCustomClasses]
    method.

    Attributes:
        parent (str):
            Required. The project and location of CustomClass resources
            to list. The expected format is
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Number of results per requests. A valid page_size ranges
            from 0 to 20 inclusive. If the page_size is zero or
            unspecified, a page size of 5 will be chosen. If the page
            size exceeds 20, it will be coerced down to 20. Note that a
            call might return fewer results than the requested page
            size.
        page_token (str):
            A page token, received from a previous
            [ListCustomClasses][google.cloud.speech.v2.Speech.ListCustomClasses]
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            [ListCustomClasses][google.cloud.speech.v2.Speech.ListCustomClasses]
            must match the call that provided the page token.
        show_deleted (bool):
            Whether, or not, to show resources that have
            been deleted.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )
    show_deleted = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListCustomClassesResponse(proto.Message):
    r"""Response message for the
    [ListCustomClasses][google.cloud.speech.v2.Speech.ListCustomClasses]
    method.

    Attributes:
        custom_classes (Sequence[google.cloud.speech_v2.types.CustomClass]):
            The list of requested CustomClasses.
        next_page_token (str):
            A token, which can be sent as
            [page_token][google.cloud.speech.v2.ListCustomClassesRequest.page_token]
            to retrieve the next page. If this field is omitted, there
            are no subsequent pages. This token expires after 72 hours.
    """

    @property
    def raw_page(self):
        return self

    custom_classes = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CustomClass",
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class GetCustomClassRequest(proto.Message):
    r"""Request message for the
    [GetCustomClass][google.cloud.speech.v2.Speech.GetCustomClass]
    method.

    Attributes:
        name (str):
            Required. The name of the CustomClass to retrieve. The
            expected format is
            ``projects/{project}/locations/{location}/customClasses/{custom_class}``.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateCustomClassRequest(proto.Message):
    r"""Request message for the
    [UpdateCustomClass][google.cloud.speech.v2.Speech.UpdateCustomClass]
    method.

    Attributes:
        custom_class (google.cloud.speech_v2.types.CustomClass):
            Required. The CustomClass to update.

            The CustomClass's ``name`` field is used to identify the
            CustomClass to update. Format:
            ``projects/{project}/locations/{location}/customClasses/{custom_class}``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated. If empty,
            all fields are considered for update.
        validate_only (bool):
            If set, validate the request and preview the
            updated CustomClass, but do not actually update
            it.
    """

    custom_class = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CustomClass",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeleteCustomClassRequest(proto.Message):
    r"""Request message for the
    [DeleteCustomClass][google.cloud.speech.v2.Speech.DeleteCustomClass]
    method.

    Attributes:
        name (str):
            Required. The name of the CustomClass to delete. Format:
            ``projects/{project}/locations/{location}/customClasses/{custom_class}``
        validate_only (bool):
            If set, validate the request and preview the
            deleted CustomClass, but do not actually delete
            it.
        allow_missing (bool):
            If set to true, and the CustomClass is not
            found, the request will succeed and  be a no-op
            (no Operation is recorded in this case).
        etag (str):
            This checksum is computed by the server based
            on the value of other fields. This may be sent
            on update, undelete, and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    allow_missing = proto.Field(
        proto.BOOL,
        number=4,
    )
    etag = proto.Field(
        proto.STRING,
        number=3,
    )


class UndeleteCustomClassRequest(proto.Message):
    r"""Request message for the
    [UndeleteCustomClass][google.cloud.speech.v2.Speech.UndeleteCustomClass]
    method.

    Attributes:
        name (str):
            Required. The name of the CustomClass to undelete. Format:
            ``projects/{project}/locations/{location}/customClasses/{custom_class}``
        validate_only (bool):
            If set, validate the request and preview the
            undeleted CustomClass, but do not actually
            undelete it.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields. This may be sent
            on update, undelete, and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag = proto.Field(
        proto.STRING,
        number=4,
    )


class CreatePhraseSetRequest(proto.Message):
    r"""Request message for the
    [CreatePhraseSet][google.cloud.speech.v2.Speech.CreatePhraseSet]
    method.

    Attributes:
        phrase_set (google.cloud.speech_v2.types.PhraseSet):
            Required. The PhraseSet to create.
        validate_only (bool):
            If set, validate the request and preview the
            PhraseSet, but do not actually create it.
        phrase_set_id (str):
            The ID to use for the PhraseSet, which will become the final
            component of the PhraseSet's resource name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-/.
        parent (str):
            Required. The project and location where this PhraseSet will
            be created. The expected format is
            ``projects/{project}/locations/{location}``.
    """

    phrase_set = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PhraseSet",
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    phrase_set_id = proto.Field(
        proto.STRING,
        number=3,
    )
    parent = proto.Field(
        proto.STRING,
        number=4,
    )


class ListPhraseSetsRequest(proto.Message):
    r"""Request message for the
    [ListPhraseSets][google.cloud.speech.v2.Speech.ListPhraseSets]
    method.

    Attributes:
        parent (str):
            Required. The project and location of PhraseSet resources to
            list. The expected format is
            ``projects/{project}/locations/{location}``.
        page_size (int):
            The maximum number of PhraseSets to return.
            The service may return fewer than this value. If
            unspecified, at most 20 PhraseSets will be
            returned. The maximum value is 20; values above
            20 will be coerced to 20.
        page_token (str):
            A page token, received from a previous
            [ListPhraseSets][google.cloud.speech.v2.Speech.ListPhraseSets]
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            [ListPhraseSets][google.cloud.speech.v2.Speech.ListPhraseSets]
            must match the call that provided the page token.
        show_deleted (bool):
            Whether, or not, to show resources that have
            been deleted.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )
    show_deleted = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListPhraseSetsResponse(proto.Message):
    r"""Response message for the
    [ListPhraseSets][google.cloud.speech.v2.Speech.ListPhraseSets]
    method.

    Attributes:
        phrase_sets (Sequence[google.cloud.speech_v2.types.PhraseSet]):
            The list of requested PhraseSets.
        next_page_token (str):
            A token, which can be sent as
            [page_token][google.cloud.speech.v2.ListPhraseSetsRequest.page_token]
            to retrieve the next page. If this field is omitted, there
            are no subsequent pages. This token expires after 72 hours.
    """

    @property
    def raw_page(self):
        return self

    phrase_sets = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PhraseSet",
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPhraseSetRequest(proto.Message):
    r"""Request message for the
    [GetPhraseSet][google.cloud.speech.v2.Speech.GetPhraseSet] method.

    Attributes:
        name (str):
            Required. The name of the PhraseSet to retrieve. The
            expected format is
            ``projects/{project}/locations/{location}/phraseSets/{phrase_set}``.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePhraseSetRequest(proto.Message):
    r"""Request message for the
    [UpdatePhraseSet][google.cloud.speech.v2.Speech.UpdatePhraseSet]
    method.

    Attributes:
        phrase_set (google.cloud.speech_v2.types.PhraseSet):
            Required. The PhraseSet to update.

            The PhraseSet's ``name`` field is used to identify the
            PhraseSet to update. Format:
            ``projects/{project}/locations/{location}/phraseSets/{phrase_set}``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. If empty, all non-default
            valued fields are considered for update. Use ``*`` to update
            the entire PhraseSet resource.
        validate_only (bool):
            If set, validate the request and preview the
            updated PhraseSet, but do not actually update
            it.
    """

    phrase_set = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PhraseSet",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeletePhraseSetRequest(proto.Message):
    r"""Request message for the
    [DeletePhraseSet][google.cloud.speech.v2.Speech.DeletePhraseSet]
    method.

    Attributes:
        name (str):
            Required. The name of the PhraseSet to delete. Format:
            ``projects/{project}/locations/{location}/phraseSets/{phrase_set}``
        validate_only (bool):
            If set, validate the request and preview the
            deleted PhraseSet, but do not actually delete
            it.
        allow_missing (bool):
            If set to true, and the PhraseSet is not
            found, the request will succeed and  be a no-op
            (no Operation is recorded in this case).
        etag (str):
            This checksum is computed by the server based
            on the value of other fields. This may be sent
            on update, undelete, and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    allow_missing = proto.Field(
        proto.BOOL,
        number=4,
    )
    etag = proto.Field(
        proto.STRING,
        number=3,
    )


class UndeletePhraseSetRequest(proto.Message):
    r"""Request message for the
    [UndeletePhraseSet][google.cloud.speech.v2.Speech.UndeletePhraseSet]
    method.

    Attributes:
        name (str):
            Required. The name of the PhraseSet to undelete. Format:
            ``projects/{project}/locations/{location}/phraseSets/{phrase_set}``
        validate_only (bool):
            If set, validate the request and preview the
            undeleted PhraseSet, but do not actually
            undelete it.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields. This may be sent
            on update, undelete, and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
