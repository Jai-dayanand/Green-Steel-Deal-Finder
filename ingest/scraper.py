from utils.logger import log
import asyncio
from utils.logger import log
from ingest.sources.rss_feeds import scrape_rss_feeds
from ingest.sources.google_news import scrape_google_news
from ingest.sources.tenders_scraper import scrape_tenders
from ingest.sources.events_scraper import scrape_events
from ingest.sources.podcast_scraper import scrape_podcasts
from utils.output_writer import save_articles_to_json

from utils.output_writer import save_articles_to_json

async def gather_articles():
    log.info("🚀 Starting full scraping pipeline...")
    
    tasks = [
        scrape_rss_feeds(),
        scrape_google_news(),
        scrape_tenders(),
        scrape_events(),
        scrape_podcasts()
    ]

    all_results = await asyncio.gather(*tasks)
    all_articles = [article for source_result in all_results for article in source_result]

    # Save to file here 🔥
    save_articles_to_json(all_articles)

    log.info(f"✅ Total articles scraped: {len(all_articles)}")
    return all_articles
