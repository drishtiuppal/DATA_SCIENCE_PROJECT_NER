import sqlite3

DB_NAME = "articles.db"

def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        article_text TEXT,
        entities TEXT,
        sentiment TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def save_to_database(url, article_text, entities, sentiment):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO articles (url, article_text, entities, sentiment)
                      VALUES (?, ?, ?, ?)''', (url, article_text, str(entities), sentiment))
    conn.commit()
    conn.close()
