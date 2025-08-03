# Croma Product Scraper

## Project Overview

This project is a full-stack web application that scrapes product information from [Croma's Televisions & Accessories](https://www.croma.com/televisions-accessories/c/997) page, stores the data in Redis, and displays it on a clean, responsive web interface. I completed tje unfinished parts as an assignment for Adeptmind to demonstrate my full-stack development capabilities.



## Setup Instructions

### Prerequisites
- Python 3.12 / 3.13
- Node.js
- Redis server running on localhost:6379

### Backend Setup


1. Set up a Python virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/macOS
   venv\Scripts\activate      # On Windows
   ```

2. Navigate to the backend folder and install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Run the scraper to fetch fresh data:
   ```bash
   python scraper.py
   ```

4. Start the Flask app:
   ```bash
   python app.py
   ```
   The API will be available at http://localhost:5000

### Frontend Setup

1. Open a new terminal window/tab
2. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Start the development server:
   ```bash
   npm run serve
   ```
   The frontend will be available at http://localhost:8080

## Quick Start (Using Run Script)

For convenience, you can use the provided run script that automates the entire process:

```bash
# Navigate to project root
cd scrapper

# Run the application
python run.py
```

The script will:
1. Run the scraper to collect fresh data
2. Start the Flask backend server
3. Launch the Vue.js frontend


## Features

- **Web Scraping**: Extracts product data (title, price, sale price, discount) from Croma's website using BeautifulSoup
- **Data Storage**: Stores scraped data in Redis as a JSON object
- **API**: Provides a REST API endpoint to retrieve the scraped data
- **Frontend Display**: Presents the scraped data in a responsive grid layout similar to Croma's design
- **Cross-platform**: Runs on multiple operating systems with minimal configuration

## Technologies Used

### Backend
- **Python 3.8+**: Core programming language
- **Flask**: Web framework for the API endpoints
- **BeautifulSoup4**: HTML parsing and web scraping
- **Redis**: In-memory data storage
- **Requests**: HTTP library for making web requests
- **lxml**: XML and HTML parser for improved performance

### Frontend
- **Vue.js**: JavaScript framework for building the user interface
- **HTML/CSS**: Structure and styling of the web application
- **Fetch API**: Making HTTP requests to the backend

## System Architecture

The application follows a standard client-server architecture:

1. **Scraper Component**: 
   - Python script using BeautifulSoup to extract product data from Croma
   - Parses HTML to find product cards and extract relevant information
   - Stores the structured data in Redis

2. **Backend Server**:
   - Flask application providing RESTful API endpoints
   - Retrieves data from Redis and serves it to the frontend
   - Handles error cases and data validation

3. **Redis Storage**:
   - In-memory database storing scraped content
   - Data stored as a JSON string under the key "scraped_content"
   - Provides fast access to the scraped data

4. **Frontend Application**:
   - Vue.js application rendering the product data
   - Responsive design adapting to different screen sizes
   - Product cards styled to resemble Croma's UI
## Limitations

- The scraper may not work properly if Croma changes their HTML structure
- The scraper only extracts a subset of product information (title, prices, discount percentage)
- There's no direct link back to the Croma product pages

## Acknowledgments

- This project was created as part of an assignment for Adeptmind's Full-Stack Internship program
- Special thanks to the AdeptMind Team for providing me such an opportunity

## Code Structure

```
scrapper/
├── backend/
│   ├── app.py                 # Flask application providing API endpoints
│   ├── requirements.txt       # Python dependencies
│   └── scraper.py             # Web scraping logic using BeautifulSoup
├── frontend/
│   ├── package.json           # NPM dependencies and scripts
|   ├── vue.config.js          # Proxy which redirects /api endpoint used in App.js to Flask App
│   └── src/                   # Vue application source code
│       ├── App.vue            # Main Vue component
│       ├── Product.vue        # Product card component
│       └── main.js            # Vue application entry point
├── run.py                     # Python script to run all components
└── README.md                  # Project documentation
```