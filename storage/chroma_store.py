import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.Client()
collection = client.get_or_create_collection("green_steel")

def store_article(article):
    collection.add(
        documents=[article["description"]],
        metadatas=[article],
        ids=[article["link"]]
    )

def get_articles(limit=10, sort="latest", category=None):
    results = collection.peek(limit)
    return results
