# 爬虫逻辑的单元测试
import pytest
from ai_web_crawler.ai_web_crawler.crawler import run_playwright
from ai_web_crawler.ai_web_crawler.deepseek import extract_with_deepseek
from ai_web_crawler.ai_web_crawler.models import StockData, YouTubeData, TwitterData
from ai_web_crawler.ai_web_crawler.schemas import TARGET_SCHEMAS


@pytest.mark.asyncio
async def test_run_playwright():
    """
    测试 run_playwright 函数是否能正确加载网页并提取文本内容。
    """
    url = "https://example.com"  # 使用一个简单的测试网页
    text = await run_playwright(url)
    assert isinstance(text, str)  # 确保返回的是字符串
    assert len(text) > 0  # 确保文本内容不为空


@pytest.mark.asyncio
async def test_extract_with_deepseek():
    """
    测试 extract_with_deepseek 函数是否能正确提取结构化数据。
    """
    # 测试数据
    text = """
    Market Cap: 1.5T
    Open: 2800
    EPS: 112.34
    Financial Performance: Strong growth in Q1 2023
    """
    schema = TARGET_SCHEMAS[0]["schema"]  # 使用股票网站的数据结构
    structured_data = extract_with_deepseek(text, schema)

    # 验证返回的数据是否符合预期
    assert isinstance(structured_data, dict)
    assert "market_cap" in structured_data
    assert "open" in structured_data
    assert "eps" in structured_data
    assert "financial_performance" in structured_data


@pytest.mark.asyncio
async def test_main_logic():
    """
    测试主逻辑（爬取网页并提取数据）是否正常工作。
    """
    target = TARGET_SCHEMAS[0]  # 使用股票网站作为测试目标
    url = target["url"]
    schema = target["schema"]

    # 爬取网页内容
    text = await run_playwright(url)
    assert isinstance(text, str)
    assert len(text) > 0

    # 提取结构化数据
    structured_data = extract_with_deepseek(text, schema)
    assert isinstance(structured_data, dict)
    assert "market_cap" in structured_data
    assert "open" in structured_data
    assert "eps" in structured_data
    assert "financial_performance" in structured_data


def test_models():
    """
    测试数据模型是否正确。
    """
    # 测试 StockData 模型
    stock_data = StockData(
        market_cap="1.5T",
        open="2800",
        eps="112.34",
        financial_performance="Strong growth in Q1 2023"
    )
    assert isinstance(stock_data, StockData)

    # 测试 YouTubeData 模型
    youtube_data = YouTubeData(
        title="Introduction to AI",
        views="100K",
        date="2023-10-01"
    )
    assert isinstance(youtube_data, YouTubeData)

    # 测试 TwitterData 模型
    twitter_data = TwitterData(
        post_author="Elon Musk",
        post_content="Just setting up my twttr."
    )
    assert isinstance(twitter_data, TwitterData)
