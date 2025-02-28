# 主爬虫逻辑
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from .ai_processor import process_with_ai

async def run_playwright(url, search_query):
    """
    使用Playwright模拟用户行为，加载网页并提取HTML内容。
    :param url: 目标网页的URL
    :param search_query: 搜索关键词
    :return: 网页的纯文本内容
    """
    async with async_playwright() as p:
        # 启动浏览器（headless=False表示显示浏览器界面，适合调试）
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        try:
            # 导航到目标网页，等待页面加载完成
            await page.goto(url, wait_until='networkidle', timeout=30000)
        except asyncio.TimeoutError:
            print("页面加载超时，继续处理已加载的内容。")

        # 在搜索框中输入关键词并提交
        search_box = await page.query_selector('input#kw')
        await search_box.type(search_query)
        await page.keyboard.press('Enter')

        # 等待搜索结果加载
        await page.wait_for_selector('div.result', timeout=30000)

        # 获取页面HTML内容
        page_source = await page.content()
        await browser.close()

        # 使用BeautifulSoup解析HTML，提取搜索结果
        soup = BeautifulSoup(page_source, "html.parser")
        results = []
        for result in soup.select('div.result'):
            title = result.select_one('h3 a')
            if title:
                results.append({
                    "title": title.get_text(strip=True),
                    "url": title['href']
                })

        # 返回结构化数据
        return {
            "search_query": search_query,
            "search_results": [result["title"] for result in results],
            "first_result_title": results[0]["title"] if results else None,
            "first_result_url": results[0]["url"] if results else None,
        }

async def main():
    """
    主函数，模拟搜索并提取搜索结果。
    """
    url = "https://www.baidu.com/"  # 目标网页
    search_query = "苹果"  # 搜索关键词

    try:
        # 使用Playwright模拟搜索并提取数据
        data = await run_playwright(url, search_query)
        print("原始数据:", data)

        # 使用 AI 处理数据
        processed_data = process_with_ai(data)
        print("AI 处理后的数据:", processed_data)
    except Exception as e:
        print(f"处理 {url} 时出错:", e)

if __name__ == "__main__":
    asyncio.run(main())
