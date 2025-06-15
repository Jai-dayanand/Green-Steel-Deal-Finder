Green Steel Deal Finder
✅ Scrapes online articles, events, podcasts, and tenders related to green steel.
✅ Uses OpenAI (or local models) to summarize the content.
✅ Stores articles + summaries into a vector database (Chroma) for smart search.
✅ Exposes a FastAPI backend to query and serve the processed data.

Main Flow:
run_pipeline.py — entry point:
  Reads config.
  Runs all scrapers (Google News, RSS, podcasts, etc).
  Summarizes using LLM.
  Saves data to JSON & vector DB.
  api/main.py — serves the data via API.

Key Tech:
  Web scraping
  OpenAI LLM / local model
  Chroma vector DB
  FastAPI server
