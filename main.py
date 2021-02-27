# coding: utf-8
import requests
from bs4 import BeautifulSoup
# import chardet
# import re
# import newspaper
# import nltk

# url = "https://www.tohoku.ac.jp/japanese/target/student.html"
# site = requests.get(url)
# soup = BeautifulSoup(site.text, "html.parser")
# print(soup.find_all("div", {"class": "entry"}))

url = "http://www2.he.tohoku.ac.jp/zengaku/zengaku_info_g.html"
site = requests.get(url)
soup = BeautifulSoup(site.content, "html.parser")
divTags = soup.find_all(id="content_box")
print(divTags)
# test = [divTag.get("a").get("href") for divTag in divTags]
# print(test)
# for item in range(len(website.articles)):
#     web_article = website.articles[item]
#     web_url = web_article.url
#     try:
#         web_article.download()
#         web_article.parse()
#         web_article.nlp()
#         print("記事["+str(item)+"]:"+web_article.url+web_article.summary+"\n")
#     except:
#         print("記事["+str(item)+"]:"+web_url+"取得エラー"+"\n")
# article = Article(url)
# article.download()
# article.parse()
# article.nlp()

# print(article.title)
# print(article.summary)
