from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
y_c_web_page = response.text
# print(y_c_website)

soup = BeautifulSoup(y_c_web_page, "html.parser")

# store the title of first article under article_text
article_texts = []
article_links = []
article_tag = soup.find_all(name="a", class_="titlelink")
for article in article_tag:  # getting hold of all article heading texts and links and scores using findall
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

# printing only int portion of upvotes

article_upvotes = [int(article_upvote.getText().split()[0]) for article_upvote in
                   soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)

# print(article_upvotes)
highest_upvote = max(article_upvotes)
highest_upvote_index = article_upvotes.index(highest_upvote)
# print(highest_upvote_index)

highest_title = article_texts[highest_upvote_index]   # getting the details of most rated article
highest_link = article_links[highest_upvote_index]
print(highest_title)
print(highest_link)
print(highest_upvote)
