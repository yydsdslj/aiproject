# ai处理逻辑

import requests
import re
from bs4 import BeautifulSoup
from .utils import load_config

def extract_important_content(html_content):
    """
    提取 HTML 内容中的关键部分。
    :param html_content: 原始 HTML 内容
    :return: 提取后的文本内容
    """
    soup = BeautifulSoup(html_content, "html.parser")
    # 移除脚本和样式标签
    for script in soup(["script", "style"]):
        script.extract()
    # 提取纯文本内容
    text = soup.get_text(separator=" ")
    return text

def compress_html(text_content):
    """
    压缩提取后的文本内容，移除不必要的空格和换行符。
    :param text_content: 提取后的文本内容
    :return: 压缩后的文本内容
    """
    # 移除多余的空格和换行符
    compressed = re.sub(r'\s+', ' ', text_content)
    return compressed

def process_with_ai(html_content):
    """
    使用 AI 模型处理页面HTML内容。
    :param html_content: 页面的HTML内容
    :return: AI 处理后的数据
    """
    config = load_config('../config/config.yml')
    api_key = config['siliconflow']['api_key']
    api_url = config['siliconflow']['api_url']
    model = config['siliconflow']['model']

    # 提取关键内容
    text_content = extract_important_content(html_content)

    # 压缩提取后的文本内容
    compressed_content = compress_html(text_content)

    # 构建请求体
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"对以下文本内容进行总结和关键信息提取，将搜索结果整理为表格，包含标题、链接和补充内容: {compressed_content}"
            }
        ],
        "max_tokens": 1000  # 根据需要调整
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
