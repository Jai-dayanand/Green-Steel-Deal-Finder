# Green Steel Deal Finder

## Overview

The Green Steel Deal Finder is a full-fledged AI-powered data pipeline designed to collect, summarize, analyze, and serve news and insights related to the green steel industry. It leverages web scraping, LLM summarization, vector databases, and an API backend to provide structured and searchable information from multiple sources.

---

## Features

* Web scraping from multiple sources (news, podcasts, RSS, tenders, events).
* Summarization using OpenAI or local LLM models.
* Vector embeddings and semantic storage with Chroma DB.
* FastAPI backend to serve processed data.
* Configurable and modular architecture for easy customization.

---

## Project Structure

```
Green-Steel-Deal-Finder/
├── api/                # FastAPI backend
├── config/             # Configuration files
├── ingest/             # Web scrapers and data ingestion logic
├── llm/                # LLM summarization modules
├── output/             # Processed data output
├── storage/            # Vector storage (Chroma)
├── utils/              # Helper functions and utilities
├── run_pipeline.py     # Main pipeline entry point
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## Installation

1. Clone the repository:

```bash
git clone <repo_url>
cd Green-Steel-Deal-Finder
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables (API keys, etc.) in a `.env` file.

---

## Configuration

Edit the `config/config.json` file to:

* Select sources to scrape.
* Choose between OpenAI or local LLM summarizer.
* Define Chroma DB storage location.
* Set model keys and settings.

---

## Usage

### Run Full Pipeline:

```bash
python run_pipeline.py
```

This will:

* Scrape data from configured sources.
* Summarize articles.
* Store them in Chroma DB and JSON files.

### Run API Server:

```bash
uvicorn api.main:app --reload
```

Access the API at `http://127.0.0.1:8000`

---

## Supported Sources

* BusinessLine Steel
* Google News
* RSS Feeds
* Podcast directories
* Steel Industry News
* Government tenders
* Industry events

---

## Tech Stack

* Python 3
* FastAPI
* BeautifulSoup, Feedparser (scraping)
* OpenAI API / HuggingFace models (LLM summarization)
* Chroma (vector storage)
* dotenv (for environment management)

---

## Contribution

Pull requests, issues, and feature requests are welcome.

---


