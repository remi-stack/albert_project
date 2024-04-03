#main script is used to run the whole project and get the final output
#It is used to call the functions from other scripts and run the project
from scripts.datasourcing import fetch_quotes, csv_saving

def main():
    base_url = input("Enter the URL to scrape: ")
    quotes_data = fetch_quotes(base_url)
    df_sorted = csv_saving(quotes_data, 'data/quotes_script.csv')
    return df_sorted




if __name__ == '__main__':
    #url to paste : https://quotes.toscrape.com/
    print(main())
