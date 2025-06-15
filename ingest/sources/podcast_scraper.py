import aiohttp
import time
from utils.logger import log
from utils.topic_loader import load_config

async def scrape_podcasts():
    start = time.time()
    config = load_config()
    podcast_urls = config.get("podcasts_sources", [])
    podcasts = []

    async with aiohttp.ClientSession() as session:
        for url in podcast_urls:
            try:
                async with session.get(url, timeout=20) as resp:
                    text = await resp.text()
                    podcasts.append({
                        "title": "Podcast info",
                        "description": text[:500],  # raw RSS for now
                        "link": url,
                        "source": "Podcasts",
                        "publishedDate": "",
                    })
            except Exception as e:
                log.error(f"Podcasts Error {url}: {e}")

    log.info(f"⏱ scrape_podcasts executed in {round(time.time()-start, 2)} seconds")
    return podcasts
