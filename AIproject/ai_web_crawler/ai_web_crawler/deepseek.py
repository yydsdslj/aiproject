# deepseek交互逻辑

import requests
from .utils import load_config

def extract_with_deepseek(text, schema):
    """
    使用 DeepSeek-V3 模型提取结构化数据。
    :param text: 网页的纯文本内容
    :param schema: 目标数据的结构定义
    :return: 结构化数据
    """
    config = load_config('../config/config.yml')
    api_key = config['siliconflow']['api_key']
    api_url = config['siliconflow']['api_url']
    model = config['siliconflow']['model']

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"Extract structured data from the following text based on the schema: {schema}\n\nText: {text}"
            }
        ],
        "max_tokens": 200
    }
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"DeepSeek API请求失败: {e}")
        return None
