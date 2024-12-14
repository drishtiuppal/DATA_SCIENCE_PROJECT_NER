import sqlite3

conn = sqlite3.connect('articles.db')

# Create a cursor object
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

cursor.execute("SELECT * FROM articles;")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()