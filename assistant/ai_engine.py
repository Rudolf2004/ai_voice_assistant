import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AIEngine:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are a voice-based AI communication assistant. "
                    "You speak naturally, think deeply, and hold conversations like a human."
                )
            }
        ]

    def respond(self, user_text: str) -> str:
        self.messages.append({"role": "user", "content": user_text})

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=self.messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply
