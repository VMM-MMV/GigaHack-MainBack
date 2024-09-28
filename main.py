import os
from groq import Groq
from dotenv import load_dotenv 
import json
load_dotenv() 

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

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

suport_script = read_file("support_ro.json")

pre_prompt = """
You are senior customer support professional. You will be given a question from a Moldovian user, 
who will ask the question using 'Moldovian'(Romanian with moldovan dialect, with some latinized russian), 
which will also have poor grammar. Sometimes even writen in cirilic instead of latin.
Your job is to classify that question based on the given response template. You in such a manner {"Class": <found_class>}
"""

# prompt = "Wa brat cum pula me bl aisi di gasit resetu la paroli"
# prompt = "ауз уай ди унди еу стеле"
prompt = "Cum bl si poati de prinit nisti stele"
response = query(pre_prompt + "Response template: " + suport_script + "\nThe question: " + prompt)

print(response)