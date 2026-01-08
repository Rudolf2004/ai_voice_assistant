import os
import requests

def text_to_speech(text: str, output_file="response.mp3"):
    url = "https://api.openai.com/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini-tts",
        "voice": "alloy",
        "input": text
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    with open(output_file, "wb") as f:
        f.write(response.content)
