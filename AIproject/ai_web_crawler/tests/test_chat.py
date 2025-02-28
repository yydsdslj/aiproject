import pytest
from ai_web_crawler.ai_web_crawler.chat import get_chat_response

def test_get_chat_response():
    """
    测试 get_chat_response 函数是否能正确获取模型回答。
    """
    prompt = "中国大模型行业2025年将会迎来哪些机遇和挑战？"
    response = get_chat_response(prompt)
    assert isinstance(response, str)
    assert len(response) > 0
