"""
Define experimental settings as json dictionary (article retrieval & display)
"""


article_set1 = {"project": 122,
               "amcat_article_set": 6832,
               "articleSet_int": 1,
               "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                           "id", "articleSet")}

article_set2 = {"project": 122,
                "amcat_article_set": 6832,
                "articleSet_int": 2,
                "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                            "id", "articleSet")}

article_set3 = {"project": 122,
                "amcat_article_set": 6832,
                "articleSet_int": 3,
                "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                            "id", "articleSet")}

article_set4 = {"project": 122,
                "amcat_article_set": 6832,
                "articleSet_int": 4,
                "columns": ("date", "title", "publisher", "url", "image_url", "text", "author", "section", "teaser",
                            "id", "articleSet")}


def get_settings(name: str):
    return globals()[name]
