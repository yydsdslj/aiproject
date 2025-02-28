import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "THUDM/glm-4-9b-chat",
    "messages": [
        {
            "role": "user",
            "content": "中国大模型行业2025年将会迎来哪些机遇和挑战？"
        }
    ],
    "stream": False,
    "max_tokens": 512,
    "stop": None,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "frequency_penalty": 0.5,
    "n": 1,
    "response_format": {"type": "text"},
    "tools": [
        {
            "type": "function",
            "function": {
                "description": "<string>",
                "name": "<string>",
                "parameters": {},
                "strict": False
            }
        }
    ]
}
headers = {
    "Authorization": "Bearer sk-mmwudtdbtjsbgxsgfpimvkhllisttgsctwywomaqtmbqhrbw",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)