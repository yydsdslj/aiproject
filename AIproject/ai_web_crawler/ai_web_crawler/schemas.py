# 定义目标网站的数据结构
# 目标网站的数据结构，用于验证网站的数据结构是否符合预期
# 如果网站的数据结构发生变化，需要更新该数据结构
TARGET_SCHEMAS = [
    {
        "url": "https://www.baidu.com/",
        "schema": {
            "properties": {
                "search_query": {"type": "string"},  # 搜索关键词
                "search_results": {"type": "array", "items": {"type": "string"}},  # 搜索结果列表
                "first_result_title": {"type": "string"},  # 第一个搜索结果的标题
                "first_result_url": {"type": "string"},  # 第一个搜索结果的链接
            },
        },
    }
]
