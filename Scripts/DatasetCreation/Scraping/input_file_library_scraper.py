import os
import sys
sys.path.append(os.getcwd())
import requests
import fpdf
from bs4 import BeautifulSoup


# URL of the page to scrape
# Instantiate a PDF writer object, because this keeps account of the sections of the website
output_pdf = fpdf.FPDF(format='letter')
input_library_text = ""

text = ""
base_url = "https://sites.google.com/"
starting_url = "https://sites.google.com/site/orcainputlibrary/"
response = requests.get(starting_url)
soup = BeautifulSoup(response.text, 'html.parser')
li_link_tags = soup.find_all('li', jsname='ibnC6b')

links = list(set([link['href'] for li_tag in li_link_tags[2:] for link in li_tag.find_all('a')]))
for i, link in enumerate(links):
    print(f"Scraping: {link}")
    response = requests.get(f"{base_url}{link}")
    soup = BeautifulSoup(response.text, 'html.parser')
    nav_tags = soup.find_all('nav')
    for nav_tag in nav_tags:
        nav_tag.decompose()
    text = ' '.join(soup.stripped_strings)
    text = text.replace("Search this site Skip to main content Skip to navigation ORCA Input Library ", "")
    
    input_library_text += text
    # Add the text as a page to the PDF
    output_pdf.add_page() #create new page
    text = text.encode('latin-1', 'replace').decode('latin-1')
    output_pdf.set_font("Arial", size=5) # font and textsize
    output_pdf.cell(5, txt=text, align="L")

output_pdf.output(os.path.join('Data','Documents','Manual','orca_input_file_library.pdf'))