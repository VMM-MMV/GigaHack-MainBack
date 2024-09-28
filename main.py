import os
from groq import Groq
from dotenv import load_dotenv 
load_dotenv() 

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def query(prompt):    
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
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

suport_script = read_file("suport_script.txt")

no_whitespace_suport_script = remove_whitespace(suport_script)

print(no_whitespace_suport_script)

pre_prompt = "You are a professional json writer. You will be given a technical support script and your job is too structure it into a json so its easier to understand. Separate romanian and russian."

response = query(pre_prompt + "This is the sript: " + no_whitespace_suport_script)

print(response)