from groq import Groq
from reader import get_env

def query(prompt):
    client = Groq(
        api_key=get_env("GROQ_API_KEY")
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

def remove_whitespace(text):
    return " ".join(text.split())