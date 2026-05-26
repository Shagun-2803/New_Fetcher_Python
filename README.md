News App :
A simple Python CLI application that fetches and displays the latest news headlines by category using the NewsAPI.

Features:
1. Fetch top headlines from different categories
2. Simple command-line interface
3. Uses environment variables for API security

Displays:
1. News title
2. Author name
3. Source name
4. Categories Available
5. business
6. entertainment
7. general
8. health
9. science
10. sports
11. technology
Technologies Used:

Python
Requests Library
Dotenv
NewsAPI

Project Structure:
news-app/
│
├── main.py
├── .env
├── requirements.txt
└── README.md

Installation:
1. Clone the repository
git clone <your-repository-link>
cd news-app
2. Install dependencies
pip install -r requirements.txt
Setup API Key

Create a .env file in the root directory:

API_KEY=your_newsapi_key

Get your API key from:
NewsAPI

Run the Program
python main.py
Example Output
Available Categories:
business
entertainment
general
health
science
sports
technology

Enter required category: technology

1: Apple launches new AI features
--> Author Name: John Doe
--> Source Name: TechCrunch
--------------------------------------------------
Requirements

Add this to requirements.txt:

requests
python-dotenv
Concepts Practiced
API handling
JSON parsing
Functions in Python
Environment variables
Loops and conditionals
User input validation
