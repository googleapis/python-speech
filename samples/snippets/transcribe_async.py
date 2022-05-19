#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample that demonstrates transcribing an audio file
   using asyncio.

Example usage:
    python transcribe_async.py audio.wav
"""


import argparse
import asyncio

from google.cloud import speech


async def audio_stream(config, file: str):
    yield speech.StreamingRecognizeRequest(streaming_config=config)
    with open(file, "rb") as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            yield speech.StreamingRecognizeRequest(audio_content=chunk)


async def print_responses(responses):
    async for response in responses:
        for i, result in enumerate(response.results):
            print(i, result.alternatives[0].transcript)


async def main(file: str):
    client = speech.SpeechAsyncClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True
    )

    stream = audio_stream(streaming_config, file)
    responses = await client.streaming_recognize(stream)

    task = asyncio.create_task(print_responses(responses))

    await task


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("file", help="File to stream to the API")
    args = parser.parse_args()
    asyncio.get_event_loop().run_until_complete(main(args.file))
