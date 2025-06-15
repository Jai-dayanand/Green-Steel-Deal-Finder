import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils.logger import log, log_execution_time
from utils.helpers import clean_text, get_topics

BASE_URL = "https://www.thehindubusinessline.com/companies/"

@log_execution_time
async def scrape_businessline():
    results = []
    topics = get_topics()

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, timeout=30) as resp:
            soup = BeautifulSoup(await resp.text(), "html.parser")
            for tag in soup.find_all("a", href=True):
                try:
                    text = clean_text(tag.get_text()).lower()
                    if any(topic.lower() in text for topic in topics):
                        full_url = urljoin(BASE_URL, tag["href"])
                        async with session.get(full_url, timeout=30) as article_resp:
                            art_soup = BeautifulSoup(await article_resp.text(), "html.parser")
                            title = art_soup.find("h1").text.strip() if art_soup.find("h1") else "No Title"
                            paragraphs = art_soup.find_all("p")
                            content = clean_text(" ".join(p.text for p in paragraphs))
                            results.append({
                                "title": title,
                                "url": full_url,
                                "date": "",
                                "summary": "",
                                "content": content,
                                "source": BASE_URL
                            })
                except Exception as e:
                    log.error(f"[businessline] Error: {e}")
    return results
