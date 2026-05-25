import requests

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

categories = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology"
]

def fetch_news(category):
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data
  
def is_valid_category(category):
  if category in categories:
    return True
  else:
    return False

def display_news(data):
  for index,article in enumerate(data["articles"] , start= 1):
    print(f"{index}: {article.get('title')}")
    print(f"--> Author Name: {article.get('author')}")
    print(f"--> Source Name: {article.get('source', {}).get('name')}")
    print("-"*50)



def main():
  
  while True:
    print("Available Categories: ")
    for category in categories:
      print(category)

    input_category = input("Enter required category: ").lower()
    if is_valid_category(input_category):
      data = fetch_news(input_category)
      display_news(data)
      break

    else:
      print("Enter Valid Category!")

main()








