import os
from flask import Flask, request, jsonify, render_template
from app.scraper import scrape_article
from app.ner import extract_entities
from app.sentiment import analyze_sentiment
from app.db_handler import initialize_database, save_to_database

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

initialize_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get('url')
    article_text = scrape_article(url)
    if not article_text:
        return jsonify({"error": "Unable to scrape the article. Please check the URL."}), 400

    entities = extract_entities(article_text)
    sentiment = analyze_sentiment(article_text)

    # Save to the database
    save_to_database(url, article_text, entities, sentiment)

    return jsonify({
        "url": url,
        "entities": entities,
        "sentiment": sentiment,
    })

if __name__ == "__main__":
    app.run(debug=True)
