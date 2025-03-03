# 爬虫逻辑的单元测试
import pytest
from ai_web_crawler.ai_web_crawler.crawler import run_playwright

@pytest.mark.asyncio
async def test_run_playwright():
    """
    测试 run_playwright 函数是否能正确加载网页并提取多条搜索结果。
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
    assert len(data["search_results"]) > 1  # 确保爬取了多条结果
