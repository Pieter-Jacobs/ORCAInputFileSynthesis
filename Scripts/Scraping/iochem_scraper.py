import os
import random
import string
import requests
from bs4 import BeautifulSoup


def download_file(url, folder):
    response = requests.get(url)
    filename = os.path.join(folder, url.split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(response.content)


def generate_random_suffix(length=8):
    """Generate a random suffix of given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def get_unique_filename(filepath):
    """Get a unique filename by adding a random suffix."""
    if not os.path.exists(filepath):
        return filepath
    filename, ext = os.path.splitext(filepath)
    random_suffix = generate_random_suffix()
    filepath = f"{filename}_{random_suffix}{ext}"
    return filepath


# URL of the page to scrape
base_url = "https://iochem-bd.bsc.es/"
url = 'https://iochem-bd.bsc.es/browse/simple-search?query=orca'
scraping = True

# Initialize the
# WebDriver
# driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed and in PATH
page_nr = 7338

while scraping:
    # Fetch the page content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if len(soup.find_all('span', string='next')) > 0:
        print("Done scraping")
        scraping = False

    # Find all links to the details page
    links = soup.find_all('a')
    next_button_link = soup.find_all('a', string='next')[-1]['href']

    links_to_click = [
        link for link in links if "browse/handle" in link['href']]

    tr_tags = [link.find_parent('tr') for link in links_to_click]
    meta_data = [[td.get_text(strip=True)
                  for td in tag.find_all('td')[4:8]] for tag in tr_tags]

    # Loop through each link and scrape ORCA input file
    for i, link in enumerate(links_to_click):
        detail_url = link['href']
        response = requests.get(f"{base_url}/{detail_url}")
        # Here I want to click the button and download the file
        try:
            # Parse the page source with BeautifulSoup
            detail_soup = BeautifulSoup(response.text, 'html.parser')

            # Find all download buttons
            download_buttons = detail_soup.find_all(
                'a', href=True, text="Download")

            # Filter out the buttons with href ending in '.inp'
            orca_download_buttons = [
                button for button in download_buttons if 'inp' in button['href']]

            for orca_button in orca_download_buttons:
                download_url = base_url + orca_button['href']
                response = requests.get(download_url)
                filename = os.path.join(
                    f'Data{os.sep}ioChem', download_url.split('/')[-1])

                meta_data_string = '_'.join(meta_data[i])
                filename = get_unique_filename(
                    filename + "_" + meta_data_string)

                with open(filename, 'wb') as f:
                    f.write(response.content)

        except Exception as e:
            print(f"Failed to scrape {detail_url}: {e}")

    # Go to next
    url = f"{base_url}/{next_button_link}"
    page_nr += 1
