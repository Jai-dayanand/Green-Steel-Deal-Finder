import aiohttp
import feedparser
import time
from utils.logger import log
from utils.topic_loader import load_config

async def scrape_rss_feeds():
    start = time.time()
    config = load_config()
    rss_urls = config.get("rss_feeds", [])
    articles = []

    async with aiohttp.ClientSession() as session:
        for url in rss_urls:
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
                            "source": "RSS"
                        })
            except Exception as e:
                log.error(f"RSS Error {url}: {e}")

    log.info(f"⏱ scrape_rss_feeds executed in {round(time.time()-start, 2)} seconds")
    return articles
