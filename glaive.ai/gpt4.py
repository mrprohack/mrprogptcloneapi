import requests
import json

url = 'https://arena.glaive.ai/generate'

headers = {
    'authority': 'arena.glaive.ai',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.5',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

data = {
    "model": "GPT-4",
    "messages": [
        {
            "content": "how are you",
            "id": "",
            "role": "user"
        }
    ],
    "title": "New chat",
    "id": None,
    "maxTokens": 1024,
    "temperature": 0.1,
    "topP": 0.95,
    "topK": 30
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    response_json = response.json()
    assistant_message = response_json['messages'][1]['content']
    print("Assistant's Response:", assistant_message)
else:
    print(f"Request failed with status code {response.status_code}")

