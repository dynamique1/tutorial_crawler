# Transcript Crawler

## Overview
This Python script demonstrates a basic understanding of web scraping using Scrapy. It is designed to crawl a specific website, subslikescript.com, to extract movie transcripts.

## Requirements
- Python 3.x
- Scrapy

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

pip install scrapy

## Usage
1. Navigate to the project directory in your terminal.
2. Run the spider using the following command:
scrapy crawl transcript_crawler -o output.json


Replace `output.json` with the desired output file format (e.g., CSV, XML).

## Spider Details
- **Name**: transcript_crawler
- **Allowed Domains**: subslikescript.com
- **Start URL**: https://subslikescript.com/movies_letter-X
- **Rules**:
- Extract links to individual movie transcripts using XPath from the page.
- Follow pagination links to crawl through multiple pages.
- **Data Extraction**:
- Title: Extracted from the `<h1>` tag within the main article.
- Plot: Extracted from the `<p>` tag within the main article.
- URL: URL of the current page.

## Notes
- Ensure proper usage of web scraping by reviewing the website's terms of service and robots.txt file.
- Customize the XPath expressions and rules as per the structure of the target website.
- Handle potential errors and edge cases gracefully to maintain the robustness of the script.

## Disclaimer
This script is provided for educational purposes only. Use it responsibly and respect the website's terms of service and copyright policies.
