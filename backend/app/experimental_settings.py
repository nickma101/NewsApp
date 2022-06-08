"""
Define experimental settings as json dictionary (article retrieval & display)
"""
experiment1 = {"project": 122,
               "amcat_article_set": 6113,
               "articleSet_int": 2,
               "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                           "id", "articleSet")}

article_set2 = {"project": 122,
                "amcat_article_set": 6113,
                "articleSet": 2,
                "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                            "id", "articleSet")}

article_set3 = {"project": 122,
                "amcat_article_set": 6113,
                "articleSet": 2,
                "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                            "id", "articleSet")}

article_set4 = {"project": 122,
                "amcat_article_set": 6113,
                "articleSet": 4,
                "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                            "id", "articleSet")}


# add 3 other conditions
def get_settings(name: str):
    return globals()[name]
