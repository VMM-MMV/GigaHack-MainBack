import json
import os
from dotenv import load_dotenv 
load_dotenv()

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
    
def get_sys_env(env_name):
    return os.getenv(env_name)