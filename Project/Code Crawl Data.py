from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import re

# Starting URL for crawling
start_url = "https://www.piaotia.com/html/11/11754/8287249.html"
# Output folder where the downloaded chapters will be stored
output_folder = r'C:\Users\dietr188\Desktop\Python-2025\Project\Data Crawl'
os.makedirs(output_folder, exist_ok=True)  # Ensure the directory exists

# Configure Chrome WebDriver options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without UI)
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration for better compatibility


def sanitize_filename(filename):
    """
    Remove illegal characters from filenames to prevent errors when saving files.
    """
    return re.sub(r'[\\/*?":<>|]', "", filename)


def clean_content(text):
    """
    Clean up the extracted text by removing unnecessary navigation words.
    """
    remove_words = ['上一章', '返回目录', '下一章', '返回书页']  # Words to remove
    for word in remove_words:
        text = text.replace(word, '')
    lines = text.split('\n')
    if len(lines) > 1:
        lines = lines[1:]  # Remove the first line if it exists
    return '\n'.join(lines).strip()  # Return cleaned text


def refine_title(title):
    """
    Refine the title by removing unwanted prefixes or restructuring chapter numbers.
    """
    if '正文' in title:
        title = title.split('正文')[-1].strip()  # Remove leading "正文" if present
    if '第' in title and '章' in title:
        title = title[title.index('第'):].strip()  # Extract the chapter number and name
    return title

# Start crawling from the first chapter
current_url = start_url

# Initialize WebDriver and start crawling
with webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=chrome_options) as driver:
    while current_url:
        try:
            # Load the webpage
            driver.get(current_url)
            time.sleep(2)  # Wait for the page to fully load

            # Extract the chapter title
            title = driver.find_element(By.TAG_NAME, 'h1').text.strip()
            refined_title = refine_title(title)

            # Extract the main content of the chapter
            content = driver.find_element(By.ID, 'content').text
            content = clean_content(content)  # Clean up unnecessary text

            # Sanitize the title for use as a filename
            safe_title = sanitize_filename(refined_title)
            filename = os.path.join(output_folder, f"{safe_title}.txt")

            # Save the chapter content to a text file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)

            print(f"Downloaded: {refined_title}")

            # Find the link to the next chapter
            next_chapter_link = driver.find_elements(By.LINK_TEXT, '下一章')
            if next_chapter_link:
                current_url = next_chapter_link[0].get_attribute('href')  # Get the URL of the next chapter
            else:
                print("No more chapters available.")
                break

        except Exception as e:
            print(f"Error downloading chapter from {current_url}: {e}")
            break

# Close the WebDriver
print("Download complete.")