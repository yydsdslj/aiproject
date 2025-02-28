import requests
from .utils import load_config

def get_chat_response(prompt):
    """
    调用 SiliconFlow API 获取聊天响应。
    :param prompt: 用户输入的问题
    :return: 模型生成的回答
    """
    # 加载配置文件
    config = load_config('../config/config.yml')
    api_key = config['siliconflow']['api_key']
    api_url = config['siliconflow']['api_url']
    model = config['siliconflow']['model']

    # 构建请求体
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"},
    }

    # 设置请求头
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 发送 POST 请求
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print(f"API 请求失败: {response.status_code}, {response.text}")
        return None
