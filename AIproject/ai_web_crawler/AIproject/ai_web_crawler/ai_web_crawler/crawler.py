# 主爬虫逻辑
import asyncio
from playwright.async_api import async_playwright
from .ai_processor import process_with_ai

async def run_playwright(url, search_query, pages=3):
    """
    使用Playwright模拟用户行为，加载网页并提取HTML内容。
    :param url: 目标网页的URL
    :param search_query: 搜索关键词
    :param pages: 需要爬取的页数
    :return: 包含每页HTML内容的列表
    """
    async with async_playwright() as p:
        # 启动浏览器（headless=False表示显示浏览器界面，适合调试）
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        all_html_contents = []

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

        # 爬取指定页数的数据
        for i in range(pages):
            print(f"正在爬取第 {i + 1} 页数据...")
            # 获取当前页面的HTML内容
            page_source = await page.content()
            all_html_contents.append(page_source)

            # 移除遮罩层
            await page.evaluate('document.getElementById("_mask")?.remove()')

            # 点击“下一页”按钮
            next_button = await page.query_selector('a.n')
            if next_button:
                await next_button.click()
                # 等待下一页内容加载
                await page.wait_for_selector('div.result', timeout=30000)
            else:
                print("没有更多页面了。")
                break

        await browser.close()

        # 返回包含每页HTML内容的列表
        return all_html_contents

async def main():
    """
    主函数，模拟搜索并提取页面源代码，交给AI处理。
    """
    url = "https://www.baidu.com/"  # 目标网页
    search_query = "香蕉"  # 搜索关键词
    pages = 3  # 爬取的页数

    try:
        # 使用Playwright模拟搜索并提取页面HTML内容
        html_contents = await run_playwright(url, search_query, pages)
        print(f"共爬取 {pages} 页的HTML内容。")

        # 对每页内容分别进行AI处理
        for i, html_content in enumerate(html_contents):
            print(f"\n正在处理第 {i + 1} 页内容...")
            processed_data = process_with_ai(html_content)
            print(f"第 {i + 1} 页的AI处理结果:", processed_data)
    except Exception as e:
        print(f"处理 {url} 时出错:", e)

if __name__ == "__main__":
    asyncio.run(main())
