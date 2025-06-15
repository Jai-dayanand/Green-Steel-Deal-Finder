import asyncio
from ingest.scraper import gather_articles
from storage.chroma_store import store_article
from utils.logger import log

async def run():
    articles = await gather_articles()
    for article in articles:
        store_article(article)
        log.info(f"✅ Processed: {article['title']}")

if __name__ == "__main__":
    asyncio.run(run())
