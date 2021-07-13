from amcatclient import AmcatAPI
from app import es

amcat = AmcatAPI("https://vu.amcat.nl", "username", "password")
es = es

es.indices.create("articles")

for article in amcat.get_articles(project=69, articleset=2564, start_date="2021-03-09", columns=("date", "title", "publisher", "url", "text", "author", "section")):
    es.create(index="articles", id=article['id'], body=article)

