import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from bs4 import BeautifulSoup
from typing import List

def scrape_website(website_url):
    print("Launching chrome browser")
    chrome_driver_path = "./chromedriver"  
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    
    # Add common user agents
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/122.0.0.0'
    ]

    
    # Configure Chrome options to avoid detection
    options.add_argument(f'user-agent={random.choice(user_agents)}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(service=service, options=options)
    
    # Add webdriver stealth properties
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    try:
        # Add random delay before accessing the site (1-3 seconds)
        time.sleep(random.uniform(1, 3))
        
        driver.get(website_url)
        print("Page loaded successfully")
        
        # Random scroll behavior to mimic human
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        for i in range(3):
            driver.execute_script(f"window.scrollTo(0, {scroll_height/4 * (i+1)});")
            time.sleep(random.uniform(0.5, 1.5))
            
        html = driver.page_source
        print("HTML content retrieved successfully")
        
        # Random delay before closing (2-4 seconds)
        time.sleep(random.uniform(2, 4))
        
        return html
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        driver.quit()
        

def extracr_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return None


def clean_body_content(body_content):
    print(body_content)
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_style in soup(['script', 'style']):
        script_style.extract()
    
    # 
    cleaned_text = soup.get_text(separator='\n')
    #remove extra whitespace
    cleaned_text = "\n".join(line.strip() for line in cleaned_text.splitlines() if line.strip())
    return cleaned_text


def split_dom_content(dom_content: str, max_length: int = 6000) -> List[str]:
    # This function splits a long DOM content string into smaller chunks
    
    # Uses list comprehension to create chunks by slicing the string
    # from position i to i+max_length in steps of max_length
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]