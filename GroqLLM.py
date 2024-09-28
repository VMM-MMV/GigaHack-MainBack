from groq import Groq
from reader import get_sys_env

class GroqLLM:
    def __init__(self):
        self.client = Groq(
            api_key=get_sys_env("GROQ_API_KEY")
        )

    def query(self, prompt):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )

        return chat_completion.choices[0].message.content

    @staticmethod
    def remove_whitespace(text):
        return " ".join(text.split())