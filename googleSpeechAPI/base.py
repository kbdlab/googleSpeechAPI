import io
import os

# Imports the Google Cloud client library
from google.cloud import speech

# Instantiates a client"
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(os.path.dirname("/home/kbdlab-server2/jang/googleSpeechAPI/"), "sample.raw")

# Loads the audio into memory
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    #encoding="FLAC",
    sample_rate_hertz=16000,
    language_code="ko-KR",
)

# Detects speech in the audio file

response = client.recognize(request={"config": config, "audio": audio})
print("debug",response)
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
