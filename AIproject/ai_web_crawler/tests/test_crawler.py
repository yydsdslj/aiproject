# 爬虫逻辑的单元测试
import pytest
from ai_web_crawler.ai_web_crawler.crawler import run_playwright

@pytest.mark.asyncio
async def test_run_playwright():
    """
    测试 run_playwright 函数是否能正确加载网页并提取文本内容。
    """
    url = "https://www.baidu.com/"  # 测试网页
    search_query = "苹果"  # 测试搜索关键词

    # 调用 run_playwright 函数
    data = await run_playwright(url, search_query)

    # 验证返回的数据是否符合预期
    assert isinstance(data, dict)  # 确保返回的是字典
    assert "search_query" in data  # 确保包含搜索关键词
    assert "search_results" in data  # 确保包含搜索结果
    assert isinstance(data["search_results"], list)  # 确保搜索结果是列表
    if data["search_results"]:  # 如果有搜索结果
        assert isinstance(data["first_result_title"], str)  # 确保第一个结果的标题是字符串
        assert isinstance(data["first_result_url"], str)  # 确保第一个结果的链接是字符串

@pytest.mark.asyncio
async def test_run_playwright_timeout():
    """
    测试 run_playwright 函数在页面加载超时时的行为。
    """
    url = "https://www.invalid-url-that-will-timeout.com/"  # 无效 URL，会导致超时
    search_query = "苹果"

    # 调用 run_playwright 函数
    data = await run_playwright(url, search_query)

    # 验证返回的数据是否符合预期
    assert isinstance(data, dict)  # 确保返回的是字典
    assert "search_query" in data  # 确保包含搜索关键词
    assert "search_results" in data  # 确保包含搜索结果
    assert isinstance(data["search_results"], list)  # 确保搜索结果是列表
