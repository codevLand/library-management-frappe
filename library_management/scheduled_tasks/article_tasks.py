import datetime
import requests
from library_management.custom_routes import article

page = 1
print("out page: ", page)

def get_articles():
    x = datetime.datetime.now()
    print("fetching articles: {}".format(x.strftime('%c')))

def get_articles_all():
    x = datetime.datetime.now()
    print("fetching articles all: {}".format(x.strftime('%c')))

def get_articles_minutely():
    x = datetime.datetime.now()
    print("fetching articles minutely: {}".format(x.strftime('%c')))

def get_articles_cron_minute():
    x = datetime.datetime.now()
    print("fetching articles cron minute: {}".format(x.strftime('%c')))

    global page
    page += 1
    print("in page: ", page)
    # r = requests.get("https://api.nytimes.com/svc/books/v3/lists.json?api-key=pO57TobcZ9DL1t8gfBpf2YLYpLXVr72F&list=hardcover-fiction")
    # for item in r.json()["results"]:
    #     details = item["book_details"][0]
    #     article_data = {}
    #     article_data["article_name"]    = details["title"]
    #     article_data["description"]     = details["description"]
    #     article_data["author"]          = details["author"]
    #     article_data["isbn"]            = details["primary_isbn10"]
    #     article_data["publisher"]       = details["publisher"]
    #     article_data["route"]           = "articles/" + details["title"].lower().replace(" ", "-")
    #     article_data["status"]          = "Available"
    #     article_data["published"]       = 1

    #     new_article = article.create_article(**article_data)
    #     new_article.save()
        # print(article_data)


