import aiohttp
import feedparser
import time
from utils.logger import log
from utils.topic_loader import load_config

async def scrape_google_news():
    start = time.time()
    config = load_config()
    queries = config.get("google_news_queries", [])
    articles = []

    async with aiohttp.ClientSession() as session:
        for query in queries:
            url = f"https://news.google.com/rss/search?q={query.replace(' ', '%20')}&hl=en-IN&gl=IN&ceid=IN:en"
            try:
                async with session.get(url, timeout=20) as resp:
                    text = await resp.text()
                    feed = feedparser.parse(text)
                    for entry in feed.entries:
                        articles.append({
                            "title": entry.title,
                            "description": entry.get("summary", ""),
                            "link": entry.link,
                            "publishedDate": entry.get("published", ""),
                            "source": "Google News"
                        })
            except Exception as e:
                log.error(f"Google News Error {url}: {e}")

    log.info(f"⏱ scrape_google_news executed in {round(time.time()-start, 2)} seconds")
    return articles
