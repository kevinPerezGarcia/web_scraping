import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)

parsed_html = BeautifulSoup(response.text)

question_stack = parsed_html.find(id="questions")

questions = question_stack.find_all(class_="s-post-summary")

for question in questions:
    title = question.find("h3").text
    description = question.find(class_="s-post-summary--content-excerpt").text
    description = description.replace("\n", "").replace("\r", "").strip()
    print(title)
    print(description)
