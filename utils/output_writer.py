import os
import json

def save_articles_to_json(articles, filename="output/articles.json"):
    os.makedirs("output", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)
