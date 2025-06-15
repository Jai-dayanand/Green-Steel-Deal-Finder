from fastapi import FastAPI, Query
from storage.chroma_store import get_articles
from utils.logger import log

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Green Steel Deal Finder API Working"}

@app.get("/articles")
def read_articles(limit: int = 10, sort: str = "latest", category: str = None):
    articles = get_articles(limit=limit, sort=sort, category=category)
    return {"articles": articles}
