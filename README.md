# AI Web Scraper with Selenium and Ollama

A powerful web scraping tool that combines Selenium for robust web scraping with AI-powered content parsing using Ollama. This project provides a user-friendly Streamlit interface for scraping websites and extracting specific information using natural language instructions.

## Features

- 🔍 **Advanced Web Scraping**: Uses Selenium with anti-detection measures
- 🤖 **AI-Powered Parsing**: Leverages Ollama for intelligent content extraction
- 🎯 **Natural Language Queries**: Describe what you want to extract in plain English
- 🧹 **Smart Content Cleaning**: Removes scripts, styles, and unnecessary whitespace
- 📱 **User-Friendly Interface**: Built with Streamlit for easy interaction

## Prerequisites

- Python 3.8+
- Chrome browser installed
- ChromeDriver (included in the project)
- Ollama installed and running locally

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd scraper_Selenium
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter the URL of the website you want to scrape

4. Click "Scrape site" to retrieve the content

5. Enter a natural language description of what you want to extract from the content

6. Click "Parse content" to get the AI-processed results

## Project Structure

- `main.py`: Streamlit application interface
- `scrape.py`: Web scraping functionality using Selenium
- `parse.py`: AI-powered content parsing using Ollama
- `requirements.txt`: Project dependencies
- `chromedriver`: Chrome WebDriver executable

## Dependencies

- streamlit: Web application framework
- selenium: Web scraping
- beautifulsoup4: HTML parsing
- langchain: AI processing framework
- langchain_ollama: Ollama integration
- python-dotenv: Environment variable management

## Anti-Detection Features

The scraper includes several features to avoid detection:
- Random user agent rotation
- Human-like scrolling behavior
- Random delays between actions
- Disabled automation flags
- Stealth mode configuration

## Contributing

Feel free to submit issues and enhancement requests!

## Author

Danis Preldzic 
