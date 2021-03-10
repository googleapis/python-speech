# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# [START speech_transcribe_with_custom_classes]
from google.cloud import speech_v1p1beta1 as speech

def transcribe_with_custom_classes(project_id, location):

    # Create the adaptation client and create the custom class phrase set
    adaptation_client = speech.AdaptationClient()

    parent = f'projects/{project_id}/locations/{location}'

    custom_class_response = adaptation_client.create_custom_class({
        "parent": parent,
        "custom_class_id": "seattlerestaurants1",
        "custom_class": {   
            "items": [{'value': 'sushido'}, {'value': 'altura'}, {'value':'taneda'}]
        }
    })

    print(custom_class_response)

    # Use the custom class that you just created
    speech_client = speech.SpeechClient()

    request = speech.RecognitionConfig()

# [END speech_transcribe_with_custom_classes]