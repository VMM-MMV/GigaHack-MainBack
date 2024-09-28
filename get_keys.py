import json
from reader import read_json

def get_json_keys(data, depth=1, current_depth=1):
    # If we have reached the desired depth, stop
    if current_depth > depth:
        return
    
    # If the current data is a dictionary, iterate over its keys
    if isinstance(data, dict):
        for key in data.keys():
            yield key
            # Recursively go deeper into nested dictionaries
            yield from get_json_keys(data[key], depth, current_depth + 1)
    
    # If the current data is a list, iterate over its elements
    elif isinstance(data, list):
        for item in data:
            yield from get_json_keys(item, depth, current_depth)

def get_keys_from_file(file_path, depth=1):
    try:
        return list(get_json_keys(read_json(file_path), depth))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return []

if __name__ == "__main__":
    response = get_keys_from_file('support_ro.json', depth=2)
    response.remove("script_support")

    print(response)
