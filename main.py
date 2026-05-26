import requests

from dotenv import load_dotenv
import os

load_dotenv()

class newsFetcher:
  def __init__(self):
    self.categories = [
      "business",
      "entertainment",
      "general",
      "health",
      "science",
      "sports",
      "technology"
    ]

    self.API_KEY = os.getenv("API_KEY")


  def fetch_news(self,category):
      url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={self.API_KEY}"
      response = requests.get(url)
      data = response.json()
      return data
    
  def is_valid_category(self,category):
    if category in self.categories:
      return True
    else:
      return False

  def display_news(self,data):
    for index,article in enumerate(data["articles"] , start= 1):
      print(f"{index}: {article.get('title')}")
      print(f"--> Author Name: {article.get('author')}")
      print(f"--> Source Name: {article.get('source', {}).get('name')}")
      print("-"*50)


newsapp= newsFetcher()

def main():
  
  while True:
    print("Available Categories: ")
    for category in newsapp.categories:
      print(category)

    input_category = input("Enter required category: ").lower()
    if newsapp.is_valid_category(input_category):
      data = newsapp.fetch_news(input_category)
      newsapp.display_news(data)
      break

    else:
      print("Enter Valid Category!")

main()








