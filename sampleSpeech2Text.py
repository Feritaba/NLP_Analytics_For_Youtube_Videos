from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io

from pathlib import Path


def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition
    """

    client = speech_v1.SpeechClient()

    # The language of the supplied audio
    language_code = "en-US"

    # Encoding of audio data sent. This sample sets this explicitly.
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    config = {
        "language_code": language_code,
        "encoding": encoding,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    text = ''
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        text += alternative.transcript
    return text

# [END speech_transcribe_sync]


sample_recognize('/home/Foroozan/Desktop/SpeechToText/SampleRecord1.flac')

results = list()
for entry in Path('/home/Foroozan/Desktop/SpeechToText').iterdir():
    if str(entry).endswith('.flac'):
        results.append(sample_recognize(str(entry)))

with open("/home/Foroozan/Desktop/SpeechToText/audioTranscript.txt", "w") as file:
    for res in results:
        file.write(res)
        file.write('\n')