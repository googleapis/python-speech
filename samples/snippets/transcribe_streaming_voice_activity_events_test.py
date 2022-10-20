# Copyright 2022, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
from uuid import uuid4

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

import transcribe_streaming_voice_activity_events

RESOURCES = os.path.join(os.path.dirname(__file__), "resources")


def delete_recognizer(name):
    client = SpeechClient()
    request = cloud_speech.DeleteRecognizerRequest(name=name)
    client.delete_recognizer(request=request)


def test_transcribe_streaming_voice_activity_events(capsys):
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")

    recognizer_id = "recognizer-" + str(uuid4())
    responses = transcribe_streaming_voice_activity_events.transcribe_streaming_voice_activity_events(
        project_id, recognizer_id, os.path.join(RESOURCES, "audio.wav")
    )

    transcript = ""
    for response in responses:
        for result in response.results:
            transcript += result.alternatives[0].transcript

    assert (
        responses[0].speech_event_type
        == cloud_speech.StreamingRecognizeResponse.SpeechEventType.SPEECH_ACTIVITY_BEGIN
    )

    assert re.search(
        r"how old is the Brooklyn Bridge",
        transcript,
        re.DOTALL | re.I,
    )

    delete_recognizer(
        f"projects/{project_id}/locations/global/recognizers/{recognizer_id}"
    )
