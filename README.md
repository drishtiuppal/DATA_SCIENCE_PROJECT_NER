# News Article Analyzer
This project is a Python-based application that allows users to scrape data from news articles using URLs, extract entities (persons and organizations), analyze the sentiment of the articles (positive, negative, neutral), store results in a database, and deploy the application using Docker.

# Features
**Web Scraping**: Extracts the main content from static HTML pages using BeautifulSoup.

**Entity Extraction**: Identifies PERSON and ORG entities from the article using spaCy.

**Sentiment Analysis**: Classifies the sentiment of articles as positive, negative, or neutral using TextBlob.

**Database Integration**: Stores URLs, extracted entities, sentiment, and timestamps in a SQLite database.

**Web UI**: Simple HTML interface built with Flask to input URLs and display results.

**Containerized Deployment**: Dockerized application for easy deployment.
