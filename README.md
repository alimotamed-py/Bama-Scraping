# 🚗 Bama.ir Web Scraper

A powerful Python-based web scraper that extracts car listings from [bama.ir](https://bama.ir), using `requests` and `BeautifulSoup`. The extracted data can be saved in both **JSON** and **Excel** formats for further analysis.

## 🧠 About the Project

This project is designed to automate the process of collecting car advertisement data from bama.ir. It allows users to scrape multiple pages and extract structured data for use in data analysis, research, or personal records.

## ✨ Features

- ✅ Scrapes car listings with details like:
  - Car title
  - Price
  - Model year
  - Mileage (کارکرد)
  - Location
  - Posting date
- ✅ Handles multiple pages of listings
- ✅ Clean parsing using `BeautifulSoup`
- ✅ Saves output in:
  - `JSON`
  - `Excel (.xlsx)`

## 📦 Technologies Used

- Python `3.x`
- [`requests`](https://pypi.org/project/requests/) – for sending HTTP requests
- [`BeautifulSoup`](https://pypi.org/project/beautifulsoup4/) – for parsing HTML
- [`pandas`](https://pypi.org/project/pandas/) – for saving data to Excel

## 🚀 Getting Started

### 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alimotamed-py/bama-scraper.git
   cd bama-scraper
