import requests

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

for index,article in enumerate(data["articles"] , start= 1):
  print(f"{index}: {article.get('title')}")
  print(f"--> Author Name: {article.get('author')}")
  print(f"--> Source Name: {article.get('source', {}).get('name')}")
print(response)
