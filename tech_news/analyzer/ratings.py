# Requisito 0010

from tech_news.database import db

# Requisito 10


def top_5_categories():
    create = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]

    result_list = db.news.aggregate(create)

    categories = [category["_id"] for category in result_list]

    return categories
