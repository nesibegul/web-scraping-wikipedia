# Wikipedia Athletics Web Scraper

## Project Description
This project is a web scraping tool built from scratch using Scrapy.
The scraper extracts athletics competition results from Wikipedia,
transforms the data into a structured format, and saves it as a CSV file.

## Technologies Used
- Python
- Scrapy
- CSV

## Target Website
Wikipedia athletics competition result pages.

Example:
https://en.wikipedia.org/wiki/1992_World_Junior_Championships_in_Athletics_–_Men%27s_high_jump

## Extracted Data
- Medal
- Athlete Name

## How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/your-username/wikipedia-athletics-scraper.git
cd wikipedia-athletics-scraper

2. Install Dependencies

pip install -r requirements.txt

3. Run the spider and save data to csv

scrapy crawl athletics -o results.csv 

4. Output

The scraped data is saved in results.csv.


# Git Commit & Push

```bash

git init
git add .
git commit -m "Initial Scrapy project for Wikipedia athletics data"
git branch -M main
git remote add origin https://github.com/USERNAME/wikipedia-athletics-scraper.git
git push -u origin main
