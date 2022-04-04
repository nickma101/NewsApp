"""
Define experimental settings as json dictionary (article retrieval & display)
"""
experiment1 = {"no_articles_displayed": 8,
               "project": 9,
               "articleset": 2564,
               "start_date": "2021-03-16",
               "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser", "id")} ##add topic
# Article input: images, headlines, teasers, text
# Experimental input: nudging settings, articleset

def get_settings(name: str):
    return globals()[name]
