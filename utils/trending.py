from collections import Counter
import re

def extract_keywords(text):
    text = re.sub(r"[^\w\s]", "", text)
    words = text.lower().split()
    stopwords = set(["the", "and", "of", "to", "in", "for", "is", "on", "with", "that", "as", "by", "an", "be", "are", "from"])
    return [word for word in words if word not in stopwords and len(word) > 3]

def get_trending(articles, top_n=10):
    all_keywords = []

    for article in articles:
        content = article.get("title", "") + " " + article.get("description", "")
        keywords = extract_keywords(content)
        all_keywords.extend(keywords)

    most_common = Counter(all_keywords).most_common(top_n)
    return [{"keyword": word, "count": count} for word, count in most_common]
