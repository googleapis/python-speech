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

from google.cloud.speech_v1.services.speech.async_client import SpeechAsyncClient
from google.cloud.speech_v1 import SpeechClient
from google.cloud.speech_v1.types.cloud_speech import LongRunningRecognizeMetadata
from google.cloud.speech_v1.types.cloud_speech import LongRunningRecognizeRequest
from google.cloud.speech_v1.types.cloud_speech import LongRunningRecognizeResponse
from google.cloud.speech_v1.types.cloud_speech import RecognitionAudio
from google.cloud.speech_v1.types.cloud_speech import RecognitionConfig
from google.cloud.speech_v1.types.cloud_speech import RecognitionMetadata
from google.cloud.speech_v1.types.cloud_speech import RecognizeRequest
from google.cloud.speech_v1.types.cloud_speech import RecognizeResponse
from google.cloud.speech_v1.types.cloud_speech import SpeakerDiarizationConfig
from google.cloud.speech_v1.types.cloud_speech import SpeechContext
from google.cloud.speech_v1.types.cloud_speech import SpeechRecognitionAlternative
from google.cloud.speech_v1.types.cloud_speech import SpeechRecognitionResult
from google.cloud.speech_v1.types.cloud_speech import StreamingRecognitionConfig
from google.cloud.speech_v1.types.cloud_speech import StreamingRecognitionResult
from google.cloud.speech_v1.types.cloud_speech import StreamingRecognizeRequest
from google.cloud.speech_v1.types.cloud_speech import StreamingRecognizeResponse
from google.cloud.speech_v1.types.cloud_speech import WordInfo

__all__ = (
    "LongRunningRecognizeMetadata",
    "LongRunningRecognizeRequest",
    "LongRunningRecognizeResponse",
    "RecognitionAudio",
    "RecognitionConfig",
    "RecognitionMetadata",
    "RecognizeRequest",
    "RecognizeResponse",
    "SpeakerDiarizationConfig",
    "SpeechAsyncClient",
    "SpeechClient",
    "SpeechContext",
    "SpeechRecognitionAlternative",
    "SpeechRecognitionResult",
    "StreamingRecognitionConfig",
    "StreamingRecognitionResult",
    "StreamingRecognizeRequest",
    "StreamingRecognizeResponse",
    "WordInfo",
)
