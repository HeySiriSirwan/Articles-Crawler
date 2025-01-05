from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = '######'

service = Service(driver_path) 
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service, options=options)
articles = []
for i in range(158,195):
    url = f"https://www.sciencedirect.com/journal/journal-of-the-mechanics-and-physics-of-solids/vol/{i}/suppl/C"
    driver.get(url)
    time.sleep(10)
    try:
        accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()
    except:
        pass
    for i in range(5): 
            driver.execute_script("window.scrollBy(0, 800);") 
            time.sleep(1)
    issue_status_element = driver.find_element(By.CSS_SELECTOR, "h3.js-issue-status.text-s")
    issue_status = issue_status_element.text
    article_titles = driver.find_elements(By.CSS_SELECTOR, "span.js-article-title.text-l")
    titles = [title.text for title in article_titles]
    articles.append(issue_status)
    for title in titles:
        articles.append(title)
        print(issue_status,title)
