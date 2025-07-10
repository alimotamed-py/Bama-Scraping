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

Install the required libraries:
pip install -r requirements.txt


 Usage
Run the scraper script:
python bama_scraper.py

The script will automatically:

Fetch listings from bama.ir

Parse the relevant data

Save results to:

output/data.json

output/data.xlsx

📂 Output Example
json
Copy
Edit
[
  {
    "title": "پژو 206 تیپ 2",
    "price": "540,000,000 تومان",
    "model": "1399",
    "mileage": "75,000 کیلومتر",
    "location": "تهران",
    "date_posted": "امروز"
  },
  ...
]
🧰 Future Improvements
 Add CLI support for selecting city or filters

 Add logging and error handling

 Build GUI with Tkinter or Streamlit

 Schedule scraper to run periodically

📄 License
This project is open-source under the MIT License.

🙋‍♂️ Author
Developed with 💻 by Ali Motamed
GitHub: @alimotamed-py




