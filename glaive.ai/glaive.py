import requests


url = 'https://arena.glaive.ai/generate'

headers = {
    'authority': 'arena.glaive.ai',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.5',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}


def get_response(prompt, model="GPT-3.5", maxTokens=1024, temperature=0.1):
    allowed_models = ["WizardCoder-Python-34B-V1.0", "GPT-4", "GPT-3.5",
                      "Phind-CodeLlama-34B-v2", "codellama-13b-oasst-sft-v10",
                      "glaive-coder-7b"]

    if model not in allowed_models:
        return ValueError(f"Invalid model '{model}'. Please choose from: \
        {', '.join(allowed_models)}")

    data = {
        "model": model,
        "messages": [
            {
                "content": prompt,
                "id": "",
                "role": "user"
            }
        ],
        "title": "New chat",
        "id": None,
        "maxTokens": maxTokens,
        "temperature": temperature,
        "topP": 0.95,
        "topK": 30
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        return "server error"
    response_json = response.json()
    return response_json['messages'][1]['content']


if __name__ == "__main__":
    respanse = get_response("how are you", model="GPT-3.5")
    print(respanse)
