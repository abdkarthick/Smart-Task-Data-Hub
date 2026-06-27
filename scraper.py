import requests
from bs4 import BeautifulSoup

def scrape_news():
    # The Hindu website la irundhu headlines 
    url = "https://www.thehindu.com/"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("\n" + "="*60)
        print("    THE HINDU - TOP HEADLINES 📰")
        print("="*60 + "\n")
        
        # Headlines eduka CSS selector
        headlines = soup.find_all('h3', class_='title', limit=10)
        
        if not headlines:
            headlines = soup.find_all('h3', limit=10)
        
        if len(headlines) == 0:
            print("Headlines still blocked. Website structure changed again.")
            return
        
        for i, headline in enumerate(headlines, 1):
            title = headline.get_text(strip=True)
            if title and len(title) > 10:  # Empty headlines 
                print(f"{i}. {title}\n")
        
        print("="*60)
        print("Scraping finished! ✓")
        
    except requests.exceptions.RequestException as e:
        print(f"Internet problem : {e}")
    except Exception as e:
        print(f"Error vandhuduchu: {e}")

if __name__ == "__main__":
    scrape_news()