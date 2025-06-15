import aiohttp
import time
from utils.logger import log
from utils.topic_loader import load_config

async def scrape_events():
    start = time.time()
    config = load_config()
    event_urls = config.get("events_sources", [])
    events = []

    async with aiohttp.ClientSession() as session:
        for url in event_urls:
            try:
                async with session.get(url, timeout=20) as resp:
                    text = await resp.text()
                    events.append({
                        "title": "Event info",
                        "description": text[:500],  # just raw html for now
                        "link": url,
                        "source": "Events",
                        "publishedDate": "",
                    })
            except Exception as e:
                log.error(f"Events Error {url}: {e}")

    log.info(f"⏱ scrape_events executed in {round(time.time()-start, 2)} seconds")
    return events
