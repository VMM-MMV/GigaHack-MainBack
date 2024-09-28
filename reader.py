import json
import os
import yaml
from dotenv import load_dotenv 
load_dotenv()

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(f"Error reading YAML file: {exc}")

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return dict(json.load(json_file))
    
def get_sys_env(env_name):
    return os.getenv(env_name)

def access_yaml(yaml_data, path):
    keys = path.strip().split(".")
    current = yaml_data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list):
                current = current[int(key)]
            else:
                raise KeyError(f"Cannot access '{key}' in {type(current)}")
        return current
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error accessing path '{path}': {str(e)}")
        return None

def get_config(path):
    return access_yaml(read_yaml("config.yaml"), path)

if __name__ == "__main__":
    val = get_config("ngrok.root")
    print(val)