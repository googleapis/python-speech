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

from .resource import (
    CustomClass,
    PhraseSet,
    SpeechAdaptation,
)
from .cloud_speech import (
    RecognizeRequest,
    LongRunningRecognizeRequest,
    StreamingRecognizeRequest,
    StreamingRecognitionConfig,
    RecognitionConfig,
    SpeakerDiarizationConfig,
    RecognitionMetadata,
    SpeechContext,
    RecognitionAudio,
    RecognizeResponse,
    LongRunningRecognizeResponse,
    LongRunningRecognizeMetadata,
    StreamingRecognizeResponse,
    StreamingRecognitionResult,
    SpeechRecognitionResult,
    SpeechRecognitionAlternative,
    WordInfo,
)

__all__ = (
    "CustomClass",
    "PhraseSet",
    "SpeechAdaptation",
    "RecognizeRequest",
    "LongRunningRecognizeRequest",
    "StreamingRecognizeRequest",
    "StreamingRecognitionConfig",
    "RecognitionConfig",
    "SpeakerDiarizationConfig",
    "RecognitionMetadata",
    "SpeechContext",
    "RecognitionAudio",
    "RecognizeResponse",
    "LongRunningRecognizeResponse",
    "LongRunningRecognizeMetadata",
    "StreamingRecognizeResponse",
    "StreamingRecognitionResult",
    "SpeechRecognitionResult",
    "SpeechRecognitionAlternative",
    "WordInfo",
)
