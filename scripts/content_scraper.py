import requests
from bs4 import BeautifulSoup

# Sources to scrape
SOURCES = [
    "https://stackoverflow.com",
    "https://www.freebuf.com",
    "https://dev.to",
    "https://www.infosecurity-magazine.com",
]

# AI rewriting function
def rewrite_content(text):
    """Use AI to rewrite content for uniqueness"""
    # In practice, this would call OpenAI API for rewriting
    return text.replace(" the ", " a ").replace(" is ", " was ")  # Simplified example

def scrape_content():
    articles = []
    for source in SOURCES:
        response = requests.get(source)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract articles - site-specific selectors
        if "stackoverflow" in source:
            items = soup.select('.question-summary')
        elif "freebuf" in source:
            items = soup.select('.article-item')
        else:
            items = soup.select('article')
        
        for item in items[:4]:  # Get first 4 articles
            title = item.select_one('h2, h3, .title').text.strip()
            content = item.select_one('.summary, .content, .excerpt').text.strip()
            articles.append({"title": title, "content": rewrite_content(content)})
    
    return articles