from datetime import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    return [
        (news["title"], news["url"])
        for news in search_news({"title": {"$regex": title, "$options": "i"}})
    ]


# Requisito 8
def search_by_date(date):
    try:
        new = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        result = search_news({"timestamp": {"$regex": new}})
        search_results = []
        for result in result:
            search_results.append((result["title"], result["url"]))
        return search_results
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"category": {"$regex": category, "$options": "i"}}
        )
    ]
