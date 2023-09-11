import time
import requests
from parsel import Selector
# from tech_news.database import create_news

# Requisito 1


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=1, headers=headers)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    try:
        return (
            Selector(html_content).css(".entry-title a::attr(href)").getall()
        )
    except IndexError:
        return None


# Requisito 3
def scrape_next_page_link(html_content):
    return Selector(html_content).css(".nav-links a.next::attr(href)").get()

# Requisito 4


def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    date = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = selector.css(".meta-reading-time::text").get()
    minutes = reading_time.split(" ")[0]
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    return_summary = "".join(summary).strip()
    category = selector.css(".label::text").get()

    return_all = {
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": writer,
        "reading_time": int(minutes),
        "summary": return_summary,
        "category": category,
    }
    return return_all


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
