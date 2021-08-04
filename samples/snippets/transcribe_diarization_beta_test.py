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

import os

from transcribe_diarization_beta import transcribe_file_with_diarization

def test_transcribe_diarization(capsys):

    test_file_path = os.path.join(os.path.dirname(__file__),
        "resources/commercial_mono.wav")

    transcribe_file_with_diarization(test_file_path)
    out, err = capsys.readouterr()

    assert "word:" in out
    assert "speaker_tag:" in out