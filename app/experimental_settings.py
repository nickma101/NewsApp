"""
Define experimental settings as json dictionary (article retrieval & display)
"""
experiment1 = {"no_articles_displayed":2,"project":9, "articleset":2564, "start_date": "2021-03-16", "columns": ("date", "title", "publisher", "url", "text", "author", "section")}

def get_settings(name: str):
    return globals()[name]
