import requests
from reader import get_sys_env

def make_request(end_point, body):
    ROOT = get_sys_env("NGROK_ROOT")

    # Send POST request
    response = requests.post(ROOT + end_point, json=body)

    # Check if the request was successful
    if response.status_code == 200:
        json_response = response.json()
        return json_response.get("response")
    else:
         raise Exception(f"Failed with status code {response.status_code}. Response: {response.text}")
