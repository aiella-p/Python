# Solution 1: Basic Web Scraper Using `requests` and `BeautifulSoup`
# Import necessary libraries
import requests  # Used to send HTTP requests
from bs4 import BeautifulSoup  # Used for parsing HTML content

# Function to extract data from the specified website
def scrape_h1_tags(url):
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the h1 tags on the page
        h1_tags = soup.find_all('h1')

        # Print the extracted h1 tags
        print(f"List all the h1 tags from {url}:")
        for tag in h1_tags:
            print(tag)
    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Specify the URL to scrape
url = "https://en.wikipedia.org/wiki/Main_Page"

# Call the function to scrape h1 tags
scrape_h1_tags(url)
