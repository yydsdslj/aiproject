import requests
from .utils import load_config

def process_with_ai(data):
    """
    使用 AI 模型处理搜索结果。
    :param data: 搜索结果数据
    :return: 处理后的数据
    """
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
                "content": f"对以下搜索结果进行摘要生成和关键信息提取: {data}"
            }
        ],
        "max_tokens": 200
    }

    # 设置请求头
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 发送 POST 请求
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"AI 处理失败: {e}")
        return None
