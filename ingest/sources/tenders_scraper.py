import aiohttp
import time
from utils.logger import log
from utils.topic_loader import load_config

async def scrape_tenders():
    start = time.time()
    config = load_config()
    tender_urls = config.get("tenders_sources", [])
    tenders = []

    async with aiohttp.ClientSession() as session:
        for url in tender_urls:
            try:
                async with session.get(url, timeout=20) as resp:
                    text = await resp.text()
                    tenders.append({
                        "title": "Tender info",
                        "description": text[:500],  # just raw html for now
                        "link": url,
                        "source": "Tenders",
                        "publishedDate": "",
                    })
            except Exception as e:
                log.error(f"Tenders Error {url}: {e}")

    log.info(f"⏱ scrape_tenders executed in {round(time.time()-start, 2)} seconds")
    return tenders
