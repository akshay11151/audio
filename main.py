import io
import os

from google.cloud import speech_v1p1beta1 as speech


def transcribe_file_with_auto_language(file_path):
    """Transcribe the given audio file using Google Cloud Speech-to-Text API with auto language detection."""
    client = speech.SpeechClient()

    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding="LINEAR16",
        sample_rate_hertz=44100,
        language_code="",
        enable_automatic_punctuation=True,
        use_enhanced=True,
        model="default",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")


if __name__ == "__main__":
    # Set the path to your service account key JSON file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/Downs/audio-384617-617199920ed2.json"

    # Set the path to your audio file
    file_path = "D:/Downs/A_J_Cook_Speech_from_Lansbury's_Labour_Weekly.ogg"

    # Transcribe the audio file
    transcribe_file_with_auto_language(file_path)
