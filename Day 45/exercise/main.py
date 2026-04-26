from bs4 import BeautifulSoup
import requests
# import lxml

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_score_index = article_upvotes.index(max(article_upvotes))

print(article_texts[highest_score_index])
print(article_links[highest_score_index])


# print(f"Title: {text} | URL: {link} | Upvotes: {article_upvote}")






# <td class="subtext">
#          <span class="subline">
#           <span class="score" id="score_40717797">
#            60 points
#           </span>


# with open('website.html') as file:
#     website = file.read()
#
# soup = BeautifulSoup(website, 'html.parser') # or lxml.parser
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.h1)
# print(soup.li)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# print(type(all_anchor_tags))
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     tag.get('href')

# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one("p a")
# name = soup.select_one("#name")
# headings = soup.select(selector=".heading")
# print(company_url)
# print(name)
# print(headings)