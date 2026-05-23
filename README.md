# Prothom Alo News Project

A Python based Prothom Alo news scraping and API project. The project has two connected parts. The first part scrapes news information from Prothom Alo pages and stores the extracted title and link data in a MySQL database. The second part provides a FastAPI service that reads the stored news data from MySQL and exposes it through API endpoints.

## Repository Link

```text
https://github.com/mirazchowdhury/prothom-alo-news-project
```

## Project Summary

This project is designed to collect news link information from Prothom Alo and make the collected data available through a simple REST API. The scraping module uses `requests_html` to visit a Prothom Alo page, extract page title and anchor links, and insert the extracted data into a MySQL table. The API module uses FastAPI, SQLAlchemy, Pydantic schemas, and MySQL connection settings from environment variables.

The repository currently contains two main folders:

```text
news_api
scraping
```

The `scraping` folder handles data collection and database insertion. The `news_api` folder handles API based data access.

## Main Features

1. Scrapes Prothom Alo news page information.
2. Extracts page title and article links.
3. Stores scraped data in MySQL.
4. Uses environment variables for database connection.
5. Provides a FastAPI backend for news data access.
6. Uses SQLAlchemy model for the `scraped_data` table.
7. Uses Pydantic schema for API response format.
8. Supports fetching stored news articles with pagination.
9. Supports creating news records through API.
10. Provides an API root route with a welcome message.
11. Separates scraping logic from API serving logic.
12. Can be expanded into a larger Bangla news collection platform.

## Repository Structure

```text
prothom-alo-news-project/
    news_api/
        requirements.txt

        app/
            __init__.py
            crud.py
            database.py
            main.py
            models.py
            schemas.py

            routers/
                news.py

    scraping/
        __init__.py

        web_scraping/
            db_connection.py
            db_operation.py
            extract_information.py
            test.ipynb

            .ipynb_checkpoints/
```

## Folder Details

## news_api

This folder contains the FastAPI service.

Main responsibilities:

1. Connect to MySQL database.
2. Map the `scraped_data` table with SQLAlchemy.
3. Define request and response schemas.
4. Provide database query functions.
5. Expose API routes through FastAPI.

## scraping

This folder contains the scraping workflow.

Main responsibilities:

1. Connect to MySQL using `mysql.connector`.
2. Fetch Prothom Alo pages using `requests_html`.
3. Extract title and link data.
4. Insert extracted data into the MySQL table.

## Main Files

## news_api/app/main.py

This is the FastAPI entry point.

Current behavior:

1. Creates a FastAPI app.
2. Includes the news router.
3. Defines a root route.
4. Returns a welcome message.

Root response:

```json
{
    "message": "Welcome to the News API"
}
```

## news_api/app/database.py

This file configures SQLAlchemy database connection.

It loads these environment variables:

```text
MYSQL_HOST
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DATABASE
MYSQL_PORT
```

Then it builds this database URL pattern:

```text
mysql+mysqlconnector://user:password@host:port/database
```

It also creates:

```text
engine
SessionLocal
Base
get_db
```

## news_api/app/models.py

This file defines the SQLAlchemy model.

Table name:

```text
scraped_data
```

Columns:

```text
id
title
link_text
link_href
```

## news_api/app/schemas.py

This file defines Pydantic schemas.

Main schemas:

```text
NewsArticleBase
NewsArticleCreate
NewsArticleResponse
```

The response schema includes:

```text
id
title
link_text
link_href
```

## news_api/app/crud.py

This file contains database helper functions.

Available functions:

1. `create_news_article`
2. `get_news_articles`
3. `get_news_article_by_id`
4. `update_news_article`
5. `delete_news_article`

The active router currently uses create and list functions.

## news_api/app/routers/news.py

This file defines the news API routes.

Active routes:

```text
GET /news/
POST /news/
```

## scraping/web_scraping/db_connection.py

This file creates a MySQL database connection using `mysql.connector`.

It loads these environment variables:

```text
DB_HOST
DB_USER
DB_PASS
DB_NAME
```

## scraping/web_scraping/extract_information.py

This file performs the web scraping task.

Main workflow:

1. Create an HTML session.
2. Connect to MySQL.
3. Visit the Prothom Alo page URL.
4. Search for a page title element.
5. Extract all anchor links.
6. Insert title and link data into the database.
7. Close the session and database connection.

Default target page in the current script:

```text
https://www.prothomalo.com/bangladesh/crime
```

## scraping/web_scraping/db_operation.py

This file currently imports `single_news_scraper` from `news_scraper_3`.

The referenced module is not visible in the repository, so this file may not run until that missing module is added or the import is updated.

## Technology Stack

## Backend API

1. Python.
2. FastAPI.
3. Uvicorn.
4. SQLAlchemy.
5. Pydantic.
6. MySQL connector.
7. python dotenv.

## Scraping

1. requests html.
2. MySQL connector.
3. python dotenv.

## Database

1. MySQL.

## API Endpoints

## Root Endpoint

```text
GET /
```

Purpose:

Checks whether the API is running.

Response:

```json
{
    "message": "Welcome to the News API"
}
```

## List News Articles

```text
GET /news/
```

Query parameters:

```text
skip
limit
```

Example request:

```text
http://127.0.0.1:8000/news/?skip=0&limit=10
```

Example response:

```json
{
    "data": [
        {
            "id": 1,
            "title": "Example page title",
            "link_text": "Example news link text",
            "link_href": "https://www.prothomalo.com/example"
        }
    ]
}
```

## Create News Article

```text
POST /news/
```

Request body:

```json
{
    "title": "Example title",
    "link_text": "Example link text",
    "link_href": "https://www.prothomalo.com/example"
}
```

Response body:

```json
{
    "id": 1,
    "title": "Example title",
    "link_text": "Example link text",
    "link_href": "https://www.prothomalo.com/example"
}
```

## Database Table

Create the table before running scraping or API code.

```sql
CREATE TABLE scraped_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    link_text VARCHAR(255),
    link_href TEXT
);
```

## Environment Variables

The repository uses two different naming styles for database variables. The scraping module uses `DB_` names, and the API module uses `MYSQL_` names.

Create a `.env` file in the relevant working folder or project root.

```env
DB_HOST=localhost
DB_USER=root
DB_PASS=your_mysql_password
DB_NAME=prothom_alo_news

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=prothom_alo_news
MYSQL_PORT=3306
```

Recommended improvement:

Use one shared naming style for both scraping and API modules in future development.

## Installation

Clone the repository.

```bash
git clone https://github.com/mirazchowdhury/prothom-alo-news-project.git
cd prothom-alo-news-project
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment on Windows.

```bash
.venv\Scripts\activate
```

Activate the virtual environment on Linux or macOS.

```bash
source .venv/bin/activate
```

Upgrade pip.

```bash
python -m pip install --upgrade pip
```

Install API dependencies.

```bash
pip install -r news_api/requirements.txt
```

If the dependency file appears on one line and installation fails, use this clean format in `news_api/requirements.txt`.

```text
fastapi
uvicorn
mysql-connector-python
requests-html
python-dotenv
sqlalchemy
pydantic
```

Important note:

The code uses SQLAlchemy, but `sqlalchemy` is not listed in the current dependency file. Install it manually if import errors occur.

```bash
pip install sqlalchemy
```

## MySQL Setup

Open MySQL and create a database.

```sql
CREATE DATABASE prothom_alo_news;
```

Use the database.

```sql
USE prothom_alo_news;
```

Create the table.

```sql
CREATE TABLE scraped_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    link_text VARCHAR(255),
    link_href TEXT
);
```

Add the database credentials to `.env`.

## How to Run the Scraper

Go to the scraper folder.

```bash
cd scraping/web_scraping
```

Run the scraper.

```bash
python extract_information.py
```

The script will scrape the configured Prothom Alo page and insert title and link data into the `scraped_data` table.

## How to Run the API

From the repository root, run:

```bash
cd news_api
uvicorn app.main:app --reload
```

Open the API in your browser.

```text
http://127.0.0.1:8000
```

Open interactive API documentation.

```text
http://127.0.0.1:8000/docs
```

Open alternative documentation.

```text
http://127.0.0.1:8000/redoc
```

## Full Usage Flow

1. Create MySQL database.
2. Create the `scraped_data` table.
3. Create a `.env` file with both scraping and API database variables.
4. Install Python dependencies.
5. Run the scraper from `scraping/web_scraping`.
6. Confirm data has been inserted into MySQL.
7. Run FastAPI from `news_api`.
8. Open `/news/` endpoint to view stored news records.

## Example API Test With curl

Get news articles:

```bash
curl "http://127.0.0.1:8000/news/?skip=0&limit=10"
```

Create a news article:

```bash
curl -X POST "http://127.0.0.1:8000/news/" \
     -H "Content-Type: application/json" \
     -d "{\"title\":\"Test Title\",\"link_text\":\"Test Link\",\"link_href\":\"https://www.prothomalo.com/test\"}"
```

## Example API Test With Python

```python
import requests

base_url = "http://127.0.0.1:8000"

response = requests.get(f"{base_url}/news/", params={"skip": 0, "limit": 10})
print(response.json())

payload = {
    "title": "Test Title",
    "link_text": "Test Link",
    "link_href": "https://www.prothomalo.com/test"
}

response = requests.post(f"{base_url}/news/", json=payload)
print(response.json())
```

## Current Code State Notes

1. Several Python files appear compressed into one line in the repository viewer.
2. Python source files should be reformatted with proper line breaks and indentation before running.
3. `crud.py` and `routers/news.py` currently show broken relative imports in raw view.
4. `database.py` uses SQLAlchemy, but `sqlalchemy` is missing from the current requirements file.
5. The scraper and API use different database environment variable names.
6. `db_operation.py` imports `news_scraper_3`, but that file is not visible in the repository.
7. The scraper currently targets one Prothom Alo URL.
8. The repository does not contain a root level README.
9. No license file was visible.
10. The repository contains Jupyter checkpoint files, which should not be committed.

## Suggested Clean main.py

```python
from fastapi import FastAPI

from .routers import news


app = FastAPI(title="Prothom Alo News API")

app.include_router(news.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the News API"}
```

## Suggested Clean database.py

```python
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

DATABASE_URL = (
    f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## Suggested Clean news.py Router

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, database, schemas


router = APIRouter(
    prefix="/news",
    tags=["news"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_news(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(database.get_db)
):
    news_articles = crud.get_news_articles(db, skip=skip, limit=limit)
    return {"data": news_articles}


@router.post("/", response_model=schemas.NewsArticleResponse)
def create_news(
    news_article: schemas.NewsArticleCreate,
    db: Session = Depends(database.get_db)
):
    return crud.create_news_article(
        db=db,
        news_article=news_article
    )
```

## Recommended Improvements

1. Reformat all Python files into standard Python style.
2. Add a root level `README.md`.
3. Add `.env.example`.
4. Add `.gitignore`.
5. Remove `.ipynb_checkpoints`.
6. Add `sqlalchemy` to requirements.
7. Use one shared database environment variable naming style.
8. Add an automatic table creation command or migration script.
9. Add article category, publish date, author, and full body scraping.
10. Add duplicate URL checking before database insertion.
11. Add pagination metadata in API responses.
12. Add update, get by id, and delete routes if CRUD functions are kept.
13. Add error handling for failed database connection.
14. Add logging for scraper runs.
15. Add Docker Compose for FastAPI and MySQL.
16. Add unit tests for CRUD functions.
17. Add a license file.
18. Add website scraping ethics and rate limit notes.

## Suggested .gitignore

```text
.venv/
__pycache__/
*.pyc
.env
.ipynb_checkpoints/
.idea/
*.log
```

## Suggested Future Structure

```text
prothom-alo-news-project/
    news_api/
        app/
            core/
                config.py
            database/
                connection.py
            models/
                news.py
            schemas/
                news.py
            crud/
                news.py
            routers/
                news.py
            main.py

    scraping/
        scrapers/
            prothom_alo.py
        services/
            database_writer.py
        config/
            settings.py

    tests/
    .env.example
    requirements.txt
    README.md
```

## Ethical Scraping Notes

1. Respect Prothom Alo website terms.
2. Use polite request timing.
3. Avoid sending too many requests in a short time.
4. Store source URLs with every scraped record.
5. Do not republish copyrighted article content without permission.
6. Use scraped data responsibly for learning, indexing, or internal analysis.

## Limitations

1. Current scraping extracts title and links only.
2. Full article body extraction is not implemented in the visible code.
3. The current scraper targets a fixed Prothom Alo page.
4. The API currently supports listing and creating records only.
5. Code formatting cleanup is needed before normal execution.
6. No authentication is included.
7. No Docker setup is included.
8. No tests are included.
9. No license file is visible.

## License

No license file was visible in the repository when this README was prepared. Add a license file before public reuse or deployment.

## Author

Miraz Uddin Chowdhury

Repository:

```text
https://github.com/mirazchowdhury/prothom-alo-news-project
```
