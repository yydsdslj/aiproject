from pydantic import BaseModel

class StockData(BaseModel):
    market_cap: str
    open: str
    eps: str
    financial_performance: str

class YouTubeData(BaseModel):
    title: str
    views: str
    date: str

class TwitterData(BaseModel):
    post_author: str
    post_content: str
