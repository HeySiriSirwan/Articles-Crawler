# Articles-Crawler

**Articles-Crawler** is a Python tool designed to crawl and extract articles from journal websites. Users can analyze word trends (annual and monthly) and generate word clouds to visualize word frequency.

⚠ **Note:** This project requires user customization. You need to configure the target journal website and provide the path to your Chrome WebDriver.

---

## Features

- **Customizable Crawling**: Configure the tool to extract articles from your preferred journal website.
- **Word Trend Analysis**: Analyze word usage trends annually and monthly.
- **Word Cloud Generation**: Visualize word frequency with word clouds.

---

## Requirements

- Python 3.x
- Google Chrome installed
- Chrome WebDriver (compatible with your Chrome version)
- Required Python libraries (`requirements.txt`)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HeySiriSirwan/Articles-Crawler.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Articles-Crawler
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Download the correct version of the [Chrome WebDriver](https://chromedriver.chromium.org/) that matches your Chrome version.

---

## Configuration

### 1. Set Your Journal Website
Edit the `crawler.py` file to include the URL(s) of the journal website(s) you want to crawl.

   ```python
   target_url = "https://example-journal.com"  # Replace with your journal website
  ```

### 2. Provide Chrome WebDriver Path
Update the `chromedriver_path` variable in `crawler.py` with the path to your Chrome WebDriver.

   ```python
   chromedriver_path = "/path/to/your/chromedriver"  # Replace with your WebDriver path
   ```

---

## Usage

1. Run the main crawler script to collect articles:

   ```bash
   python crawler.py
   ```

   This will extract articles from the configured journal website.

2. Analyze annual word trends:

   ```bash
   python annual_word_trends.py
   ```

3. Analyze monthly word trends:

   ```bash
   python monthly_word_trends.py
   ```

4. Analyze monthly trends for a specific word:

  ```bash
   python monthly_word_trends_per_word.py
   ```

5. Generate a word cloud:

   ```bash
   python word_cloud.py
   ```

---

## Project Structure

