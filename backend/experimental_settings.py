"""
Define experimental settings as json dictionary (article retrieval & display)
"""
experiment1 = {"no_articles_displayed": 8,
               "project": 9,
               "amcat_article_set": 2564,
               "start_date": "2021-03-16",
               "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                           "id")}  # add topic

article_set2 = {"no_articles_displayed": 8,
               "project": 9,
               "amcat_article_set": 2564,
               "start_date": "2021-03-16",
               "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                           "id")}  # add topic

article_set3 = {"no_articles_displayed": 8,
               "project": 9,
               "amcat_article_set": 2564,
               "start_date": "2021-03-16",
               "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                           "id")}  # add topic

article_set4 = {"no_articles_displayed": 8,
               "project": 9,
               "amcat_article_set": 2564,
               "start_date": "2021-03-16",
               "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                           "id")}  # add topic

# add 3 other conditions

def get_settings(name: str):
    return globals()[name]
