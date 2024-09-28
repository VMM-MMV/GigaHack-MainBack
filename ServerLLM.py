import requests
from reader import get_config

class ServerLLM:
    def query(self, query, end_point="/classify"):
        ROOT = get_config("ngrok.root")

        data = {"query": query}

        # Send POST request
        response = requests.post(ROOT + end_point, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            json_response = response.json()
            return json_response.get("response")
        else:
            raise Exception(f"Failed with status code {response.status_code}. Response: {response.text}")
