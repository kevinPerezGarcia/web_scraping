import requests
from lxml import html

url = "https://www.wikipedia.org/"
headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

parsed_html = html.fromstring(response.content)

english = parsed_html.get_element_by_id("js-link-box-en")
print(english.text_content())

languages = parsed_html.find_class("central-featured-lang")

for language in languages:
    print(language.text_content())
