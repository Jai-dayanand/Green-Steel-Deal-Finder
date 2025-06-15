import re
import random
from llm.summarize_local import summarize

def clean_text(text):
    return re.sub(r'\s+', ' ', text)

def generate_bulletines(summary):
    sentences = summary.split('. ')
    return sentences[:3]

def predict_category(article):
    return random.choice(["Technology", "Steel", "Business", "Energy"])

def enrich_article(article):
    article["description"] = clean_text(article.get("description", ""))
    article["summary"] = summarize(article["description"])
    article["bulletines"] = generate_bulletines(article["summary"])
    article["category"] = predict_category(article)
    article["thumbnail"] = ""
    return article
