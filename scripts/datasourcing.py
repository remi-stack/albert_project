#data sourcing script
#create a .csv file with the data scraped from the website

#libraries
import requests  # for making HTTP requests to web pages
from bs4 import BeautifulSoup  # for parsing HTML content
import pandas as pd

# The base URL of the website we're scraping
base_url = 'https://quotes.toscrape.com/'

def fetch_quotes(page_url):
    """
    Fetch quotes and authors from a given page URL.

    Parameters:
    - page_url: URL of the page to scrape

    Returns:
    - A list of dictionaries, each containing an 'Author' and their 'Citation'
    """
    quotes_data = []  # Initialize an empty list to store quotes and authors
    response = requests.get(page_url)  # Make a GET request to fetch the page content

    if response.status_code == 200:  # Check if the request was successful (HTTP status code 200)
        soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content of the page
        # print(soup.prettify())
        quotes = soup.find_all('div', class_='quote')  # Find all quote blocks on the page

        for quote in quotes:  # Iterate over each quote block
            text_element = quote.find('span', class_='text')  # Find the element containing the quote text
            author_element = quote.find('small', class_='author')  # Find the element containing the author's name
            if text_element and author_element:  # Ensure both elements were found
                text = text_element.get_text(strip=True)  # Extract the text of the quote, stripping whitespace
                author = author_element.get_text(strip=True)  # Extract the author's name, stripping whitespace
                quotes_data.append({'Author': author, 'Citation': text})  # Add the quote and author to our list

        # Check for a link to the next page
        next_page = soup.find('li', class_='next')
        if next_page and next_page.find('a'):  # Ensure the next page link exists
            next_page_url = base_url + next_page.find('a')['href']  # Construct the URL for the next page
            quotes_data.extend(fetch_quotes(next_page_url))  # Recursively fetch quotes from the next page

    return quotes_data  # Return the list of quotes and authors


def csv_saving(data, filename):
    """
    Save the scraped data to a CSV file.

    Parameters:
    - data: List of dictionaries containing the scraped data
    - filename: Name of the CSV file to save
    """
    quotes_data = fetch_quotes(base_url)
    df = pd.DataFrame(data)  # Convert the list of dictionaries into a pandas DataFrame
    df_sorted = df.sort_values(by='Author').reset_index(drop=True)
    df.to_csv(filename, index=False)  # Save the DataFrame to a CSV file without row numbers
    return df_sorted  # Return the sorted DataFrame

# Start the scraping process from the first page of the site

if __name__ == '__main__':
    quotes_data = fetch_quotes(base_url)
    df_sorted = csv_saving(quotes_data, 'data/quotes_script.csv')
    print(df_sorted) # Display the sorted DataFrame
