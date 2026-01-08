import os
import requests

def speech_to_text(audio_file_path: str) -> str:
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}

    with open(audio_file_path, "rb") as audio:
        files = {"file": audio}
        data = {"model": "gpt-4o-transcribe"}

        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json()["text"]
