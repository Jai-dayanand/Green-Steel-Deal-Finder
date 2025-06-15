import aiohttp
from bs4 import BeautifulSoup
from utils.helpers import clean_text, get_topics
from utils.logger import log, log_execution_time

BASE_URL = "https://steelindustry.news/"

@log_execution_time
async def scrape_steelindustry_news():
    articles = []
    topics = get_topics()

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, timeout=30) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, "lxml")
            for tag in soup.select("article"):
                try:
                    title_tag = tag.select_one("h2 a")
                    if not title_tag:
                        continue
                    title = clean_text(title_tag.text)
                    if not any(topic.lower() in title.lower() for topic in topics):
                        continue  # filter by topics dynamically

                    url = title_tag["href"]
                    date = tag.select_one("time")['datetime'] if tag.select_one("time") else None
                    summary = clean_text(tag.select_one("div.entry-summary").text if tag.select_one("div.entry-summary") else "")
                    
                    async with session.get(url, timeout=30) as article_resp:
                        art_soup = BeautifulSoup(await article_resp.text(), "html.parser")
                        paragraphs = art_soup.find_all("p")
                        content = clean_text(" ".join(p.text for p in paragraphs))

                    articles.append({
                        "title": title,
                        "url": url,
                        "date": date,
                        "summary": summary,
                        "content": content,
                        "source": BASE_URL
                    })
                except Exception as e:
                    log.error(f"[steelindustry] Error: {e}")
    return articles
