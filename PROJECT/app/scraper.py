import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    try:
        response = requests.get(url)
        
        # Check if the request was successful 
        if response.status_code != 200:
            print(f"Error: Failed to fetch the page. Status code: {response.status_code}")
            return None

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find('div', {'id': 'bodyContent'})

        if content_div:
            # Extract all the paragraphs in the article
            paragraphs = content_div.find_all('p')
            article_text = ' '.join([para.get_text() for para in paragraphs])
            return article_text
        else:
            print("Error: Article content not found.")
            return None

    except Exception as e:
        print(f"Error scraping the article: {e}")
        return None
