# Price Scraper and Web Content Extractor

This project contains Python scripts for web scraping tasks, designed to extract product prices and web content efficiently from various websites. It includes error handling, automated scheduling, and support for both single and batch URL processing.

## Features
- **Product Price Extraction**: Scrapes product prices and names from e-commerce websites and saves them to a text file.
- **Content Scraper**: Extracts paragraph content (`<p>` elements) from web pages.
- **Command-Line Interface**: Provides user-friendly CLI options for scraping a single URL or batch URLs from a file.
- **Automated Scheduling**: Includes functionality to schedule daily scraping tasks to avoid triggering rate limits.
- **Dynamic Dependency Management**: Automatically installs required Python packages if they are not already installed.

## Requirements
- Python 3.6 or higher
- Required Python libraries:
  - `argparse`
  - `requests`
  - `beautifulsoup4`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/price-scraper.git
   cd price-scraper
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Price Comparison Script
Run the script to scrape product prices:
```bash
python price_comparison.py --url "<product_url>"
```
To process multiple URLs from a file:
```bash
python price_comparison.py --file <file_path>
```
The script will save the product names and prices to `prices.txt`.

### Web Content Scraper
Run the script to scrape `<p>` content from a web page:
```bash
python content_scraper.py --url "<target_url>"
```
To process multiple URLs from a file:
```bash
python content_scraper.py --file <file_path>
```

## File Descriptions
- **`price_comparison.py`**: A script to extract and save product prices.
- **`content_scraper.py`**: A script to scrape paragraph content from web pages.
- **`requirements.txt`**: Contains the list of required Python packages.

## Notes
- Add a delay between requests (e.g., 24 hours in the current setup) to avoid triggering rate-limiting mechanisms.
- Ensure URLs provided are valid and accessible.
- Modify headers in the script if required for specific websites.

## License
This project is licensed under the MIT License. Feel free to modify and use it as needed.

---

Happy scraping!

